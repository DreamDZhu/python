s1 = "asdadqeqeqgxcvhrtgh"
ll = [1, 2, 3, 4, 5, 6, 7]


def my_len(s):
    count = 0
    for i in s:
        count += 1
    print(count)


my_len(s1)
my_len(ll)

# 函数：以功能为导向 ，应当最小化的完成一件工作。
# 减少代码的重复性，增强代码的可读性

'''
结构: def 关键字，定义函数
    meet 函数名：与变量设置相同，具有可描述性。
    函数体：缩进，函数中尽量不要出现print

'''

# 函数什么时候执行？ 调用该函数的时候才会执行
# 函数名() 调用函数


def my_func(name, age):
    print("打开")
    print("123")
    return name, age


print(my_func("zhu", 18))


# 函数的返回值 return , 在函数中遇到return ，直接结束函数。不继续执行后续内容
# return 将数据返回给函数的执行者，调用者。

def t_func():
    print("1")
    print("2")
    print("3")
    return '妹子', 123, [22, 33]


# 当函数返回多个元素的时候，会自动创建一个元祖，来保存这些返回值，并返回给函数的执行者
ret = t_func()
print(ret, type(ret))
