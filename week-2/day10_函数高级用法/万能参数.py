# 形参角度
# 万能参数


def eat(a, b, c, d, e, f):
    print('eat: %s,%s,%s,%s,%s,%s' % (a, b, c, d, e, f))


#eat('1', '2', '3', '4')

# 当我们实参这时候，需要传输更多参数的时候，我们就需要去更改方法源码
eat('1', '2', '3', '4', '5', '6')

# args 只是一个形参名，但通常是万能参数的约定俗称名
# * 在函数定义时，代表聚合。* 将所有的位置参数聚合成一个元组，赋值给args
def eat_all(*args):
    print(args)
    print("我请你吃:%s,%s,%s,%s" %(args))


eat_all(1, 2, 3, "a")

# 写一个函数：计算你传入函数的所有数字的和
def count_num(*args):
    count = 0
    for num in args:
        count += num
    print(count)

count_num(1,2,3,4,5,6,7)

# 也是一种万能函数，** 也是一种聚合，将所有的关键字参数，聚合成一个字典中，赋值给kwargs
# def count(**kwargs):
#     print(kwargs)
# count(name="ddz",age="18",sex="man")


# 真正的万能参数，接收所有的参数
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
# func(1111,name="aaa")


# def fuc(a,b,*args,sex="男"):
#     print(a,b)
#     print(sex)
#     print(args)
# fuc(1,2,3,4,5,6,sex="女")

# **kwargs 位置 , 当使用kwargs 时，需要把kwargs放到参数的最后
# def fux(a,b,*args,sex='男',**kwargs):
#     print(a,b)
#     print(sex)
#     print(args)
#     print(kwargs)
#
# fux(1,2,3,4,5,sex='女',name='alex',age=18)

# 形参角度的第四个参数：仅限关键字参数，表示函数只能接受关键字参数
# 像下面这样的函数定义，C看似是一个位置参数，其实是一个关键词参数，如果在调用处不传递c="xxx" ，那么调用就会报错
# def fuv(a,b,*args,sex="男",c,**kwargs):
#     #do something
#     print(a)


# * 在函数调用时，写在实参中，* 代表打散
def func(*args):
    print(args)

func(*[1,2,3],*[22,33]) # 等同于 (1,2,3,22,33)

def funcc(*args,**kwargs):
    print(args)
    print(kwargs)

# 当我们不使用* 来打散列表的时候，会发现，args 获得了所有的元素，删除结果为：({'name': 'ddz', 'age': '18'},)
#      {}
funcc({'name':'ddz'},{'age':'18'})
# 而当我们的调用变成
funcc(**{'name':'ddz'},**{'age':'18'})
# 结果：()
#      {'name': 'ddz', 'age': '18'}

# ** 打散了字典，而字典成为了关键字参数，所以kwargs接受到了打散后的内容。




