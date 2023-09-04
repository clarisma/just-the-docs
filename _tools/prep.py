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

        with open(src_file, 'r') as fin, open(dest_file, 'w') as fout:
            inside_code_block = False
            code_block = ""

            for line in fin:
                if line.startswith("```"):  # detect start or end of code block
                    inside_code_block = not inside_code_block

                    if not inside_code_block:
                        lang = line.strip("`\n")
                        if lang == "" or lang == "python":
                            # Pass code block through pygments and write to fout
                            highlighted_code = highlight(code_block, lexer, formatter)
                            fout.write(highlighted_code)
                            code_block = ""
                        else:
                            fout.write(f"```{lang}\n{code_block}```\n")
                            code_block = ""
                    continue

                if line.startswith("---"):
                    inside_front_matter = not inside_front_matter
                    if not inside_front_matter:
                        fout.write(f"---\n{inside_front_matter}---\n")
                        front_matter = ""
                        fout.write(f"""
                            {{% comment %}}
                            ==========================================
                           
                               AUTO-GENERATED CONTENT, DON NOT EDIT 

                                   Any changes will be lost 
                                   the next time the
                                   pre-processor runs!

                            ==========================================

                            {{% endcomment %}}
                            """)
                if inside_code_block:
                    code_block += line
                elif inside_front_matter:
                    inside_front_matter += line
                else:
                    fout.write(line)


if __name__ == "__main__":
    transform("_source/python", "python")
