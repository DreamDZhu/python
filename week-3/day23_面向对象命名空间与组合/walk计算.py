# 使用walk 来计算文件夹的总大小

import os

g = os.walk('/Users/ddz/Desktop/workspace/python/')
size = 0
for path, dirs, files in g:
    for name in files:
        # 获取绝对路径
        abs_path = os.path.join(path, name)
        # 获取文件大小，返回的是字节大小
        size += os.path.getsize(abs_path)


print(size)
print(size / 1024 / 1024)



