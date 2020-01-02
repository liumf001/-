'''
中国大学排名定向爬虫

三个函数
getHTMLText()
fillUnivList()
printUnivList()
'''
import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def fillUnivList(uList, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            uList.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(uList, num):
    print("{:<15}\t{:<15}\t{:<15}".format("排名", "学校", "总分"))
    for i in range(num):
        u = uList[i]
        print("{:<15}\t{:<15}\t{:<15}".format(u[0], u[1], u[2]))
    print('Suc' + str(num))


def main():
    uInfo = []
    url = 'http://zuihaodaxue.cn/Greater_China_Ranking2019_0.html'
    html = getHTMLText(url)
    fillUnivList(uInfo, html)
    printUnivList(uInfo, 50)


if __name__ == '__main__':
    main()