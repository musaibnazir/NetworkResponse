from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor
import datetime
cookie_jar = CookieJar()
opener = build_opener(HTTPCookieProcessor(cookie_jar))
opener.open('http://localhost/blogger')
print(len(cookie_jar))
cookies = list(cookie_jar)
#a=datetime.datetime.fromtimestamp(cookies[0].expires)
#print(a)
print(cookies)
print(cookies[0].name)
print(cookies[0].value)
print(cookies[0].domain)
print(cookies[0].path)
print(cookies[0].expires)
print(cookies[0].get_nonstandard_attr('HttpOnly'))
print(cookies[0].secure)
