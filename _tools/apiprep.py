import io

def parse_api_command(s):
    buf = io.StringIO()
    n = s.find('(')
    full_name = (s if n < 0 else s[:n]).strip()
    args = s[n:] if n > 0 else ''
    n = full_name.rfind('.')
    prefix = full_name[:n]
    name = full_name[n+1:]
    id = full_name.replace('.', '_')
    buf.write(
        f'<h1 id="{id}">'
        f'<span class="apicontext">{prefix}.</span>'
        f'<b>{name}</b>')

    italics = False
    for ch in args:
        if ch=='*':
            italics = not italics
            buf.write('<i>' if italics else '</i>')
        else:
            buf.write(ch)
    
    buf.append('\n')
    html = buf.getvalue()
    buf.close()
    return (full_name, prefix, name, html)

def end_api_doc(res):
    res.append("</div>\n")
    res.append("\n")

def prep_api_doc(lines):
    res = list()
    in_api_doc = False
    for line in lines:
        if line:
            if line[0] == '#':
                if in_api_doc:
                    end_api_doc(res)
                    in_api_doc = False
            elif line[0] == '>':
                if len(line) > 2:
                    if line[1] == '.':
                        if line.startswith(">.api"):
                            parsed = parse_api_command(line[5:].strip())
                            if in_api_doc:
                                end_api_doc(res)
                            res.append(parsed[3])
                            res.append('<div class="apidoc" markdown="1">')
                            in_api_doc = True
                            continue
                        if line.startswith(">.end_api"):
                            if in_api_doc:
                                end_api_doc(res)
                            in_api_doc = False
        res.append(line)
    return res

print(prep_api_doc([
    "xyz",
    ">.api Map.add(*item*)",
    "Test",
    "### Next"]))