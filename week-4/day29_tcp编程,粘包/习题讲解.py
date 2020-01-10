class Foo(object):
    def __init__(self,num):
        self.num = num

v1 = [Foo for i in  range(10)]
v2 = [Foo(5) for i in range(10)]
v3 = [Foo(i) for i in range(10)]

print(v1)
print(v2)
print(v3)



# 重写 eq , gt ,lt 方法

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def ___eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False

    # 大于
    def __gt__(self, other):pass

    # 小于
    def __lt__(self, other):pass







