exp = (1 + 3 * 4 * 5 / 6) - 4


# 计算两个数的乘法或者除法
def mul_div(exp):
    if '*' in exp:
        a, b = exp.split('*')
        return float(a) * float(b)
    if '/' in exp:
        a, b = exp.split('/')
        return float(a) / float(b)

# 计算表达式中的所有的乘除法






