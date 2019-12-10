s1 = "python测试字符"
# s2 = s1[0]   #字节索引
# print(s2, type(s2))
# s3 = s1[2]
# print(s3)
# s4 = s1[-1]
# print(s4)    #字节索引
# s5 = s1[0:6] # 字符切片，切片顾头不顾尾。表示切 下标 0 - （5-1）的位置
# print(s5)
# s6 = s1[6:]
# print(s6)

# 切片步长
s7 = s1[::2]
print(s7)

# 倒序切片，倒序需要将步长设置为负数才有输出，否则不会输出，也不会报错
s8 = s1[-1:-5:-1]
print(s8)

# 按索引：s1[index]
# 按切片：s1[start_index:end_index+1]
# 按步长: s1[start_index:end_index+1:步长]
# 反向按照切片步长：s1[start_index:end_index后延一位：2]

# 倒序取全部
s2 = s1[::-1]
print(s2)

s = "123a4b5c"

s1 = s[:3] #123
s2 = s[3:6] #a4b
s1 = s[0::2] #1345
s1 = s[1:-1:2] # 2ab
s1 = s[:-2:-1] # c
s1 = s[-3::-2] # ba2


print(s1)
print(s2)