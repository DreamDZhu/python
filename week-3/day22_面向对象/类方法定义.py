class Dog:
    def __init__(self, name, blood, ad, kind):
        self.dog_name = name
        self.hp = blood
        self.ad = ad
        self.kind = kind

    def lick(self):  # 方法，拥有一个必须传的参数 --> self
        print("hahahha", self.__dict__)


class Person:
    def __init__(self, name, blood, ad, kind):
        self.person_name = name
        self.hp = blood
        self.ad = ad
        self.kind = kind

    def fight(self, dog):
        print(f'{self.person_name} 打了一下 {dog.dog_name},造成了{self.ad}点伤害。')


alex = Person("alex", 250, 10, "人")


write = Dog("小白", 100, 100, "泰迪")
# write.lick()
yellow = Dog("小黄", 100, 100, "金毛")
# yellow.lick()

alex.fight(write)








