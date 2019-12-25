# 装饰器：完全遵循开放封闭原则 ，在不改变原函数代码，以及调用方式的前提下，为其增加新的功能。

import time

#版本一
# def index():
#     """有很多操作"""
#     print("欢迎登陆首页")
#     time.sleep(2)
#     print("登陆成功")
#
# def picture():
#     """有很多操作"""
#     print("欢迎登陆图片页")
#     time.sleep(2)
#     print("登陆成功")

#现在写一些代码，测试一下index函数的执行效率。
# start_time = time.time()
# index()
# end_time = time.time()
# #print(start_time)
# print(end_time-start_time)
#
#
# start_time = time.time()
# picture()
# end_time = time.time()
# print(end_time-start_time)

# 该方法，重复代码过多。



# 版本二
# def timer(func):
#     start_time = time.time()
#     func()
#     end_time = time.time()
#     print(f"耗时:",end_time-start_time)
#
# timer(picture)

# 版本二存在的问题是，原函数index源码没有改变，但是给函数添加了一个新的功能 。假设项目中有多处调用Index，那么所有调用Index的地方，都要修改成 timer(index).这样是非常不便的。

# 版本三
# 如何修改，当我们调用index的时候，继会执行index，又会执行timer
# def index():
#     """有很多操作"""
#     print("欢迎登陆首页")
#     time.sleep(2)
#     print("登陆成功")
#
#
# def timer(func):
#     def inner():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(f"耗时:{end_time-start_time}")
#     return inner
#
# ret = timer(index) # ret = inner
# ret() # == inner() == start , func ,end,print


def func():
    print('a')

def func1():
    print('b')

func()
func = 666
func()



