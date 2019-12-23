# int 将一个字符串或数字类型转换为整型
print(int(3.6))

# float 将整型和字符串转换成浮点型
print(float(3))

# bin 将十进制转换成二进制并返回
print(bin(100))

# oct 将十进制转换成八进制并返回
print(oct(10))

# hex 将十进制转换成十六进制字符串并返回
print(hex(100))

# divmod 获取两个数的除结果和余，返回一个元祖
print(divmod(10, 3))

# round 保留浮点数小数位数 接收一个数和要保留的位数，返回结果
print(round(3.1415, 2))

# pow 求X**Y次幂
print(pow(2, 3))
# 表示2的3次幂，且对3取余
print(pow(2, 3, 3))

# bytes ***
s1 = '太白'
b = s1.encode('utf-8')
b = bytes(s1, encoding='utf-8')  # 方法相同，都是编码转换

print(b)

# ord 输入字符，输出该字符在编码表中的位置，会自动找不同的编码表
print(ord('a'))  # ascll
print(ord('中'))  # unicode

# 输入位置，转换成对应的字符输出
print(chr(20013))

# repr 返回一个对象的string的所有字符（包括引号,转义字符等）
s1 = '太白\n'
print(repr(s1))

# all 可迭代对象中，全都是true 才是true  / and
l1 = [1, 2, '太白', True, False]
print(all(l1))

# any 可迭代对象中，有一个true ，就是true / or
print(any(l1))

# print
print(1, 2, 3, 4, sep='&')  # 指定数据分隔符
print(1, end='@')  # 更改终止符


# dict 创建字典的几种方式
dic = dict([(1, 'one'), (2, 'two'), (3, 'three')])
dic = dict(one=1, two=2)

# abs 绝对值
print(abs(-10))


# sum 求和
ll = [i for i in range(10) if i > 5]
print(sum(ll))
sum(ll, 100)  # 表示最终结果+100


# list.reverse 列表翻转 ,直接将原列表翻转
l1 = [i for i in range(10)]
l1.reverse()
print(l1)  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# reversed 不改变原列表，而是创建一个翻转的迭代器
l2 = [i for i in range(10)]
obj = reversed(l2)
print(l2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(obj)  # <list_reverseiterator object at 0x1047b5cd0>
print(list(obj))  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# zip 拉链方法 ，另类生成器，结合多个可迭代对象，取最短容量
l1 = [1, 2, 3, 4, 5]
tu1 = ('a', 'b', 'c')
s1 = '&^%$'

obj = zip(l1, tu1, s1)
print(obj)
for i in obj:
    print(i)
''' 结果
<zip object at 0x10234e1e0>
(1, 'a', '&')
(2, 'b', '^')
(3, 'c', '%')
'''

####################################

#min max
ll = [33,2,1,54,7,-1,-9]
print(min(ll),max(ll))

















