import sys

# 用这种方式读取文件，文件可以自动关闭。
with open("yesterday", 'r', encoding='utf-8') as f:
    for line in f:
        print(line)

# 同时打开多个文件
with open("yesterday2", 'r', encoding='utf-8') as f,\
        open("yesterday3", 'r', encoding='utf-8') as f2:
    for line in f:
        print(1)
    for line in f2:
        print(2)


# ASCII 英文占1个字节 中文在ascII中。。中文不能存在ASCII中！！
#


