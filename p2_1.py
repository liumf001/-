'''
Beautiful Soup库解析器
bs4 HTML解析器 Beautiful Soup(mk, 'html.parser')
lxml的HTML解析器 BeautifulSoup(mk, 'xml')
lxml的XML解析器 BeautifulSoup(mk, 'xml')
html5lib的解析器 BeautifulSoup(mk, 'html5lib')

Beautiful Soup类的基本元素
Tag 标签
Name 标签的名字
Attributes 标签的属性
NavigableString 标签内的非属性字符串
Comment 标签内字符串的注释部分
'''
from bs4 import BeautifulSoup
import requests
r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
soup.prettify()

print(soup.title)
print(soup.a) #第一个a标签
print(soup.a.parent.name)
print(soup.a.parent.parent.name)
print(soup.a.attrs)
print(soup.a.attrs['href'])

print(soup.a.string)
print(soup.p.string)

