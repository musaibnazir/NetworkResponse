from urllib.request import urlopen , Request
response = urlopen('http://localhost/blogger')
print(response.getheader('Content-Type'))
format,params = response.getheader('Content-Type').split(';')
charset= params.split('=')[1]
print(params)
print(charset)
