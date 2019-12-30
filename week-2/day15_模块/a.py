"""
这是一个自定义模块 自定义模块中包括可执行语句（解释器遇到就执行），函数定义
模块中出现的：变量定义，可执行语句（循环体,函数定义等）统称为： 模块的成员
"""

# 可执行语句
# a = 1
# print(a)
b = 1

# 函数定义
def add(*args):
    count = 0
    for i in args:
        count += i
    return count

def f():
    print('hello world')

def a():
    print(123)


if __name__ == '__main__':
    print(a())







