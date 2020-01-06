import random
import time


class Dog:
    def __init__(self, name, blood, ad, kind):
        self.dog_name = name
        self.hp = blood
        self.ad = ad
        self.kind = kind
        self.random = 10

    # 舔舔攻击
    def lick(self, person):  # 方法，拥有一个必须传的参数 --> self
        hit = random.randint(1, self.random)
        person.hp -= hit
        print(self.lick_format(self.dog_name, person.person_name, hit))

    def lick_format(self, dog_name, person_name, hit):
        return f"{dog_name}舔了一口{person_name},对其造成了{hit}点伤害"


class Person:
    def __init__(self, name, blood, ad, kind):
        self.person_name = name
        self.hp = blood
        self.ad = ad
        self.kind = kind
        self.random = 20

    # 普通攻击
    def fight(self, dog):
        hit = random.randint(1, self.random)
        dog.hp -= hit
        print(self.fight_format(self.person_name, dog.dog_name, hit))

    def fight_format(self, person_name, dog_name, hit):
        return f"{person_name} 打了{dog_name}一拳，对其造成了{hit}点伤害"


alex = Person('alex', 1000, 10, "未知")
dog = Dog('小黑', 5000, 50, "泰迪")


print("人狗大战开始!")
flag = True
while True:
    time.sleep(1)
    if flag:
        alex.fight(dog)
        print(f"{alex.person_name}剩余{alex.hp}血量")
        print("==================================")
        flag = False
        if alex.hp <= 0:
            print("over ,alex die")
            break
    else:
        dog.lick(alex)
        print(f"{dog.dog_name}剩余{dog.hp}血量")
        print("==================================")
        flag = True
        if dog.hp <= 0:
            print("over, dog die")
            break





