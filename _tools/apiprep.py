import io

def parse_api_dent(s):
    buf = io.StringIO()
    n = s.find('(')
    full_name = (s if n < 0 else s[:n]).strip()
    args = s[n:] if n > 0 else ''
    n = full_name.rfind('.')
    prefix = full_name[:n+1]
    name = full_name[n+1:]
    id = full_name.replace('.', '_')
    buf.write(
        f'<h1 id="{id}">'
        f'<span class="apicontext">{prefix}</span>'
        f'<b>{name}</b>')

    italics = False
    for ch in args:
        if ch=='*':
            italics = not italics
            buf.write('<i>' if italics else '</i>')
        else:
            buf.write(ch)
    
    s = buf.getvalue()
    buf.close()
    return s



print(parse_api_dent("Map.add(*item*)"))