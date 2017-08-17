# !/usr/bin/env/Python3
# - * - coding: utf-8 - * -


# 思路源于http://blog.csdn.net/nwpulei/article/details/7272832


from html.parser import HTMLParser
from urllib import request


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.li = False  # 用标签的True/False表示开始/关闭
        self.h3 = False
        self.a = False
        self.p = False
        self.time = False
        self.span1 = False
        self.span2 = False
        self.event_dict = {}
        self.count = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'li':
            self.li = True
        elif tag == 'h3':
            for k, v in attrs:  # 有些attrs可能是空的， 故直接用if attrs[0][1]=='event-title'会报错
                if k == 'class' and v == 'event-title':
                    self.h3 = True
        elif tag == 'a':
            self.a = True
        elif tag == 'p':
            self.p = True
        elif tag == 'time':
            self.time = True
        elif tag == 'span':
            for k, v in attrs:
                if k == 'class' and v == 'say-no-more':
                    self.span1 = True
                elif k == 'class' and v == 'event-location':
                    self.span2 = True

    def handle_data(self, data):
        if self.li:
            if self.h3 == True and self.a == True:
                self.count += 1  # 用self.count作为self.IDdict的key，表示会议的次数
                self.event_dict[self.count] = {}
                self.event_dict[self.count]['name'] = data
            elif self.p:
                if self.time:
                    if not self.span1:
                        self.event_dict[self.count]['time'] = data
                    else:
                        self.event_dict[self.count]['time'] += (',' + data)
                else:
                    if self.span2:
                        self.event_dict[self.count]['site'] = data

    def handle_endtag(self, tag):
        if tag == 'a':
            self.a = False
        elif tag == 'h3':
            self.h3 = False
        elif tag == 'span':
            self.span1 = False
            self.span2 = False
        elif tag == 'time':
            self.time = False
        elif tag == 'p':
            self.p = False
        elif tag == 'li':
            self.li = False


def parse_python_event(html_data):
    global parser
    parser.feed(html_data)  # feed()接受的html_data为str类型，bytes类型需要decode
    return parser.event_dict


if __name__ == '__main__':
    with request.urlopen('https://www.python.org/events/python-events/') as f:
        html_data = f.read()  # 得到的是bytes类型，需要decode
        # 也可以f.readlines()
        '''n = 0
        for line in f.readlines():
            n += 1
            print(n, line.decode('utf-8'))'''

    parser = MyHTMLParser()
    event = parse_python_event(html_data.decode('utf-8'))
    print('Conference: %s' % event)
    for i in range(1, parser.count+1):  # 变量parser是global的
        print('event %s:' % i, event[i]['name'], '\n', event[i]['time'], '\t', event[i]['site'])
        print('-' * 30)