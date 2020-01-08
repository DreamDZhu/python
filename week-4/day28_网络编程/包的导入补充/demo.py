#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     demo.py
   Description :
   date：          2020-01-08
-------------------------------------------------
"""
# 导入一个包，等于导入了这个包的init方法
# 并不代表将包下的所有文件都导入进来
# import glance
# import sys

# 要想直接导入某个包（文件夹）下的所有文件

#import glance.api.policy as policy


#print(glance)



# 方式二

#from glance.api import policy
#policy.get()

#from glance.api.policy import get # 这样写是可以来导入的，但是会造成歧义

# 当使用from * import something 时，*处所填的语句。 .这个字符的前面，必须是包！！而不是能具体的模块或者函数

#get()

# 进阶导入方式

# 为什么这样会报错？？  带有相对路径导入的文件，是无法直接运行的！！只能通过其他文件调用
# from . import glance as g
# g.api.policy.get()

import json

# 当你需要写一个功能
# 这个功能不是直接运行的，而是被别人导入之后使用的，这种情况，这个独立功能还形成了文件夹
# 那么文件夹内的所有文件都需要使用相对导入

# 但如果我们自己开发一个项目，这个项目有一些文件是需要直接运行的，这种情况不适合用相对导入
# 适合用绝对导入


