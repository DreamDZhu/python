# %s format

name = '太白'
age = 18
#msg = '我叫%s,今年%s' % (name, age)
#msg1 = '我叫{},今年{}'.format(name, age)


# print(msg)
# print(msg1)


# 格式化输出
msg2 = f'我叫{name},今年{age}'
print(msg2)

# 可以加表达式
dic = {'name': 'alex', 'age': 73}
msg3 = f'我叫{dic["name"]},今年{dic["age"]}'  # 外边用单引号，内边就用双引号。不能一致。

# 可以写表达式
count = 7
print(f'结果为:{count**2}')
print(f'结果为:{str(count).upper()}')

# 结合函数
def _sum(a, b):
    return a + b
msg = f'最终结果为:{_sum(10,20)}'
print(msg)

# 优点
'''
结构更加简单
效率更高

'''
