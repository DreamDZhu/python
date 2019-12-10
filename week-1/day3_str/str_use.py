s = 'qwerty谢谢JWSqS'
# 字符串常用操作方法
# upper lower

# 将字符串英文全部转换为大写
s = s.upper()
# 将字符串英文全部转换为小写
s = s.lower()

# 判断是否已指定字符开头
print(s.startswith('q'))
# 步长 表示 索引 3 - （6-1） 是否已r开头
print(s.startswith('r', 3, 6))

# 判断是否已指定字符结尾
print(s.endswith('S'))

msg = 'this is a test msg , this is a old msg'
# 字符串替换，不写值表示匹配到的全部替换
msg = msg.replace('this', 'that', 1)
print(msg)

msg1 = ' strip asd  qweqxxx      '
# 去除字符串中指定字符，默认为去除空格 ，但是不会去除字符串中间的空格
msg1 = msg1.strip()
print(msg1)

msg1 = msg1.strip('strx')
print(msg1)

# split 根据指定字符，分割字符串 默认按照空格分割
msg2 = msg.split(',')
print(msg2)

sa = "123,我,kk,abc,3"

# 表示只分割前两项
sa = sa.split(',', 2)
print(sa)

# join 将每一个字符由指定的分割符组合在一起
s1 = "alex ABer"
s2 = '+'.join(s1)
print(s2) #a+l+e+x+ +A+B+e+r

ll = ['A', 'B', 'c']
s3 = ':'.join(ll) #A:B:c 限制，元素必须都是字符串
print(s3)

# count 记录字符出现的次数
s8 = 'asdsadfdgdfdsasfdgdfg'
print(s8.count('a'))

# format 格式化输出
msg = '名称:{}'
print(msg.format('大壮'))
msg = '力量:{},敏捷:{},智力:{}'
print(msg.format('100', '200', '300'))

msg = '力量:{0},敏捷:{1},智力:{0}'
print(msg.format('100', '200'))

# is 判断字符串组成
name = "taibai123"
name.isalnum() # 字母或数字
name.isalpha() # 字母
name.isdecimal() # 由十进制数字组成

# username = input("用户名:")
# password = input("密码:")
#
# code = 'QweA'
# your_code = input("code:")
#
# if code.upper() == your_code.upper():
#     if username == 'a' and password == '123':
#         print("success")
#     else:
#         print("faild")
# else:
#     print("faild")
