# 深copy
# 把外壳与内容，全部进行复制，创建新的内存空间存放

import copy

l1 = [1, 2, 3, ["aa", "bb", ["cc", "dd"]]]
l2 = copy.deepcopy(l1)

print(l1, id(l1), id(l1[3]))
print(l2, id(l2), id(l2[3]))

l1[-1].append("oo")

print(l1, id(l1))
print(l2, id(l2))


"""
结果：
[1, 2, 3, ['aa', 'bb', ['cc', 'dd']]] 4366825424
[1, 2, 3, ['aa', 'bb', ['cc', 'dd']]] 4366464576
[1, 2, 3, ['aa', 'bb', ['cc', 'dd'], 'oo']] 4366825424
[1, 2, 3, ['aa', 'bb', ['cc', 'dd']]] 4366464576
"""
# 但是python 对深拷贝做了优化，当遇到不可变数据类型进行深拷贝时，指向的依然是同一个内存空间 , 但是可变数据类型，指向的是完全不同的内存空间

print(id(l1[0]))
print(id(l2[0]))

# 切片是属于浅拷贝
l1 = [1, 2, 3, ["a", "b"]]
l2 = l1[:]
l1[-1].append("a")

print(l1) #[1, 2, 3, ['a', 'b', 'a']]
print(l2) #[1, 2, 3, ['a', 'b', 'a']]

# 浅copy: 嵌套的可变数据类型是同一个
# 深copy: 嵌套的可变数据类型不是同一个
