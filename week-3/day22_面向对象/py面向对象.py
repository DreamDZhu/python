# alex = {
#     'name': 'alex',
#     'sex': '不详',
#     'job': 'it man',
#     'level': 0,
#     'hp': 250,
#     'atk': 10
# }
# dog = {
#     'name': '太白',
#     'sex': 'man',
#     'level': 0,
#     'hp': 250,
#     'atk': 5
# }

# 保证所有的玩具初始化的时候拥有相同的数学
# 每来一个新玩家，都手动创建一个字段，然后向字典中传值


def Persion(name, sex, job, hp, weapon, ad, level=0):
    def 搓(dog):
        dog['hp'] -= dic['ad']
        print(f'{dic["name"]} 搓了一下{dog["name"]},造成了{dic["ad"]}点伤害。')

    dic = {
        'name': name,
        'sex': sex,
        'job': job,
        'hp': hp,
        'weapon': weapon,
        'ad': ad,
        'level': level,
        'action': 搓
    }
    return dic


def Dog(name, kind, hp, ad):

    # 闭包
    def 舔(person):
        person['hp'] -= dic['ad']
        print(f'{dic["name"]}舔了一口{person["name"]},造成了{dic["ad"]}点伤害')

    dic = {
        'name': name,
        'kind': kind,
        'hp': hp,
        'ad': ad,
        'action': 舔
    }
    return dic


alex = Persion('alex', '不详', '搓澡工', 250, '搓澡巾', 1)
whit = Dog('小白', '泰迪', 5000, 249)


whit['action'](alex)
alex['action'](whit)


# 面向过程： 想要一个结果 写代码 实现计算结果
# 面向对象开发： 有哪些角色 角色的属性和技能 两个角色之间是如何交互的

# 复杂的 拥有开放式结束的程序 比较适合使用面向对象开发来完成

