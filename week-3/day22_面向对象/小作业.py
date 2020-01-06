# 定义一个圆形类，半径是这个圆形的属性，实例化一个半径为5的圆形，一个半径为10的圆形，
# 该类 有两个方法，一个是返回圆的周长，一个是返回圆的面积
class Spherical:
    def __init__(self, radius):
        self.radius = radius
        self.pai = 3.14

    def get_perimeter(self):
        return 2 * self.pai * self.radius

    def get_area(self):
        return self.pai * self.radius * self.radius

# radius_5 = Spherical(5)
# print(radius_5.get_perimeter())
# print(radius_5.get_area())
# radius_10 = Spherical(10)

# 定义一个用户类，用户名和密码是这个类的属性，实例化两个用户，分别有不同的用户名和密码
# 设计一个方法，允许修改密码
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        if self.username == "root" and self.password == "123456"
            print("登录成功")
        else:
            print("登录失败")

    def change_pwd(self,new_pwd):
        self.password = new_pwd

# 完善人狗大战，比如狗造成的是随机区间伤害，每个人一个回合自动战斗，直到一方狗带。
# 双方均有一定的概率闪避攻击



