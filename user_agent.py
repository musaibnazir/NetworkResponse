from urllib.request import urlopen , Request
req= Request('http://localhost/blogger')
urlopen(req)
print(req.get_header('User-Agent'))
req.add_header('User-Agent','Mozilla/5.0(X11;Linux X86_64;rv:24.0) Geeko/20190722 Firefox/24.0 Iceweeasel/247.0')
print(req.get_header('User-agent'))
print(req.header_items())
