# 装饰器：完全遵循开放封闭原则 ，在不改变原函数代码，以及调用方式的前提下，为其增加新的功能。
# 装饰器就是一个函数。装饰器的本质就是闭包

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
# index = timer(index) # ret = inner
# index() # == inner() == start , func ,end,print


# 版本四
# 但是上面的版本，还是非常反人类，我们需要在每一个调用index的地方，都加上 index = timer(index) 这句函数

# python 做了一个优化，提出了一个语法糖的概念

# def timer(func):
#     def inner():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(f"耗时:{end_time-start_time}")
#     return inner
#
# def p_hello(f):
#     def inner():
#         f()
#         print("测试装饰器")
#     return inner

# @timer # 这就是语法糖，这就等同于 index = timer(index)
# #@p_hello
# def index():
#     """有很多操作"""
#     print("欢迎登陆首页")
#     time.sleep(2)
#     print("登陆成功")


#index() # == inner() == start , func ,end,print

# # 版本六：被装饰函数带返回值
# def timer(func):
#     # func = index
#     def inner():
#         start_time = time.time()
#         #print(f'真正获取666的人:{func()}')
#         f = func()
#         end_time = time.time()
#         print(f"耗时:{end_time-start_time}")
#         return f
#     return inner
#
# @timer
# def index():
#     """有很多操作"""
#     print("欢迎登陆首页")
#     time.sleep(0.6)
#     return 666
#
# ret = index()
# print(ret) # 操作到这里会发现，return 并没有返回666，而是返回了None，这是为什么 ？
#
# # 当index 装饰后，index() 已经成为了inner , index() = inner(),那么print 打印的，就是inner的返回值，但是inner没有返回值，所以是返回了 None
# # index 返回的666，是让index的执行者所捕获， 也就是func
# # 如果想要，ret 获取到666，那么返回的666 ,应该写在inner中。


# 版本七 被装饰函数带参数
# 当被装饰函数带参数时，永远要明确。真实执行的方法，已经变成了 inner() ,所以接收参数的函数，应该是inner,而不再是index !!
#

def timer(func):
    # func = index
    def inner(*args,**kwargs):
        start_time = time.time()
        f = func(*args,**kwargs)
        end_time = time.time()
    return inner

@timer
def index():
    time.sleep(0.6)
    #print(f'欢迎{a}登录博客园首页')
    return True

#index('太白')

# 增加装饰器可扩展性 ,装饰器中的函数，可以用*args,**kwargs 来接收所有的参数。以获得足够的扩展性

@timer
def dariy(name,age):
    time.sleep(0.5)
    print(f'欢迎{age}的{name}使用日志系统')


ret = dariy("ddz",18)








