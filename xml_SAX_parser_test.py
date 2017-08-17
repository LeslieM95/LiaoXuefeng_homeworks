# !/usr/bin/env/Python3
# - * - coding: utf-8 - * -


from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):

    def start_element(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def end_element(self, name):
        print('sax:end_element: %s' % name)

    def char_data(self, text):
        print('sax:char_data: %s' % text)

    def comment(self, text):
        print('sax:comment: <!-- %s -->' % text)



def parse_xml(data):
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.CommentHandler = handler.comment
    return parser.Parse(data)

if __name__ == '__main__':
    data = r'''<?xml version="1.0"?>
    <!-- w3school.com.cn -->
    <ol>
        <li><a href="/python">Python</a></li>
        <li><a href="/ruby">Ruby</a></li>
    </ol>
    '''
    parse_xml(data)