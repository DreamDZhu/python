"""
pickle : 支持python中所有数据类型，转换成字节串

序列化过程： 数据结构 ==> bytes
反序列化过程 : bytes ==> 数据结构

"""

import pickle

# bys = pickle.dumps((1,2,3))
# print(bys) # b'\x80\x03K\x01K\x02K\x03\x87q\x00.'
# print(type(bys)) # <class 'bytes'>
#
# res = pickle.loads(bys)
# print(res,type(res)) # (1, 2, 3) <class 'tuple'>


# 把pickle 序列化内容写入文件中

# with open(file='b.txt',mode='ab') as f:
#     pickle.dump([1,2,3],f)

# 从文件中读取pickle数据，反序列化到内存中
# with open(file='b.txt',mode='rb') as f:
#     res = pickle.load(f)
#     print(res)

# pickle 支持多次写，多次读

# 多次写入到同一个文件中
# with open(file='b.txt', mode='wb') as f:
#     pickle.dump([1, 2, 3], f)
#     pickle.dump([1, 2, 3], f)
#     pickle.dump([1, 2, 3], f)
#     pickle.dump([1, 2, 3], f)

# with open(file='b.txt', mode='rb') as f:
#     res = pickle.load(f)
#     print(res)
with open(file='b.txt',mode='rb') as f:
    for x in range(4):
        res = pickle.load(f)
        print(res)

# 但是不建议多次读，因为文件是二进制方式，无法看出其中究竟有多个pickle数据，多次容易出错
# pickle 常用场景 ：和Json 一样，一次性写入，一次性读取


"""
区别
json : 
1.不是所有的数据类型都可以序列化，即使序列化，也可能丢失数据类型
2.不能多次对同一个文件序列化，但是可以通过文件本身写入的方式，一行行进行写入
3. json 是 object <==> string
4. json 数据可以跨语言读取


pickle :
1. 可以序列化所有数据类型，并反序列的时候得到正确的数据类型
2. pickle 是 object <==> bytes
3 pickle 数据通常只允许python进行读取

"""


