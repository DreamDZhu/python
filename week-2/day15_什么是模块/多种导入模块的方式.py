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

import os
import sys
sys.path.append(os.path.dirname(__file__)+'/ceshi')

from b import *



# 解决模块命名冲突 ： 使用别名解决冲突
from time import sleep as s  # 导入成员起别名
import os as o  # 给模块起别名

print('123')
s(2)
print('456')


# from xxx import * 控制成员被导入
# 默认情况下，所有成员都会被导入

# __all__ 是一个列表，用于表示本模块可以被外界使用的成员
# __all__ = ['age','age2']
# 验证__all__所控制的成员
print(age)
print(age2)
print(age3)

# 使用以下方式，可以绕过__all__的限制
# import b as bb
'''
print(b.age)
print(b.age2)
print(b.age3)
'''











