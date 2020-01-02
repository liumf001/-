'''
信息提取的一般方法
    1， 完整解析信息的标记形式，在提取关键信息
        XML JSON YAML
        需要标记解析器 例如：bs4库的标签树遍历

    2，无视标记形式，直接搜索关键信息
           对信息的文本查找函数即可

    3，融合方法 结合形式解析与搜索方法，提取关键信息
        需要标记解释器及文本查找函数
'''

# 提取所有url链接
from bs4 import BeautifulSoup
import requests
r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
soup.prettify()

for link in soup.find_all('a'):
    print(link.get('href'))
