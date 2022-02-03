from urllib.parse import urlparse, urljoin, parse_qs
result = urlparse('http://localhost/blogger/search.php?q=urlparse & area =default')
print(parse_qs(result))
result1 = urlparse('http://localhost/blogger/search.php?q=urlparse & q = urljoin')
print(parse_qs(result1.query))
