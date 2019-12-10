#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     lst_test.py
   Description :
   date：          2019-10-24
-------------------------------------------------
"""
names = ['alex', 'jack']

# 追加
names.append("rain")
names.append("eva")

# 插入
names.insert(2, "black")

print(names)

# 合并
n2 = ['a','b','c']
names.extend(n2)

print(names)

# 删除最后一个元素并返回删除的值
names.pop()
# 删除指定元素
names.pop(1)
# 清空
#names.clear()

names[0] = "金角大王"
names[-1] = "银角大王"

print(names)

# 查找元素 返回从左开始匹配到的第一个eva的索引
names.index("eva")
# 返回列表中 eva 的个数
names.count("eva")

# 切片
# 切片的特性是顾头不顾尾，即start的元素会被包含，end-1是实际取出来的值
# names[start:end]





