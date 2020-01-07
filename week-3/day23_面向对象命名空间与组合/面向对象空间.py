# 类型：int float str dict list tuple set - 类（内置的数据类型，内置的类）
# 变量名 = xx 数据类型对象

# class A:
#
#     country = '中国'      # 静态变量/静态属性  存储在类的命名空间中
#     def __init__(self,name,age,country):  # 绑定方法 存储在类的命名空间中
#         self.name = name
#         self.age = age
#         self.country = country
#
#     def func1(self):pass
#     def func2(self):pass
#     def func3(self):pass
#     def func4(self):pass
#     def func5(self):pass

# a.func3() # === A.func3()  在创建a对象的时候，会创建类指针，存储了类所在的内存地址
#
# print(a.name)
# print(a.country) # 这时候会发现，country 输出是印度，而不是中国。因为在声明类对象的时候，开辟的对象空间，存在country 变量，值为印度。所以会优先返回 对象空间中的属性，而不是类中的静态属性。
# print(A.country) # 这里输出就是中国


class A:

    country = '中国人'      # 静态变量/静态属性  存储在类的命名空间中

    def __init__(self, name, age, country):  # 绑定方法 存储在类的命名空间中
        self.name = name
        self.age = age


print(A.__dict__)

a = A('alex', 83, '印度')
b = A('wusir', 74, '泰国人')
A.country = '日本人'

print(a.country)
print(b.country)
print(A.country)

# 类中的变量是静态变量
# 对象中的变量只属于对象本身，不属于类，每个对象有属于自己的空间来存储对象的变量
# 当使用对象名去调用某一个属性的时候，会优先在自己的空间中寻找，如果找不到，再去对应的类空间中寻找
# 如果在对象空间中不存在，就引用类空间中的，如果类空间中还没有，就报错
# 对于类来说，类中的变量，所有的对象都是可以读取的，并且读取的是同一份变量




# 实现一个类，能够自动统计这个类，实例化了多少个对象
class W:
    count = 0
    def __init__(self):
        W.count +=1

    def get_count(self):
        return self.count


a = W()
b = W()

print(W.count)
# 类中的静态变量的用处
# 如果一个变量，是所有的对象共享的值，那么这个变量应该被定义成静态变量
# 所有和静态变量相关的增删改查都应该使用类名来处理


