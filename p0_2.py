import requests

# head()
# r = requests.head('http://httpbin.org/get')
# print(r.headers)
# print(r.text) # 空的

# post() put()
payload = {'key1' : 'value1', 'key2' : 'value2'}
r =  requests.post('http://httpbin.org/post', data=payload) # 字典自动编码为form（表单） 字符串会编码为data
print(r.text)
r2 = requests.put('http://httpbin.org/put', data = payload) # 类似post，但将原有数据覆盖掉
print(r2.text)