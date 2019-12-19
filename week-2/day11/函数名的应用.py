# def func():
#     print(666)

# 函数名指向的是函数的内存地址。
# 函数名 + () 就可以执行此函数。

# 变量名没有意义，只是一个代号，真正重要的是内存地址

#print(func,type(func))

# 函数名就是变量

# def func():
#     print(666)
# f = func
# f1 = f
# f2 = f1
# f2() # f2 指向 func ，所以f也可以像方法一样执行。

# def func():
#     print("in func")
#
# def func1():
#     print("in func1")
#
# func1 = func
# func1()


# 函数名可以作为容器类数据类型的元素
# def func1():
#     print('in func1')
#
# def func2():
#     print('in func2')
#
# def func3():
#     print('in func3')
#
# l1 = [func1,func2,func3]
#
# for i in l1:
#     i()

# 函数名可以作为函数的参数
# def func1():
#     print('in func')
#
# def func2(func):
#     func()
#
# func2(func1)


# 函数名可以作为函数的返回值
def func():
    print('in func')

def func1(x):
    print('in func1')
    return x

ret = func1(func)
ret()



