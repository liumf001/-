'''
标签树的三种遍历方式
    下行遍历
        .contents 子节点的列表
        .children 子节点的迭代类型
        .descendants 子孙节点的迭代类型
'''
from bs4 import BeautifulSoup
import requests
r = requests.get('http://python123.io/ws/demo.html')
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
soup.prettify()

print(soup.body.contents)
print(len(soup.body.contents))
print(soup.body.contents[2])

for child in soup.body.children:
    print("儿子：" + str(child))

for child in soup.body.descendants:
    print("后代：" + str(child))

'''
上行遍历
    .parent 节点的父亲标签
    .parents 节点先辈标签的迭代类型
'''
print(soup.title.parent)
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

'''
平行遍历
    .next_sibling
    .previous_sibling
    .next_siblings
    .privious_siblings
'''
print(soup.a.next_sibling)
print(soup.a.privious_sibling)
for sibling in soup.a.next_siblings:
    print(sibling)