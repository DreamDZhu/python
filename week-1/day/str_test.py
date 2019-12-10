#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     str_test.py
   Description :
   date：          2019-10-24
-------------------------------------------------
"""

word = "this is a test word"
# 首字母大写
print(word.capitalize())

word = "THIS IS A TEST WORD"
# 字符串全转为小写
word = word.casefold()
# 根据补齐符，将字符串补齐到指定的字节长度
word = word.center(50, '-')

print(word)

# 统计该字符出现的次数
word.count('e')
# 从指定下标开始,统计该字符出现的次数
word.count('e', 3)


li = ['alex', 'eric', 'rain']
