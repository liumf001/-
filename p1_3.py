'''
网络图片的爬取和存储
(url是.jpg结尾的， 感觉没啥用)
'''
import requests
import os
root = './test_files/'
url = 'https://gss2.bdstatic.com/-fo3dSag_xI4khGkpoWK1HF6hhy/baike/c0%3Dbaike80%2C5%2C5%2C80%2C26/sign=b785816abd19ebc4d4757ecbe34fa499/b3119313b07eca80ab8c87e89f2397dda1448330.jpg'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print("爬取失败")
