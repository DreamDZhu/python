# 什么是可迭代对象？
'''
由多个元素组成 ？ 这样解释不全对
字母意思: python 中 一切皆对象。一个实实在在存在的值，对象。

可迭代？：更新迭代,一个重复的过程，类似于循环的一个过程。更新迭代，每次都有新的内容。
可以进行循环更新的对象

专业角度：内部含义__iter__方法的对象，叫可迭代对象

可迭代对象:str list tuple dict set range 文件句柄等....

'''

# dir():获取对象的所有方法，并且以字符串的形式表现
#s1 = 'fjdsk1'
# print(dir(s1))

# 所以只要判断__iter__ 字符串是否存在于dir(对象) 中，如果存在，该对象就是一个可迭代对象。如果不在，就不是可迭代对象。
# if "__iter__" in dir(s1):
#     print(123)

# 关于可迭代的对象
# 优点：存储的数据直接能显示，比较直观。
    # 拥有的方法比较多，操作方便
# 缺点：占用内存。
    # 不能直接通过for循环，不能直接取值（索引,key）

# 可迭代对象，是不能直接取值的。之所以可以直接用for来进行操作，是因为自动将其转换为了 ： 迭代器


'''
迭代器的定义 : 可更新迭代的工具。
专业角度： 内部含义'__iter__' 方法，且含义'__next__' 方法的对象。就是迭代器

判断一个对象是否是迭代器: '__iter__' and '__next__' 在不在dir(对象) 中

'''
#
# with open('文件1', encoding='utf-8', mode='w') as f1:
#     print('__iter__' in dir(f1) and '__next__' in dir(f1))

# s = '123123'
# print('__next__' in dir(s)) #输出False
#
# ret = iter(s) # 将可迭代对象转换成迭代器
# print('__next__' in dir(ret))
# print(ret) #<str_iterator object at 0x102875cd0>
#
# print(ret.__next__()) #获取迭代器中的参数
# print(ret.__next__())
# print(ret.__next__())

# 一次__next__() 取一个值，如果__next__() 执行次数大于可迭代对象中的参数个数，就会报错

# l1=[1,2,3,4,5]
# ret = iter(l1)
# print(ret)

# 可迭代对象可以转化成迭代器
# for i in s:
#     print(i)


# 迭代器的优点:
'''
优点: 
1. 节省内存。假设使用 readline 读取一个大文件，那么是生成了一个列表，一次性将所有的信息读取到内存中，会使内存溢出。
而当我们使用的是文件句柄（迭代器）的时候，文件句柄每次只占用1条的内存量。 对于数据量非常大的文件进行处理时，必须使用迭代器进行处理。
2. 惰性机制：next一次，就取一个值，绝不会过多的取值。
    

缺点：
1。速度慢。相比一次性全部取出
2. 不可逆，每次next 就往下取一次。


可迭代对象每次迭代，都会重新开始
而对于迭代器，每次都是向下next

'''

ll = [1,2,3,4,5,6,7,8,9,10]
# ret = iter(ll)
#
# # 迭代器案例
# for i in range(4):
#     print(next(ret))  # 输出1 2 3 4
#
# for i in range(6):
#     print(next(ret))  # 输出5 6 7 8 9 10
#

# 迭代对象案例
count = 0
for i in ll:  # 1 2 3 4
    print(i)
    count +=1
    if count ==4:
        break

count =0
for i in ll: # 1 2 3 4 5 6
    print(i)
    count +=1
    if count ==6:
        break