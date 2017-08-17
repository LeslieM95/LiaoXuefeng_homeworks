# !/usr/bin/env/Python
# - * - coding: utf-8 - * -

from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def __init__(self):
        # self.n = 0
        self.weather_data = {}

    def start_element(self, name, attrs):
        # self.n += 1 由此可知，解析每一行XML时，变量初始值都是上一行的值
        if name == 'yweather:location':
            self.weather_data['city'] = attrs['city']
            self.weather_data['country'] = attrs['country']
        elif name == 'yweather:condition':
            self.today_date = attrs['date']
        elif name == 'yweather:forecast':
            if attrs['date'] in self.today_date:
                self.weather_data['today'] = {'text': attrs['text'], 'low': int(attrs['low']), 'high': int(attrs['high'])}
            elif int(attrs['date'][:2]) == int(self.today_date[5:7]) + 1:
                self.weather_data['tomorrow'] = {'text': attrs['text'], 'low': int(attrs['low']), 'high': int(attrs['high'])}

    def end_element(self, name):
        pass  # 用不到

    def char_data(self, text):
        pass  # 用不到


def parse_weather(data):  # 把下面一堆东西全部弄到一个函数里
    handler = DefaultSaxHandler()
    parser = ParserCreate()
    # 函数式编程，函数本身也可以赋值于变量
    parser.StartElementHandler = handler.start_element  # parser.StartElementHandler初始为NoneType
    parser.EndElementHandler = handler.end_element  # parser.EndElementHandler初始为NoneType
    parser.CharacterDataHandler = handler.char_data  # parser.CharacterDataHandler初始为NoneType
    parser.Parse(data)  # parser.Parse()逐行解析，每一行都会调用以上三种方法，但内部原理不太明白
    return handler.weather_data  # 应返回self.weather_data, 这是一个字典, 包含了我parse XML时收集的Weather Data

if __name__ == '__main__':
    # "如何获取网页中的XML"本章最后一节讲, 这里先用硬编码
    data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
    <rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
        <channel>
            <title>Yahoo! Weather - Beijing, CN</title>
            <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
            <yweather:location city="Beijing" region="" country="China"/>
            <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
            <yweather:wind chill="28" direction="180" speed="14.48" />
            <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
            <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
            <item>
                <geo:lat>39.91</geo:lat>
                <geo:long>116.39</geo:long>
                <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
                <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
                <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
                <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
                <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
                <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
                <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
            </item>
        </channel>'''

    weather = parse_weather(data)
    assert weather['city'] == 'Beijing', weather['city']
    assert weather['country'] == 'China', weather['country']
    assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
    assert weather['today']['low'] == 20, weather['today']['low']
    assert weather['today']['high'] == 33, weather['today']['high']
    assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
    assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
    assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
    print('Weather: %s' % weather)


