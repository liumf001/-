import requests
r = requests.get("http://www.baidu.com")
print(r.status_code) # 200 访问成功 404或其他表示失败
r.encoding = 'utf-8'
print(r.headers) # get请求头部信息
print(r.text) #text表示响应内容的字符串形式，content是二进制形式
