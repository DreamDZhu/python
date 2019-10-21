# 打开文件的几种方式

# 基本用法 出现异常程序崩溃
file = open("a.txt")
data = file.read()
file.close()

# 增加异常判断 冗余
file = open("a.txt")
try:
    data = file.read()
finally:
    file.close()

# with 方法 自带异常判断
with open("a.txt") as file:
    data = file.read()

