# 看代码求结果：

# def test():
#     for i in range(4):
#         yield i

# g=test()  # 这个方法不会执行， 只有执行next ,list()时，才会执行

# g1 = (i for i in g) #没有执行，只是生成了一个生成器地址
# g2 = (i for i in g1) #没有执行，只是生成了一个生成器地址

# 结果: [0, 1, 2, 3]
# print(list(g1))
# print(list(g2))
# 结果: []  ，由于是生成器，g1 已经将生成器取到了3，g2已经无法继续取值，所以输出为[]
# print(list(g2))

# 看代码求结果 答案是 ：[20, 21, 22, 23]

def add(n, i):  #函数，调用就执行
    return n + i


def test(): #生成器
    for i in range(4):
        yield i


g = test()  #赋值生成器，只是记录一个地址，没有执行
for n in [1, 10]:
    g = (add(n, i) for i in g)  # 循环两次，产生了两个生成器对象！也没有执行 。由于没有执行，所以第二次生成的g ，并不会覆盖第一次生成的g !!



###
print(list(g))

