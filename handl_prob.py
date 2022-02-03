import urllib.error
from urllib.request import urlopen
print('Error Handling:')
a = input("Enter url: ")
try:
    urlopen(a)
    print('No Error, Success')
except urllib.error.HTTPError as e:
    print('status', e.code)
    print('reason', e.reason)
    print('url', e.url)


print('HTTP Headers ')
b= input("Enter url: ")
response = urlopen(b)
print(response.getheaders())
