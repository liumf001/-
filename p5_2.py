'''
Re库的Match对象
常用属性
    .string 待匹配的文本
    .re 匹配时使用的pattern对象（正则表达式）
    .pos 正则表达式搜索文本的其实位置
    .endpos 搜索文本的结束位置
常用方法
    .group(0) 获得匹配后的字符串
    .start() 匹配字符串在原始字符串的开始位置
    .end() 结束位置
    .span() 返回(.start(), .end())
'''

import re
m = re.search(r'[1-9]\d{5}', 'BIT 100081 TSU 100084')
print(m.string)
print(m.re)
print(m.pos)
print(m.endpos)
print(m.group(0))
print(m.start())
print(m.span())