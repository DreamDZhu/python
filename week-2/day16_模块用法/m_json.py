# Json  = JavaScript Object Notation
# 已经成为一种简单的数据交换格式


"""

序列化 ： 将内存中的数据，转换成字符串，用以保存在文件或通过网络传输，称为：序列化过程。

"""

"""

反序列化：从文件，网络中获取的数据，转换成内存中结构化的数据类型，称为：反序列化过程

"""


import json
ret = json.dumps([1, 2, 3])  # 将指定的对象转换成Json格式的字符串
print(type(ret))
print(ret.split(','))

s = json.dumps((1, 2, 3))  # 元组序列化后，就变成了列表。无法反序列化再成为元组
print(s)

res = json.dumps({'name': 'Andy', 'age': 10})
print(res)

# 将json 结果写到file中
with open('a.txt', mode='at', encoding='utf-8') as f:
    json.dump([1, 2, 3], f)


# t -> text    已文本形式 表示单位
# b -> binary  已二进制形式 表示单位
# a -> append  追加
# w -> write   写入
# r -> read    读取
# + 在原有模式上，再加一个相反的模式 w+ 写读，r+ 读写

# 往文件中写数字，列表，字典等数据，必须先序列化成字符串，再写入，因为磁盘是线性数据结构。
# with open("a.txt",mode='wb') as f:
#     f.write("abc")
