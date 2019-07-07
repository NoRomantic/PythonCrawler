import urllib.request
import urllib.parse
import json
import time

while True:
    content = input('请输入要翻译的词语(输入"q!"退出程序)：')
    if content == 'q!':
        break
    
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    '''
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    '''

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

    req = urllib.request.Request(url, data)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')

    response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')

    ta = json.loads(html)
    # print(html)
    print(ta['translateResult'][0][0]['tgt'])

    time.sleep(5)


