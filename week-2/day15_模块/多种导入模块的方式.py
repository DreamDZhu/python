# import xxx 导入一个模块中的所有成员
# import aaa,bbb 一次性导入多个模块的成员 （不推荐）
# from xxx import a : 从某个模块中导入指定的成员
# from xxx import a,b,c: 从某个模块中导入多个成员
# from xxx import *:从模块中导入所有成员


# import xx 和 from xx import * 区别

'''
使用import xxx 方式，在使用模块中的方法时，必须使用该模块名作为前缀 例如
import time
time.sleep(1)

from xx import * ,不需要使用模块名作为前缀，可以直接使用成员名 (这种方法容易产生命名冲突，这样就不知道成员与变量，究竟属于哪一个模块)
from time import *
sleep(1)


'''

# import os
# import sys
# sys.path.append(os.path.dirname(__file__)+'/ceshi')
#
# from b import *
#
# test()
# print(age)


# 解决模块命名冲突 ： 使用别名解决冲突







