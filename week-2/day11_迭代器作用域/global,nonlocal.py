# global 作用:
# 在局部作用域声明一个全局变量

#name = 'alex'
# def func():
#     global name
#     name = 'taibai'
#     #print(name)
#     #global name2='al'
#
# func()
# print(name)


def func():
    global name
    name ="太白金星"

#print(name) #这一句是不能执行的，因为函数还没有执行，这个global 变量还没有创建出来
func()

print(name)

# 在局部函数中修改一个全局变量

count = 1
def funs():
    global count
    count +=1
funs()
print(count)

# nonlocal
# 不能操作全局变量
# 作用域:局部作用域 ，内层函数对外层函数的局部变量进行修改时，使用。
count = 1
def funcc():
    count = 1
    def inner():
        nonlocal count # 这个时候，这个函数内部就可以操作上层funcc函数中的count
        count += 1
    print(count)
    inner()
    print(count)


funcc()
















