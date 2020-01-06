# 先定义一个对象集合，用来描述一类事物
# 每一个对象，应该拥有相同的属性与动作

# 定义Person 类


class Person:
    # 类的初始化函数 , 这个类似 构造函数 ？？
    # 类的所有属性都可以写在这个里面
    def __init__(
            self,
            name="无名氏",
            sex="男",
            job="乞丐",
            level=0,
            hp=100,
            weapon="拳头",
            ad=1):
        # print('-'*10)
        self.name = name
        self.sex = sex
        self.job = job
        self.level = level
        self.hp = hp
        self.weapon = weapon
        self.ad = ad
        # print('*'*10)

    # 在类中的方法，缩进一次的方法在执行模块的时候，会自动执行，而缩进两次的内容，不会执行


# 类名() 会自动调用类中的__init__方法
alex = Person()  # alex 就是对象 alex = Persion()的过程，是通过类获取一个对象的过程，这个过程称之为：实例化
wusir = Person("wusir", "男", "法师", 0, 500, "打狗棒", 1000)


# rint(wusir.name)

print(alex.__dict__)
print(wusir.__dict__)

# 类和对象之间的关系?
# 类 是一个大范围，是一个模子，它约束了事物有哪些属性，但是不能约束具体的值
# 对象 是一个具体的内容，是类的表现，遵循了类的约束，同时给属性赋予具体的值


# 在这个案例中，Person 就是一个类 ，而 alex 与 wusir 就是这个类的对象
