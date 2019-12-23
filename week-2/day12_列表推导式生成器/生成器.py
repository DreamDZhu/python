# 生成器 python社区，把生成器与迭代器看成是同一种。生成器的本质就是迭代器。
# 唯一的区别：生成器是我们自己用Python 代码构建的数据结构，而迭代器都是由python内置直接提供，或者转换获得

'''
获取生成器的三种方式：
生成器函数
生成器表达式
python内部提供的一些

'''

# 用生成器函数获取生成器


def func():
    # print(111)
    # print(222)
    yield 3  # 当使用yield ，这个函数就变成了一个生成器
    a = 1
    b = 2
    c = a + b
    print(c)
    yield 4


ret = func()

print(next(ret))  # next 取的是yield 3
# print(next(ret))
# 1个next ，对应一个yield元素,每次执行next ,都会执行到下一个yield 的位置，并且会返回yield 后面的值，给这个整体

# ret = func()
# print(ret)

# return yield 区别
'''
return: 函数中只存在一个return 函数，用于结束函数，并且给函数的执行者返回值
yield: 只要函数中有yield ，那么它就是生成器函数。yield 会给执行者返回值。生成器函数中可以存在多个yield ，一个yield对应一个next,yiled不会简单的结束函数


'''

# 生成器函数使用案例 通过生成器函数，5000个包子不会一次性产生，用多少产生多少。节约内存。内存中始终就占用一次产生的内存量
# def gen_func():
#     for i in range(1,5001):
#         yield f'{i}号包子'
#
# ret=gen_func()
# for i in range(100):
#     print(next(ret))
#
# for i in range(100):
#     print(next(ret))

# yield from 3.4版本新特性


def func():
    ll = [1, 2, 3, 4, 5]
    # yield from 对象：相当于把该对象转换为迭代器，并根据next来返回对应的元素，而不是直接返回整个对象
    yield from ll


ret = func()
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))
