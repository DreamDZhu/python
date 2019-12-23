# 封闭的东西: 保证数据的安全。

# ll = []
# l1 = []
# def make_avg(new_value):
#     ll.append(new_value)
#     total = sum(ll)
#     avg = total / len(ll)
#     return avg
# ll.append(50)
# print(make_avg(10000))
# print(make_avg(12000))

# 由于ll 是全局变量，并不能保证数据安全，当我们有多行代码，对ll进行误操作，就会出现问题。


def make_averager():
    ll = []
    def averager(new_value):
        ll.append(new_value)
        total = sum(ll)
        return total/len(ll)
    return averager
avg = make_averager() # avg = averager 这个函数

# 输出后发现，ll虽然处于局部作用域，局部变量空间，但是却被缓存下来了，这是为什么？？
print(avg(100000))
print(avg(110000))
print(avg(120000))
print(avg(130000))

# ll 之所以存在，就是因为闭包现象：在这样的函数状态下,ll成为了一个自由变量，当每次执行avg时，获取到的ll，都是最初创建的ll对象。

# 闭包：
# 闭包只能存在于 : 嵌套的函数中
# 形成闭包的条件: 内层函数对外层函数，非全局变量的引用（使用）。
# 被引用的非全局变量，也称作：自由变量 。这个自由变量会与内层函数产生一个绑定关系，
# 自由变量不会在内存中消失。


# 闭包的作用：保证数据安全，闭包后的变量，外部无法进行直接访问，只有执行闭包函数，才会对自由变量造成影响。

# 如何判断一个嵌套函数，是不是闭包函数


# 闭包案例: 只要符合闭包的两大条件，都是属于闭包
def wrapper():
    a = 1
    def wrap():
        print(a)
    return wrap
ret = wrapper()

# 此案例不是闭包，因为a是全局变量！！！
a = 2
def wrappe():
    def wrap():
        print(a)
    return wrap

# 这也是闭包 ,不要被全局的a,b变量名混淆，当调用该函数时。传入了2，3
# 底层是在局部作用域中，创建了两个变量 a=2,b=3 ！！！，然后内部嵌套函数，使用了局部作用域中的变量
def wrapper (a,b):
    def inner():
        print(a)
        print(b)
    return inner
a = 2
b = 3
ret =wrapper(a,b)

# 判断函数是否是闭包 （如果一个函数拥有自由变量，那么这个函数，就属于闭包）
print(ret.__code__.co_freevars) #输出函数绑定的自由变量






