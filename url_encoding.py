from urllib.parse import quote, urlencode, urlunparse
print(quote('A duck?'))

path = 'http://locahost/blogger'
path_enc = quote(path)
print(path_enc)

query_dict ={'action':'search','term':'Are you sure?'}
query_enc = urlencode(query_dict)
print(query_enc)

netloc = 'localhost/blogger'
a=urlunparse(('http',netloc,path_enc,'',query_enc,'')) #contains 7 arguments
print(a)
