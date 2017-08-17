#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import OrderedDict


class FIFOOrderedDict(OrderedDict):
    def __init__(self, capacity, *args, **kw):
        self._capacity = capacity  # 把"self._capacity = capacity"放在"super().__init__(*args, **kw)"之前就对了
        super().__init__(*args, **kw)  # 传入*args或**kw 内部会先逐个(k,v)依次调用__setitem__()
        # self._capacity = capacity    # 而，这时"self._capacity = capacity" 还未执行，因此会报错
                                       # AttributeError: 'FIFOOrderedDict' object has no attribute '_capacity'

    def __setitem__(self, key, value):
        containkey = 1 if key in self else 0
        # 等价于: if key in self:
        #             contaonkey = 1
        #         else:
        #             containkey = 0
        if len(self) - containkey == self._capacity:  # ">="和"=="都对，因为(k,v)是逐个依次调用__setitem__()的，len(self)每次+1
            # 调用父类OrderedDict的popitem()方法, self.popitem(last=False)或者super().popitem(last=False)
            first = super().popitem(last=False)  
            print('remove:', first)  # 打印tuple不能用%s, 因为%s只能表示tuple中的一个元素

        if containkey:
            del self[key]  # 删除原k-v，然后替换
            print('replace:', (key, value))
        else:
            print('set:', (key, value))

        super().__setitem__(key, value)  # 子类不能直接调用父类的private method
                                         # self.__setitem__()会形成递归调用，栈溢出
        print(self)                      


if __name__ == '__main__':
    m_od = FIFOOrderedDict(2, [('a', 1), ('b', 2), ('c', 3)])
    # 为什么不能这样传入呢[('a', 1), ('b', 2), ('c', 3)]或者(a=1, b=2, c=3)
    # 但是, 把继承的父类OrderedDict改成dict就可以了
    # 我明了, 因为dict传入*args或**kw 内部不会调用__setitem__
    # 而OrderedDict传入*args或**kw 内部会先逐个(k,v)依次调用__setitem__()
    print(m_od)
    #m_od['a'] = 1
    #m_od['b'] = 2
    m_od['c'] = 4
