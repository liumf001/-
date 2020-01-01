'''
搜索引擎关键词提交接口
baidu
    baidu.com/s?wd=keyword
360
    so.com/s?q=keyword
'''
import requests
keyWord = input("输入关键词")
try:
    kv = {'wd' : keyWord}
    r = requests.get('http://www.baidu.com/s', params=kv)
    print("url:")
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')