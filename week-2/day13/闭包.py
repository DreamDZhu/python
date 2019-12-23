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

# ll 之所以存在，就是因为闭包现象：




