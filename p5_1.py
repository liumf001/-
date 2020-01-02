'''
Re库的主要功能函数

re.search()
    在一个字符串中搜索匹配正则表达式的第一个位置，返回match对象     
re.match()
    从一个字符串的开始位置其匹配正则表达式，返回match对象
re.findall()
    搜索字符串，以列表类型返回全部能匹配的子串
re.split()
    将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
re.finditer()
    搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
re.sub()
    在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
'''
import re
'''
re.search(pattern, string, flags=0)
    pattern 正则表达式的字符串或原声字符串表示
    string 带匹配字符串
    flags 正则表达式使用时的控制标记
        re.I re.IGNORECASE 忽略大小写
        re.M re.MULTILINE ^操作符能够将给定字符串的每行当作匹配开始
        re.S re.DOTALL .操作符能匹配所有字符，默认匹配除换行外的所有字符
'''
match = re.search(r'[1-9]\d{5}', 'BIT 100081')
if match:
    print(match.group(0))

'''
re.match(pattern, string, flags=0)
'''
match = re.match(r'[1-9]\d{5}', 'BIT 100081')
if match == None:
    print("no match")
else:
    print(match.group(0))

'''
re.findall(pattern, string, flags=0)
'''
ls = re.findall(r'[1-9]\d{5}', 'BIT 100081\n CL262400')
print(ls)

'''
re.slpit(pattern, string, maxsplit=0. flags=0)
maxsplit 最大分割数，剩余部分作为最有一个元素输出
'''
print(re.split(r'[1-9]\d{5}', 'BIT 100081\nCL262400AAA'))
print(re.split(r'[1-9]\d{5}', 'BIT 100081\nCL262400AAA', maxsplit=1))

'''
re.finditer(pattern, string, flags=0)
'''
for m in re.finditer(r'[1-9]\d{5}', 'BIT 100081\nCL262400AAA'):
    if m:
        print(m.group(0))

'''
re.sub(pattern, repl, string, count=0, flags=0)
repl 替换匹配字符串的字符串
count 匹配的最大替换次数
'''
print(re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT 100081\nCL262400AAA'))


'''
面向对象的用法：编译后多次操作
regex = re.compile(pattern, flags=0)
'''
pat = re.compile(r'[1-9]\d{5}')
res = pat.search("BIT 100081")
print(res.group(0))