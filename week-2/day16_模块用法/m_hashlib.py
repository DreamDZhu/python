"""

hashlib : 封装一些用于加密的类

加密的目的 ： 用于判断和验证，而非解密
"""

import hashlib

# 给一个数据加密的三大步骤
# 获取一个加密对象
m = hashlib.md5()
# 使用加密对象的update ，进行加密
m.update('123456'.encode('utf-8'))
# 通过hexdigest 获取加密结果 或digest
res = m.hexdigest()  # e10adc3949ba59abbe56e057f20f883e
# res = m.digest()  # b'\xe1\n\xdc9I\xbaY\xab\xbeV\xe0W\xf2\x0f\x88>'

print(res)

# 给一个数据加密
# 验证：用另一个数据加密的结果和第一次加密的结果对比
# 如果结果相同，说明原文相同

# 不同加密算法：实际上是加密结果的长度不同。
sha256 = hashlib.sha256('1qaz2wsx'.encode('utf-8')).hexdigest()
print(sha256)

# 在创建加密对象时，可以指定参数，称为salt
# 这个abc就可以称为salt  也就是在初始化的时候加上一段字符，这样未来所有的加密都是 md5(abc + xxx)
m = hashlib.md5(b'abc')
print(m.hexdigest())

m = hashlib.md5()
m.update(b'1qaz2wsx')
print(m.hexdigest())
