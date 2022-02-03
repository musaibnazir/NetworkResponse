from urllib.parse import urlparse
from urllib.request import urlopen , Request
req= Request('http://localhost/blogger')
response = urlopen('http://localhost/blogger')
result = urlparse('http://localhost/blogger')
print(result)
print(result.netloc)
print(result.path)
print(urlparse('http://localhost/blog'))
