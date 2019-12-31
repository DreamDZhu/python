import random

print(random.random())  # [0.0,1.0) 范围内浮点数
print(random.randint(1, 10))  # 获取[a,b] 范围内的一个整数
print(random.uniform(1, 10))  # 获取[a,b） 范围内的一个浮点数

x = [1, 2, 3, 4, 5]
print(random.shuffle(x))  # 把参数指定的数据中的元素打乱，参数必须是一个可变的数据类型
print(x)

k = ['a', 'b', 'c', 'd', 'e']
k = random.sample(k, 3)  # 从k中随机抽取3个数据，组成一个列表返回
print(k)
