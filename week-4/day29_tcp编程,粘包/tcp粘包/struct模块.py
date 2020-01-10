import struct

num1 = 2147483646
num2 = 138
num3 = 8

# struct.pack用于将Python的值根据格式符，转换为字符串（因为Python中没有字节(Byte)类型，可以把这里的字符串理解为字节流，或字节数组）。其函数原型为：struct.pack(fmt, v1, v2, ...)，参数fmt是格式字符串，关于格式字符串的相关信息在下面有所介绍。v1, v2, ...表示要转换的python值。

ret1 = struct.pack('i', num1)

print(ret1)

ret2 = struct.pack('i',num2)

print(ret2)

ret3 = struct.pack('i',num3)

print(ret3)

res1 = struct.unpack('i',ret1)
res2 = struct.unpack('i',ret2)
res3 = struct.unpack('i',ret3)

print(res1)
print(res2)
print(res3)












