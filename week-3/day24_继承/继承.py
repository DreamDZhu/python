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
class Foo:
    def __init__(self):
        self.func()

    def func(self):
        print('in foo')

class Son(Foo):

    def func(self):
        print('in son')

Son()

# 如何给狗和猫定制个性的属性









