# !/usr/bin/env/Python3
# - * - coding: utf_8 - * -

# 模拟微博登录, 为什么不成功呢？？？
from urllib import request, parse


print('Login to weibo.cn......')
phonenum = input('Phonenumber: ')
password = input('Password: ')
login_data = parse.urlencode([
    ('username', phonenum),  # 用元组列表或字典都可以
    ('password', password),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
req.add_header('Referer', 'http://weibo.com/#_loginLayer_1488550589291')


with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status: %s %s' % (f.status, f.reason))
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data: %s' % f.read().decode('gbk'))