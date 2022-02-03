from urllib.request import urlopen
response = urlopen('http://127.0.0.1/blogger')
print(response)
print(response.readline())
print(response.url)
print(response.status)
