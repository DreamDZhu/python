# 猫：吃，喝，睡，爬树
# 狗：吃，喝，睡，看家


# 没有用继承的时候，吃喝睡明明是一样的方法，但是两个class类都拥有，重复了。
# class Cat:
#     def __init__(self):
#         pass
#
#     def eat(self): pass
#     def drink(self): pass
#     def sleep(self): pass
#     def play_tree(self): pass
#
#
# class Dog:
#     def __init__(self):
#         pass
#
#     def eat(self): pass
#     def drink(self): pass
#     def sleep(self): pass
#     def watch_home(self):pass

# 继承 - 解决代码重复的问题

# class A:
#     pass

# 表示B继承A , A是父类，B是子类

#
# class B(A):
#     pass

# A 是父类，基类，超类
# B 是子类，派生类
# 子类可以使用父类中的所有方法和静态变量

# 继承的语法
# class 子类名(父类名):pass


# class Animal:
#     def __init__(self, name, food):
#         self.name = name
#         self.food = food
#         self.hp = 100
#         self.mp = 100
#
#     def eat(self):
#         print(f"{self.name}吃{self.food}")
#
#     def drink(self):
#         print(f"{self.name}喝水")
#
#     def sleep(self):
#         print(f"{self.name}睡觉")
#
#
# class Cat(Animal):
#     def play_tree(self):
#         print(f"{self.name}爬树")
#
#     def eat(self):
#         Animal.eat(self)
#         self.hp += 100
#
#
# class Dog(Animal):
#     def watch_home(self):
#         print(f"{self.name}看家")
#
#     def eat(self):
#         Animal.eat(self)
#         self.mp += 100
#
#
# 小白 = Cat('小白', '猫粮')
# 小黑 = Dog('小黑', '狗粮')

# print(Animal.name)
# print(Animal.food)

# 先开辟空间，空间里有一个类指针 --> 指向 Cat
# 调用init ，对象在自己的空间中找Init 没找到，到cat 类中找init 也没找到
# 找父类Animal 中的init

# 小白.sleep()
# 小白.play_tree()

# 小白.eat()
# 小黑.eat()
#
# print(小白.hp, 小白.mp)
# print(小黑.hp, 小黑.mp)

# 有时，子类想要调用父类的方法的同时，还想执行自己的同名方法。
# 可以在子类的方法中，调用父类名+方法  如：Animal.eat(self) 并手动传递self

# 子类调用对象，如果自己拥有，优先调用自己的，如果自己没有，就去调用父类的。如果父类还是不存在，就报错。


# 执行代码输出什么？
from types import FunctionType, MethodType


class Foo:
    def __init__(self):
        self.func()  # 在每一个self 调用func的时候，我们不看这句话在哪里执行，而是看self究竟是谁

    def func(self):
        print('in foo')


class Son(Foo):

    def func(self):
        print('in son')

# Son()

# 如何给狗和猫定制个性的属性


class Animal:
    def __init__(self, name, food):
        self.name = name
        self.food = food
        self.hp = 100
        self.mp = 100

    def eat(self):
        print(f"{self.name}吃{self.food}")

    def drink(self):
        print(f"{self.name}喝水")

    def sleep(self):
        print(f"{self.name}睡觉")


class Cat(Animal):
    def __init__(self, name, food, eye_color):
        Animal.__init__(self, name, food)  # 调用父类的初始化，去完成一些通用属性的初始化
        self.eye_color = eye_color         # 这样这个属性，就属于派生属性


class Dog(Animal):
    def __init__(self, name, food, size):
        Animal.__init__(self, name, food)
        self.size = size


# 小白 = Cat('小白', '猫粮', '蓝色')
# print(小白.__dict__)


# 单 多重继承
# class A:
#     def __init__(self):
#         self.func()
#
#     def func(self):
#         print("i am a")
#
# class B(A):
#     def func(self):
#         print("i am b")
#
# class C(B):pass
# c = C()


# 多继承 有好几个爹
# 有一些语言不支持多继承 java
# python 语言的特点：可以在面向对象中支持多继承

class A:
    def func(self): print("IN A")


class B:
    def func(self): print("IN B")


class C(B, A):
    pass


# 当进行多继承时，调用到多个父类中的同名方法时，函数的寻找顺序优先从先继承的父类中寻找，以此类推
# C().func()

# 调子类的对象：子类自己拥有的时候
# 调父类的对象：子类自己没有的时候
# 调子类和父类的：子类父类都有，在子类中调用父类的

# 多继承
# 一个类有多个父类，在调用父类方法的时候，按照继承顺序，先继承的就先寻找，以此类推


# 所有类都默认继承Object 类
class A(object):
    pass


# 输出A的父类
# print(A.__bases__)  # (<class 'object'>,)


class C:
    pass


class B(A, C):
    pass


# print(B.__bases__)  # (<class '__main__.A'>, <class '__main__.C'>)

# 如果存在多层继承关系的话， 默认bases 只输出上一级父类信息，



a = 10
b = 'abc'
c = 110

# 判断数据是否是对应的类型
# print(isinstance(a, int))
# print(isinstance(b, str))
# print(isinstance(c, str))
#
# # 也是判断类型
# print(type(a) is int)
# print(type(b) is str)


class Animal:pass
class Cat(Animal):pass

小白 = Cat()

print(type(小白) is Cat)  # True
print(type(小白) is Animal) # False

print(isinstance(小白, Cat)) # True
print(isinstance(小白, Animal)) # True

# 对比后能发现，type 只能判断对象是否是该类型 。而isinstance ，可以判断对象跟对象的继承关系



# 绑定方法和普通函数
# FunctionType : 函数
# MethodType : 方法

# isinstance type



