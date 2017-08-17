# !/usr/bin/env/Python3
# - * - coding: utf_8 - * -


from urllib.request import urlopen
from bs4 import BeautifulSoup

# 廖老师要求的是获取XML，不懂怎么获取XML
# 这里我用beautifulsoup处理HTML
def fetch_html(url):
    with urlopen(url) as f:
        data = f.read()
    soup=BeautifulSoup(data, 'lxml')  # data无须decode
    count=0
    for i in soup.select('div[class="D(ib) Va(m) W(1/4)"]'):
        count=count+1

    for j in range(count):
        print('星期:',soup.select('div[class="D(ib) Va(m) W(1/4)"]')[j].get_text())  # get_text()方法获取元素的内容，返回一个字符串
        print('天气:',soup.select('span[class="D(ib) Va(m) W(1/4) Ta(c)"] > img')[j]['alt'])
        a=soup.select('span[class="D(ib) Va(m) W(1/4) Ta(end)"]')[j].get_text()
        print('温度:','high:%sF, low:%sF'%(a[:3],a[3:]))
        print('降水量: %s' % soup.select('span[class="D(ib) Mstart(1/3)"]')[j].get_text())
        print('-'*30)


if __name__ == '__main__':
    fetch_html('https://www.yahoo.com/news/weather/united-states/new-york/new-york-2459115')
    # 注意！！！必须联网了，才能向服务器发送请求，有时会需要翻墙