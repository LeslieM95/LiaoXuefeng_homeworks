#!/usr/bin/env/python3
# -*- coding: utf-8 -*-

import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    m = re.match(r'^UTC([\+\-]0?[0-9]|1[0-2])\:00$', tz_str)

    if m is not None:
        try:
            dt = datetime.strptime(dt_str, '%Y-%m-%d  %H:%M:%S')  # strptime()自带验证d_str, 无需再用re验证
            tz = timezone(timedelta(hours=int(m.group(1))))
            dt_utc_x = dt.replace(tzinfo=tz)
            return dt_utc_x.timestamp()  # 带UTC的datetime也可以直接转换为timestamp
        except BaseException as e:  # 可以 捕捉到日期和时间的格式错误 和 如2-31这样的非法日期错误
            print('ValueError: %s!!!'% e)
    else:
        raise ValueError('Wrong Format UTC!')


if __name__ == '__main__':
    t1 = to_timestamp('2015-6-1  01:10:30', 'UTC+00:00')
    assert t1 == 1433121030.0, t1
    print(t1)

    t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-9:00')
    assert t2 == 1433121030.0, t2
    print(t2)

    print('Pass')