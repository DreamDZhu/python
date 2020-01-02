# import src
# 直接引用是加载不到的，因为不在内置的路径下
# import sys
# import os

# 这样引用虽然可以实现，但是会有问题
# work_path = os.path.abspath("..")
# sys.path.append(work_path+r'/core')
# sys.path.append(work_path+r'/conf')
# sys.path.append(work_path+r'/lib')

# 1. 项目中的这些py文件，肯定会互相引用settings , com .虽然我们第一个运行的是main.py ,当运行后，sys.path.append将其他的目录都添加到内存中去，这样其他的模块再互相引用的时候，就不会发生引用不到的问题。但是如果现在有几十个文件夹，难道一个个去添加吗 ？？

# import sys
# import os
#
# # 可以直接导入父目录，通过from 子路径 import 模块 的方式来进行导入
# # 但是我们要动态的获取项目的主目录路径
# sys.path.append(os.path.abspath(".."))
#
# # from core import src
# #
# # print(sys.path)
#
# #import src
# #sys.path
#
# print(__file__) # 动态获取本文件的绝对路径
# print(os.path.dirname(__file__)) # 获取父级的目录
# print(os.path.dirname(os.path.dirname(__file__))) #获取blog的绝对路径

import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from core import src

# 这样就防止其他函数在引用该模块的时候，可以启动
if __name__ == '__main__':
    src.run()