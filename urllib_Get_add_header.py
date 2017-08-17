# !/usr/bin/env/Python3
# - * - coding: utf_8 - * -


from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone\
 OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko)\
  Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:  # 返回适合iPhone的移动版网页
    print('Status: %s %s' % (f.status, f.reason))
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data: %s' % f.read().decode('utf-8'))

# 安卓User-Agent:
# Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255
# Mozilla/5.0 (Linux; Android 4.4.4; HM NOTE 1LTEW Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36 MicroMessenger/6.0.0.54_r849063.501 NetType/WIFI
# 苹果User-Agent:
# Mozilla/5.0 (iPhone; CPU iPhone OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Mobile/9B176 MicroMessenger/4.3.2
# Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25