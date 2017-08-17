#!/usr/bin/env/ python3
#-*- coding: utf-8 -*-

class Dict(dict):

    def __init__(self, **kw):#这一行没什么用
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]#self.key调用出来的是self[key]的value, key不是dict的属性
        except KeyError as e:
            raise AttributeError(r"'Dict' 中object has no attribute '%s'(%s)" % (key, e))

    def __setattr__(self, key, value):
        self[key] = value#把设置的属性添加到字典

    
