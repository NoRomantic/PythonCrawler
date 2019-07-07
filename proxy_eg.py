import urllib.request

url = 'http://www.whatismyip.com.tw'

proxy_support = urllib.request.ProxyHandler({'http': '114.225.223.144:9999'})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)

