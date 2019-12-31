"""

os : 和操作系统相关的操作被封装到这个模块中

"""

import os

# 和文件操作相关，重命名，删除

# os.remove(r"1.txt") # 删除
# os.rename(r'1.txt',r'2.txt') # 修改文件名

# 删除目录，必须是空目录才能删除
# os.removedirs(r'aa') # 删除对应目录
# 在程序中删除数据，不会放入回收站

# 使用shutil 模块，可以删除目录中带内容的目录
# import shutil
# shutil.rmtree(r'aa')

# 和路径相关的操作，被封装到另一个子模块中：os.path
print(os.path.dirname(r"c:/a/a/b.txt"))  # 取出路径的父目录 c:/a/a
# 返回一个路径的绝对路径 /Users/ddz/Desktop/workspace/python/week-2/day16_模块用法/aa/1.txt
print(os.path.abspath(r'aa/1.txt'))
print(os.path.abspath(r'/aa/1.txt'))  # 如果以/开头，就是当前路径


print(os.path.basename(r'c:/a/a/b.txt'))  # 取出文件名 b.txt

# 切割路径，直接返回dirname 和 basename ('c:/a/b', 'c.txt')
print(os.path.split(r'c:/a/b/c.txt'))
print(os.path.join(r'd', r'aaa', r'bbb.txt'))  # 拼接路径 d/aaa/bbb
print(os.path.exists(r'aa/1.txt'))  # 判断文件是否存在 True
print(os.path.isabs(r'aa/1.txt'))  # 判断路径是不是绝对路径
print(os.path.isdir(r'aa/1.txt'))  # 判断该路径下的文件，是否是目录，如果不存在是False
print(os.path.isfile(r'aa/1.txt')) # 判断该路径下的文件，是否是普通文件
print(os.path.islink(r'aa/1.txt')) # 判断文件是否是链接文件

