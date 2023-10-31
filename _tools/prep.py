import os
from pathlib import Path
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def transform(srcdir, destdir):
    srcdir = Path(srcdir)
    destdir = Path(destdir)

    lexer = PythonLexer()
    formatter = HtmlFormatter()

    for src_file in srcdir.rglob('*.md'):
        rel_path = src_file.relative_to(srcdir)
        dest_file = destdir / rel_path

        # Ensure the destination directory exists
        dest_file.parent.mkdir(parents=True, exist_ok=True)

        with open(src_file, 'r', encoding='utf-8') as fin, open(dest_file, 'w', encoding='utf-8') as fout:
            inside_code_block = False
            inside_front_matter = False
            code_block = ""
            front_matter = ""

            for line in fin:
                if line.startswith("```"):  # detect start or end of code block
                    inside_code_block = not inside_code_block

                    if not inside_code_block:
                        lang = line.strip("`\n")
                        if lang == "" or lang == "python":
                            # Pass code block through pygments and write to fout
                            highlighted_code = highlight(code_block, lexer, formatter)
                            highlighted_code = highlighted_code.replace(
                                '<pre><span></span>', '<pre class="highlight"><code>')
                            highlighted_code = highlighted_code.replace(
                                '</pre></div>', '</code></pre></div>')
                            fout.write(
                                '<div class="language-python highlighter-rouge">'
                                f'{highlighted_code}</div>')
                            code_block = ""
                        else:
                            fout.write(f"```{lang}\n{code_block}```\n")
                            code_block = ""
                    continue

                if line.startswith("---"):
                    inside_front_matter = not inside_front_matter
                    if not inside_front_matter:
                        fout.write(f"---\n{front_matter}---\n")
                        front_matter = ""
                        fout.write(f"""
    {{% comment %}}

    ==========================================
                           
        AUTO-GENERATED CONTENT, DO NOT EDIT 

            Any changes will be lost 
            the next time the
            pre-processor runs!

    ==========================================

    {{% endcomment %}}

""")
                    continue

                if inside_code_block:
                    code_block += line
                elif inside_front_matter:
                    front_matter += line
                else:
                    fout.write(line)


if __name__ == "__main__":
    transform("_source/python", "python")
