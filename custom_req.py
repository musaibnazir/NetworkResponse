from urllib.request import Request, urlopen
a = print("Customising Requests")
a = input("Enter url: ")
req = Request(a)
req.add_header('Accept-Language','Sr')
response = urlopen(req)
print(response.readline())
print(req.header_items())




header=  {'Accept-Language':'Sr'}
req = Request(a)
print(req.header_items())
