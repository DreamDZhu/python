#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     文件修改.py
   Description :
   date：          2019-12-18
-------------------------------------------------
"""
import sys

f = open("yesterday", "r", encoding="utf-8")
fnew = open("yesterday3.bak", 'w', encoding="utf-8")

for line in f:
    if "凡人歌" in line:
        line = line.replace('凡人歌', '解放军之歌')
    fnew.write(line)

find_str = sys.argv[1]      # 脚本接收的第一个参数
replace_str = sys.argv[2]   # 脚本接收的第二个参数

def sed(str1, str2, file):
    for line in file:
        if str1 in line:
            line = line.replace(str1, str2)
        file.write(line)


