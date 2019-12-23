def func():
    lst1 = ['a','b','c','d']
    lst2 = [1,2,3,4]
    yield from lst1
    yield from lst2

ret = func()

for i in range(8):
    print(next(ret),end=' ')

# 结果 a b c d 1 2 3 4

# 通过结果发现，虽然写两个yield ，但是他们并不是交叉输出，而是当一个yield from全部生成结束，再使用下一个yield from





