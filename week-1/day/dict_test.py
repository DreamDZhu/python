#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     dict_test.py
   Description :
   date：          2019-10-24
-------------------------------------------------
"""

# {key1:value1,key2:value2}

info = {
    "name": "test",
    "mission": "输出信息",
    "website": "www.baidu.com"
}

name = {
    "alex": [23, "ceo", 60000],
    "black girl": [24, "行政", 4000],
}

name["pq"] = [26, "讲师", 40000]

print(name)

# 删除指定的key-value
name.pop("pq")
# 随机删除1个key
name.popitem()
# 删除指定key 同pop 方法
del name["pq"]
# 清空dict
name.clear()

name["pq"] = [27, "讲师", 30000]


