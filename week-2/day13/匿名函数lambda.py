# 匿名函数，一句话函数 ，一行构建一个函数

# 普通用法


def func(a, b):
    return a + b


# 构建匿名函数
func1 = lambda a, b: a + b
print(func1(1,2))

# 接收一个可切片的数据，返回索引为0与2的对应元素（元祖形式）
func2 = lambda arg: (arg[0],arg[2])

# 写匿名函数：接收两个int参数，将较大的数据返回
func3 = lambda a,b: a if a > b else b

print(func3(100,20))