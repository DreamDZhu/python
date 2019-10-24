#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     buycar.py
   Description :
   date：          2019-10-24
-------------------------------------------------
"""

names = ["金角大王", "黑姑娘", "rain", "eva", "狗蛋", "银角大王", "eva", "鸡头"]

num = names.index("eva")
num += names.index("eva", num, -1)
print(num)
print(names[::-1])
print(names[1::2])

names[num] = "EVA"
print(names)

goods = [
{"name": "电脑", "price": 1999},
{"name": "鼠标", "price": 10},
{"name": "游艇", "price": 20},
{"name": "美女", "price": 998}, ]

wage = input("input your wage: ")
if wage.isdigit():
    while True:
        index = 0
        for item in goods:
            print(f"编号:{index+1} 商品名:{item['name']} 价格:{item['price']}")
            index += 1
        ipt_index = input("请输入要购买的物品编号:")
        if ipt_index.isdigit():
            ipt_index = int(ipt_index)
            if 0 < ipt_index <= index+1:
                print(goods[ipt_index-1]['price'])
            else:
                print("input error !!!")
        else:
            print("input error !!!")

else:
    print("please input number !!!")