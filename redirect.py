from urllib.request import Request, urlopen
req = Request('http://localhost/blogger')
response = urlopen(req)
print(response.url)
print(req.redirect_dict)
