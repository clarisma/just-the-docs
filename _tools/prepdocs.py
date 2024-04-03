from pathlib import Path
import os
import re

operators = [
    ('+', '__add__'),
    ('-', '__sub__'),
    ('&', '__and__'),
    ('|', '__or__'),
]


class Page:
    def __init__(self, name, filename, lines):
        self.name = name
        self.filename = filename
        self.lines = lines

    def save(self):
        directory = os.path.dirname(self.filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        with open(self.filename, 'w') as file:
            file.writelines(line + '\n' for line in self.lines)


class ApiObject:
    def __init__(self, page, name):
        self.page = page
        self.name = name


class Class(ApiObject):
    def __init__(self, page, name):
        super().__init__(page, name)
        self.methods = {}
        self.properties = {}

    def add_method(self, method):
        self.methods[method.name] = method
        method.parent = self

    def add_property(self, property):
        self.properties[property.name] = property
        property.parent = self


class Module(ApiObject):
    def __init__(self, page, name):
        super().__init__(page, name)
        self.classes = {}
        self.methods = {}
        self.properties = {}

    def add_class(self, c):
        self.classes[c.name] = c
        c.parent = self

    def add_method(self, method):
        self.methods[method.name] = method
        method.parent = self

    def add_property(self, property):
        self.properties[property.name] = property
        property.parent = self


class Param:
    def __init__(self, name, is_keyword, default):
        self.name = name
        self.is_keyword = is_keyword
        self.default = default


class Member(ApiObject):
    def __init__(self, page, name, version=None):
        super().__init__(page, name)
        self.version = version

    def append_stub(self, buf):
        if self.name == self.parent.name:
            prefix = self.parent.parent.name  # For constructor, use module instead of class
        else:
            prefix = self.parent.name

        buf.append('<h3 id="')
        if isinstance(self.parent, Class):
            buf.append(self.parent.name)
            buf.append('_')
        buf.append(self.name)
        buf.append('" class="api"><span class="prefix">')
        buf.append(prefix)
        buf.append('.</span><span class="name">')
        buf.append(self.name)
        buf.append('</span>')

    def append_version(self, buf):
        if self.version:
            buf.append('<del>')
            buf.append(self.version)
            buf.append('</del>')
        buf.append("</h3>")


class Method(Member):
    def __init__(self, page, name, version=None):
        super().__init__(page, name, version)
        self.params = []

    def add_param(self, param):
        self.params.append(param)

    def format_html(self):
        buf = []
        self.append_stub(buf)
        buf.append('<span class="paren">(</span>')
        is_first_param = True
        for param in self.params:
            if not is_first_param:
                buf.append(", ")
            is_first_param = False
            if not param.is_keyword:
                buf.append('<i>')
            buf.append(param.name)
            if not param.is_keyword:
                buf.append('</i>')
            if param.default:
                buf.append('=')
                buf.append('<span class="default">')
                buf.append(param.default)
                buf.append('</span>')
        buf.append('<span class="paren">)</span>')
        self.append_version(buf)
        buf.append('<div class="api" markdown="1">')
        return ''.join(buf)


class Property(Member):
    def __init__(self, page, name, version=None):
        super().__init__(page, name, version)

    def format_html(self):
        buf = []
        self.append_stub(buf)
        self.append_version(buf)
        buf.append('<div class="api" markdown="1">')
        return ''.join(buf)


class ApiDocProcessor:
    def __init__(self):
        self.pages = []
        self.modules = {}
        self.classes = {}
        self.current_module = None
        self.current_class = None
        self.current_method = None
        self.current_property = None

    def process_files(self, path_str):
        path = Path(path_str)
        for filename in path.rglob('*.md'):
            with open(filename, 'r') as file:
                lines = file.readlines()
            dest_filename = str(filename)[len(path_str) + 1:]
            name = '/' + dest_filename[:-3]
            page = Page(name, dest_filename, lines)
            self.pages.append(page)

        for page in self.pages:
            self.process_page_commands(page)
        for page in self.pages:
            self.resolve_api_links(page)
        for page in self.pages:
            page.save()

    def process_page_commands(self, page):
        self.current_module = None
        self.current_class = None
        self.current_method = None
        self.current_param = None
        self.current_property = None

        in_code = False

        new_lines = []
        for line in page.lines:
            if line.startswith('>'):
                cmdline = line[1:].strip()
                if cmdline.startswith('.'):
                    line = self.process_command(page, cmdline)
            elif line.startswith('```'):
                in_code = not in_code
            elif line.startswith('#') and not in_code:
                # End the current API section whenever we encounter a heading
                if self.current_property or self.current_method:
                    self.current_property = None
                    self.current_method = None
                    new_lines.append('</div>')
            new_lines.append(line.rstrip())
        page.lines = new_lines

    def process_command(self, page, line):
        if line.startswith(".module"):
            return self.process_module_command(page, line[7:].strip())
        if line.startswith(".class"):
            return self.process_class_command(page, line[6:].strip())
        if line.startswith(".method"):
            return self.process_method_command(page, line[7:].strip())
        if line.startswith(".property"):
            return self.process_property_command(page, line[9:].strip())
        if line.startswith(".end"):
            return self.process_end_command(page, line[4:].strip())
        raise RuntimeError("Unknown command: " + line)

    def process_module_command(self, page, cmd):
        module_name = cmd
        m = self.modules.get(module_name, None)
        if not m:
            m = Module(page, module_name)
            self.modules[module_name] = m
        self.current_module = m
        return ""

    def process_class_command(self, page, cmd):
        class_name = cmd
        c = self.classes.get(class_name, None)
        if not c:
            c = Class(page, class_name)
            self.classes[class_name] = c
            self.current_module.add_class(c)
        self.current_class = c
        # TODO: would be better to set ID of next heading
        return f'<a id="{class_name}"></a>'

    def process_method_command(self, page, cmd):
        n = cmd.find('(')
        n2 = cmd.rfind(')')
        if n < 0 or n2 < 0:
            raise RuntimeError("Expected (args) in " + cmd)
        method_name = cmd[:n].strip()
        args = cmd[n + 1:n2]
        version = cmd[n2 + 1:].strip()
        method = Method(page, method_name, version)
        if self.current_class:
            self.current_class.add_method(method)
        elif self.current_module:
            self.current_module.add_method(method)
        else:
            raise RuntimeError("Must set .class or .module")

        args = args.strip().split(',')
        for arg in args:
            arg = arg.strip()
            if not arg:
                continue
            n = arg.find('=')
            if n < 0:
                param_name = arg
                default_value = None
            else:
                param_name = arg[:n].strip()
                default_value = arg[n + 1:].strip()
            if param_name[0] == '*':
                if param_name[-1] != '*':
                    raise RuntimeError("Expected *arg* in " + cmd)
                param_name = param_name[1:-1]
                is_keyword = False
            else:
                is_keyword = True
            method.add_param(Param(param_name, is_keyword, default_value))

        close_tag = ""
        if self.current_method or self.current_property:
            self.current_method = None
            self.current_property = None
            close_tag = "</div>"
        self.current_method = method
        return close_tag + method.format_html()

    def process_property_command(self, page, cmd):
        n = cmd.find(' ')
        if n < 0:
            properties = cmd
            version = None
        else:
            properties = cmd[0:n].strip()
            version = cmd[n + 1:].strip()

        tags = ""
        if self.current_method or self.current_property:
            self.current_method = None
            self.current_property = None
            tags = "</div>"
        for property_name in properties.split(','):
            property_name = property_name.strip()
            prop = Property(page, property_name, version)
            if self.current_class:
                self.current_class.add_property(prop)
            elif self.current_module:
                self.current_module.add_property(prop)
            else:
                raise RuntimeError("Must set .class or .module")
            tags += prop.format_html()
        self.current_property = prop
        return tags

    def process_end_command(self, page, cmd):
        close_tag = ""
        if cmd == "class":
            self.current_class = None
        if self.current_method or self.current_property:
            self.current_method = None
            self.current_property = None
            close_tag = "</div>"
        return close_tag

    def replace_markdown_links(self, line):
        # Regular expression to match Markdown links
        pattern = r'\[([^\]]+)\]\(([^\)]+)\)'

        # Callback function for re.sub to replace the matched link
        def replace_callback(match):
            link_text = match.group(1)
            old_link = match.group(2)
            new_link = self.resolve_api_link(old_link)
            return f"[{link_text}]({new_link})"

        return re.sub(pattern, replace_callback, line)

    def resolve_api_link(self, link):
        if not link.startswith('#'):
            return link
        name = link[1:]
        n = name.find('.')
        if n < 0:
            # potential link to class
            c = self.classes.get(name)
            if c:
                link = c.page.name + '#' + c.name
        else:
            class_name = name[0:n]
            member_name = name[n + 1:]
            c = self.classes.get(class_name)
            if c:
                prefix = class_name + '_'
            else:
                c = self.modules.get(class_name)
                prefix = ""
            if c:
                method = c.methods.get(member_name)
                if method:
                    link = method.page.name + '#' + prefix + method.name
                else:
                    prop = c.properties.get(member_name)
                    if prop:
                        link = prop.page.name + '#' + prefix + prop.name
        return link

    def resolve_api_links(self, page):
        new_lines = []
        for line in page.lines:
            new_lines.append(self.replace_markdown_links(line))
        page.lines = new_lines


if __name__ == '__main__':
    processor = ApiDocProcessor()
    processor.process_files("_source")
