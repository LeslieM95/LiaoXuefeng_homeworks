#!/usr/bin/env/python3
#-*- coding: utf-8 -*-

#在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径
#或在指定目录及指定目录的.........................................., 并打印出绝对路径
import os

def search(des_str, des_dir):
    
    for x in os.listdir(des_dir):

        now_searching_dorf = os.path.join(des_dir, x)#join()自动添加'\\', print出来就成了'\'

        if os.path.isfile(now_searching_dorf) and des_str in x:
            print(now_searching_dorf)#应该打印合并后的路径now_searching_dorf

        elif os.path.isdir(now_searching_dorf):#isdir和isfile的参数应该是now_searching_dorf, 而不是x
            search(des_str, now_searching_dorf)#内部递归函数的参数名now_searching_dorf, 不要与des_dir相同
    
if __name__ == '__main__':
    search('y', '.')  #c:/users/xyeg/desktop
