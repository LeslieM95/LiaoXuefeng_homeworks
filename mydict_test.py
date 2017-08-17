#!/usr/bin/env/python3
#-*- coding: utf-8 -*-

from unittest import TestCase, main

from myDict import Dict

class TestDict(TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown???')
    
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['you'] = 'Isabel'
        self.assertEqual(d.you, 'Isabel')
        
    def test_attr(self):
        d = Dict()
        d.you = 'Isabel'
        self.assertEqual(d['you'], 'Isabel')
        self.assertTrue('you' in d)

    def test_keyerror(self):
        d = Dict(a=1)
        with self.assertRaises(KeyError):#若d['key']不存在，测试是否会抛出KeyError
            d['a']#如果d['a'], 会报错AssertionError: KeyError not raised

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            val = d.empty#写成"val = d.empty"和"d.empty"的结果是一样的

if __name__ == '__main__':
    main()
