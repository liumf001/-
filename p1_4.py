'''
IP地址归属地的自动查询
ip138 查询ip和手机号码的归属地
m.ip138.com/ip/asp?ip=ipaddress
'''
import requests
url = 'http://www.ip138.com/iplookup.asp?ip='
url2 = '&action=2'
print(url + '202.204.80.112' + url2)
try:
    r = requests.get(url + '202.204.80.112' + url2)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print('爬取失败')

