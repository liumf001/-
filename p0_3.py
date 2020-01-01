'''
requests.request(method, url, **kwargs)
method: 请求方式，
    GET HEAD POST PUT PATCH delete OPTIONS
url: 拟获取页面的url连接
**kwargs: 控制访问参数，共13个
'''
import requests

# params 字典或字节序列，作为参数增加到url中
# kv = {'key1' : 'value1', 'key2' : 'value2'}
# r =  requests.request('GET', 'http://python123.io/ws', params=kv)
# print(r.url)

# data 字典、字节序列或文件对象，作为Request的内容
# kv = {'key1' : 'value1', 'key2' : 'value2'}
# r = requests.request('POST', 'http://python123.io/ws', data=kv)
# body = 'main context'
# r = requests.request('POST', 'http://python123.io/ws', data=body)

# json json格式的数据， 作为Request的内容
# kv = {'key1' : 'value1'}
# r = requests.request('POST', 'http://python123.io/ws', json=kv)

# heads 字典， HTTP定制头
# hd = {'user-agent' : 'Chrome/10'} # 模拟Chrome的第十个版本
# r = requests.request('POST', 'http://python123.io/ws', headers=hd) 

# cookies 字典或CookieJar，Request中的cookie

# auth 元组，支持http认证功能

# files 字典类型 传输文件
# fs = {'file' : open('test_files/data.xls', 'rb')}
# r = requests.request('POST', 'http://python123.io/ws', files=fs)

# timeout 设定超时时间，秒为单位

# proxies 字典类型， 设定访问代理服务器，可以增加登陆认证
# pxs = {'http' : 'http://user:pass@10.10.10.1:1234',  'https' : 'https://10.10.10.1:4321'}
# r = requests.request('GET', 'http://www.baidu.com', proxies=pxs, timeout=5)

# allow_redirects True/Flase 默认为Ture，重定向开关

# stream True/Flase，默认True，获取内容立即下载开关

# verify 默认Ture，认证SSL证书开关

# cert 本地SSL证书路径


'''
requests.get(url, params=None, **kwargs) 最常用
requests.head(url, **kwargs)
requests.post(url, data=None, json=None, **kwargs)
requests.put(url, data=None, **kwargs)
requests.patch(url, data=None, **kwargs)
requests.delete(url, **kwargs)
'''