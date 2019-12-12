# 函数的传参：让函数封装的功能，更加灵活。

# meet() 括号中的表示形参，代表要接受的参数类型


def meet(sex, age, job):
    print("open app")
    print('性别:%s , 年龄:%s , python %s' % (sex, age, job))


# 调用函数，传递参数（）括号中的代表实参，实际参数
meet("女", "18", "技术好")

# 函数的传参： 实参，形参
# 实参角度：
# 1.位置参数 ，调用函数，从左到右边，一一对应。形参有多少，调用函数时，实参就应该有多少。

# 只接受2个int参数，将较大的数返回


def compare(a, b):
    if isinstance(a, int) & isinstance(b, int):
        print("success")
    return a if a > b else b


print(compare(10, 11))

# 三元运算符：简单的if else
a = 10
b = 20
# 表示如果a > b ，c = a 否则 c = b
c = a if a > b else b

# 2.关键字参数 ，直接将形参写在调用处，更清晰的调用方法 这种调用方式，参数顺序可以任意打乱
meet(sex="男", age="88", job="测试工作")

# 传入两个字符串参数，将两个参数拼接完成后，返回

# def split_str(str1, str2):
#     return str1 + str2
# print(split_str("abc", "edf"))

# 3.混合传参
# 将位置传参与关键字参数组合在一起。需要注意，关键字参数必须在位置传参的后面调用，否则会报错
# 在使用混合传参的时候 ，当前几个参数已经通过为止

def meet2(sex, age, skill, hight, weight):
    c = age + skill + hight
    print(c)
    return '筛选结果:性别:%s,体重:%s' % (sex, weight)


print(meet2("女", "18", "play game", "170", weight="130"))

# 默认参数：给函数设置默认参数，这样在调用的时候，可以简化函数填写
def meet3(sex,age,skill="运维大佬",hight="测试"):
    return sex + age + skill + hight
print(meet3("女","18"))