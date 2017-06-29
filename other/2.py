# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse

url = 'http://www.tuling123.com/openapi/api'
data = {
    "key":"your",
    "info":"你好",
}

data = urllib.parse.urlencode(data).encode('utf-8')
re = urllib.request.Request(url,data)
html = urllib.request.urlopen(re)

print(html.getcode(),html.msg)
print(html.read())