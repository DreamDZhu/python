# sys argv 练习
# 写一个python 脚本，在cmd 里执行
# python xxx.py 用户名 密码 cp 文件路径 目的地址

import sys
import os
import shutil


# def args_check(f):
#
#     def inner(*args, **kwargs):
#         # 判断args 中，不能有空值
#
#         f(*args, **kwargs)
#     return inner


# rm /root/1.txt
def rm(*args):
    rm_path = args[0]
    if os.path.isfile(rm_path):
        os.remove(rm_path)
    elif os.path.isdir(rm_path):
        shutil.rmtree(rm_path)


# cp /root/1.txt /root/go/src/2.txt
def cp(*args):
    src_path = args[0]
    dest_path = args[1]
    # if args[0] or args[1]:
    #     print("args error !!")
    #     return

    if os.path.exists(src_path) and os.path.exists(dest_path):
        # 获取要复制的文件名
        filename = os.path.basename(src_path)
        # 检测目标路径是否存在文件名，如果存在的话就是复制到目标路径并重命名
        dest_filename = os.path.basename(dest_path)
        if dest_filename is None:
            dest_path = os.path.join(dest_path, filename)

        shutil.copy2(src_path, dest_path)


# rename /root/1.txt /root/2.txt
def rename(*args):
    # old_name = os.path.basename(args[0])
    # new_name = os.path.basename(args[1])
    # 文件重命名
    if os.path.isfile(args[0]):
        os.rename(args[0], args[1])
    # 目录重命名
    elif os.path.isdir(args[0]):
        shutil.move(args[0], args[1])


# move /root/1.txt /root/2.txt
def move(*args):
    pass


def mkdir(*args):
    pass


cmd_dict = {
    'rm': rm,
    'cp': cp,
    'rename': rename,
    'move': move,
    'mkdir': mkdir,
}


def test_argv():
    if len(sys.argv) >= 5:
        username = sys.argv[1]
        password = sys.argv[2]
        # 模拟
        if username == 'alex' and password == '123456':
            if sys.argv[3] in cmd_dict:
                # 根据argv 个数来传递参数
                if len(sys.argv) == 5:
                    cmd_dict[sys.argv[3]](sys.argv[4], sys.argv[5])
                elif len(sys.argv) == 4:
                    cmd_dict[sys.argv[3]](sys.argv[4])

    else:
        print("请输入一条有效的命令")

    file_path = sys.argv[0]
