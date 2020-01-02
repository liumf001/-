'''
<>.find_all(name, attrs, recursive, string, **kwargs)
    返回一个列表类型，存储查找的结果
'''
import re
from bs4 import BeautifulSoup
import requests
r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
soup.prettify()

# name  对标签名称的检索字符串
print(soup.find_all('a'))
print(soup.find_all(['a', 'b']))
for tag in soup.find_all(True):
    print(tag.name)

# attrs 对标签属性值的检索字符串，可标注属性检索
print(soup.find_all('p', 'course'))
print(soup.find_all(id='link1'))

# recursive 是否对子孙全部搜索,默认Ture
print(soup.find_all('a', recursive=False))

# string <>...</>中字符串区域的检索字符串
print(soup.find_all(string= 'Basic Python'))
print(soup.find_all(string= re.compile('python')))

'''
简写方法
    <tag>() 等价于 <tag>.find_all()
    soup() 等价于 soup.find_all()

扩展方法
    find()
    find_parents()
    find_parent()
    find_next_siblings()
    find_next_sibling()
    find_previous_siblings()
    find_previous_sibling()
'''
