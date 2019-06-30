import urllib.request
import urllib.parse
import json

content = input('请输入要翻译的词语：')

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}

data['i']=content
data['doctype']='json'
data['keyfrom']='fanyi.web'
data['typoResult']='true'
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='1520416292076'
data['sign']='41fe7ea28425a0a4ceb88ab4c8609d13'
data['version']='2.1'

data['action']='FY_BY_CLICKBUTTION'
data['typoResult']='false'

data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')

ta = json.loads(html)
print(html)
print(ta['translateResult'][0][0]['tgt'])
