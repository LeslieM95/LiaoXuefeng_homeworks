# !/usr/bin/env/Python3
# - * - coding: utf-8 - * -


from html.parser import HTMLParser
from html.entities import name2codepoint  # 为什么这行没用？


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):  # 相当于xml中的start_element
        print('starttag: <%s>, attrs: %s' % (tag, attrs))

    def handle_endtag(self, tag):  # 相当于xml中的end_element
        print('endtag: </%s>' % tag)

    def handle_startendtag(self, tag, attrs):  # 若没有此方法, <br/>会被处理成<br><br/>
        print('startendtag: <%s/>, attrs: %s' % (tag, attrs))

    def handle_data(self, text):  # 相当于xml中的char_data
        print('data: %s' % text)

    def handle_comment(self, text):
        print('<!--%s-->' % text)

    def handle_entityref(self, name):  # handle_entityref和handle_charref貌似没用
        c = name2codepoint[name]
        print('&%s;' % c)

    def handle_charref(self, name):
        print('charref: &#%s;' % name)


def parse_html(data):
    parser = MyHTMLParser()
    return parser.feed(data)

if __name__ == '__main__':
    data = r'''<html><head><time datetime="2017-03-10T00:00:00+00:00">10 March &ndash; 13 March <span class="say-no-more"> 2017</span></time>
<h3 class="event-title" type='Leslie'/></head><body><!-- test html parser --><p>Some <a href="#">html</a> HTML&#160;tutorial...<br/>END</p>
</body></html>'''                     # &nbsp;或&#160; 表示空格

    parse_html(data)