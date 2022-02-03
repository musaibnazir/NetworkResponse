from urllib.request import Request, urlopen
import gzip
a = print("Content Compression")
a = input("Enter url: ")
req = Request(a)
req.add_header('Accept-Encoding','gzip')
response= urlopen(req)
content = gzip.decompress(response.read())
content.splitlines()[:5]
req.add_header('Accept-Encoding','identity')
response= urlopen(req)
print(response.getheader('Content-Encoding'))
