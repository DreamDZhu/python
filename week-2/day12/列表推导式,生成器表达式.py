# 用一行代码构建一个比较复杂有规律的列表。

# 构建一个列表，包含1-10
# 普通写法
ll = []
for i in range(1, 11):
    ll.append(i)

# 列表推导式
ll = [i for i in range(1, 11)]


# 列表推导式分为两种

# 循环模式 [var for var in iterable]
# 筛选模式(满足条件的留下) [var for var in iterable if 条件]


# 循环模式案例:
# 将10以内所有整数的平方写入列表
# 100以内所有的偶数写入列表
# 从python1期到python100期写入列表

ll = [i * i for i in range(1, 10)]
ll = [i for i in range(2, 101, 2)]
ll = [f"python{i}期" for i in range(1, 101)]


# 筛选模式案例:
# 30以内能被3整除的数
ll = [i for i in range(1, 31) if i % 3 == 0]

# 过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母

ll = ['asdasd', 'asda', 'alex', 'ab', 'wusirx']
l2 = [i.upper() for i in ll if len(i) > 3]

names = [["Tom", 'Billy', 'Jefferson', 'Andrew', 'Wesley',
          'Steven', 'Joe'], ['Alice', 'Jill', 'Ana', 'Eva', 'Jennifer']]

# for i in names:
#     for item in i:
#         if item.count('e') == 2:
#             print(item.upper())

# 多层嵌套循环
names2 = [name.upper() for i in names for name in i if name.count('e') == 2]


print(names2)

# 生成器表达式















