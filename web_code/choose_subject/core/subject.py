# 课程
class Subject:

    def __init__(self, name, time, price):
        self.name = name
        self.time = time
        self.price = price

    def premium(self):
        self.price += int(self.price * 0.1)

    def discount(self, rate):
        if 0 < rate <= 1:
            self.price *= rate
        else:
            print("折扣率设置错误,请输入0-1区间的数")
