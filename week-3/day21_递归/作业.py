# os模块: 查看一个文件夹下的所有文件，这个文件夹下面还有文件夹，不能用walk

import os


def show_file(path):
    # 获取该路径下所有文件名，并返回一个列表
    name_lst = os.listdir(path)
    for name in name_lst:
        # 通过组合获取所有目录的绝对路径
        abs_path = os.path.join(path, name)
        if os.path.isfile(abs_path):
            print(abs_path)
        elif os.path.isdir(abs_path):
            show_file(abs_path)




show_file("/Users/Ddz/Desktop/workspace/python/")