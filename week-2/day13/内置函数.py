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
print(divmod(10,3))

# round 保留浮点数小数位数 接收一个数和要保留的位数，返回结果
print(round(3.1415,2))

# pow 求X**Y次幂
print(pow(2,3))
# 表示2的3次幂，且对3取余
print(pow(2,3,3))

# bytes ***
s1 = '太白'
b = s1.encode('utf-8')
b = bytes(s1,encoding='utf-8')  #方法相同，都是编码转换

print(b)

# ord 输入字符，输出该字符在编码表中的位置，会自动找不同的编码表
print(ord('a')) # ascll
print(ord('中')) # unicode

# 输入位置，转换成对应的字符输出
print(chr(20013))

# repr 返回一个对象的string的所有字符（包括引号,转义字符等）
s1 = '太白\n'
print(repr(s1))

# all 可迭代对象中，全都是true 才是true  / and
l1 = [1,2,'太白',True,False]
print(all(l1))

# any 可迭代对象中，有一个true ，就是true / or
print(any(l1))



