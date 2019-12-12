# 写函数，用户传入修改的文件名，要修改的内容，执行函数，完成整个文件的批量修改操作
import os


def file_change(path, old_str, new_str, ecd='utf-8'):
    with open(path, encoding=ecd) as f1,\
            open(path + '.bak', encoding=ecd, mode='w') as f2:
        for line in f1:
            new_line = line.replace(old_str, new_str)
            f2.write(new_line)
    os.remove(path)
    os.rename(path + '.bak', path)
