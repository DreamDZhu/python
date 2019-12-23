# python 提供了多个内置函数。

# eval 执行字符串类型的代码 , 工作中慎用
eval("print(123)")

s = '{"name":"alex"}'
print(s, type(s))
print(eval(s))

# 在获取网络传输的str,input 输入，sql 注入，绝对不能使用eval ,容易被黑客攻击

# exec 与 eval 几乎一样，但是exec 用于处理代码流
msg = """
for i in range(10):
    print(i)
"""
exec(msg)

# hash 获取一个对象的哈希值
str = "abc"
print(hash(str))

# help 获取函数或者模块的详细说明
#help(str)

# callable 判断对象是否可调用 （函数可以被调用）
s1 = 'asdaffsd'
print(callable(s1))













