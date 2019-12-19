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
s1 = 'fjdsk1'
#print(dir(s1))

# 所以只要判断__iter__ 字符串是否存在于dir(对象) 中，如果存在，该对象就是一个可迭代对象。如果不在，就不是可迭代对象。
if "__iter__" in dir(s1):
    print(123)

# 关于可迭代的对象
# 优点：存储的数据直接能显示，比较直观。
      #拥有的方法比较多，操作方便
# 缺点：占用内存。
      #不能直接通过for循环，不能直接取值（索引,key）

# 可迭代对象，是不能直接取值的。之所以可以直接用for来进行操作，是因为自动将其转换为了 ： 迭代器











