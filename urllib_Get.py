# !/usr/bin/env/Python3
# - * - coding: utf_8 - * -


from urllib import request


with request.urlopen('https://en.wikipedia.org') as f:
    data = f.read()
    # f的属性：f.status:返回状态码；f.reason:返回说明; f.version:返回http版本
    print('Status:', f.status, f.reason, f.version)
    for k, v in f.getheaders():  # 得到HTTP响应的头？？？
        print('%s: %s' % (k, v))
    print('Data: %s' % data.decode('utf-8'))
    # f.read()得到的是Bytes类型, 需要decode, 这个URL用的是JSON