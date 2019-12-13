# 默认参数的陷阱
# def func(name, sex='男'):
#     print(name)
#     print(sex)
#
#
# func('alex')
# 对于不可变参数，是没有陷阱的
# 陷阱只针对于默认参数是可变的数据类型
def func(name,alist=[]):
    alist.append(name)
    return alist
ret1 = func('alex')
print(ret1,id(ret1))
ret2 = func('taibai')
print(ret2,id(ret2))
# 执行完输出，会发现这个数组中，保存了 alex和taibai。这是为什么？？
# 输出内存地址后会发现， ret1 与 ret2 的内存地址相同，是同一个列表

# 这就是python 机制所导致的，在同一个py文件作用域中，当向函数传递可变参数（列表，字典） 。 这个传递的可变参数，并不存在于全局，也不会存在于局部 。他会将该可变参数，创建在一个第三方特殊空间中 。既不隶属于全局，也不隶属于局部。

# 所以当第二次传递可变参数时，他在第三方特殊空间中，获取到了该可变参数。就不会重复创建 。这个特殊区域的参数，不会随着函数的执行结束而消失。

# 总结：如果你的默认参数指向的是可变的数据类型，那么你无论调用多少次这个默认参数，他都是指向同一个。

# def func(a,list=[]):
#     list.append(a)
#     return list
#
# print(func(10,))
# print(func(20,[]))
# print(func(100,))
# # 结果
# '''
# [10]
# [20]
# [10, 100]
# '''
# # 以上操作的步骤解析：
# ll = []
# ll.append(10)
# l2 = []
# l2.append(20)
# ll.append(100)

# 智商测试题
def func(a,list=[]):
    list.append(a)
    return list

ret1 = func(10,)  # 10, 100
ret2 = func(20,[]) # 20
ret3 = func(100,) # 10, 100

print(ret1)
print(ret2)
print(ret3)










