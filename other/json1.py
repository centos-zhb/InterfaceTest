import  json
'''
序列化json格式的字符串
'''
dict1={'name':'leizi','age':24,'address':'北京'}

print (u'未序列化前的数据类型为:',type(dict1))
print (u'未序列化前的数据:',dict1)
#对dict1进行序列化的处理
str1=json.dumps(dict1)
print (u'序列化后的数据类型为:',type(str1))
print (u'序列化后的数据为:',str1)