#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     file_test.py
   Description :
   date：          2019-10-24
-------------------------------------------------
"""

# openfile ==>  read/change ==> closefile
# r 只读模式 w 创建模式,若文件已存在，则覆盖旧文件 a 追加模式,新数据会写到文件末尾


f = open(file='test.txt', mode='w')
f.write("Alex ")
f.write("Black")
f.close()

filename = "123.txt"
f = open(file=filename, mode="a")
f.write("测试测试")
f.close()

# 读模式
f = open(file=filename, mode="r")
print(f.readline())
print('----test----')
data = f.read()
print(data)
f.close()









