import os
import sys


user_dict = {}
status_dict = {
    'username':None,
    'status':False
}

def get_user_pwd():
    with open(conf.register_path, encoding='utf-8') as f:
        for line in f:
            info_lst = line.strip().split(',')
            user_dict[info_lst[0].strip()] = info_lst[1].strip()


# 装饰器在文件中，属于公共组件
def auth(f):

    def inner(*args,**kwargs):
        ret = f(*args,**kwargs)
        return ret
    return inner


def login():
    pass

def register():
    pass



# 这些属于主逻辑函数
@auth
def article():
    print('欢迎访问文章界面')

@auth
def comment():
    print('欢迎访问评论页面')

@auth
def dariy():
    print('欢迎访问日记页面')

@auth
def collections():
    print('欢迎访问收藏页面')



def loginout():
    pass


def _quit():
    pass

dic = {
    1:login(),
    2:register(),
}

def run():
    while True:
        print("""
            1.登录
            2.注册
            3.进入文章页面
            4.进入评论页面
            5.进入日记页面
            6.进入收藏页面
            7.注销账号
            8.退出整个程序
        """)
        num = input('请输入对应选项: ').strip()
        num = int(num)

run()  # 属于启动按钮