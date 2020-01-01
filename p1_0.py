'''
京东商品网页的爬取
'''
import requests
try:
    r = requests.get('https://item.jd.com/100005185599.html')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print('爬取失败')
