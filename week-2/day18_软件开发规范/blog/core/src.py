import os
import sys
from conf import settings
from lib import com

user_dict = {}
status_dict = {
    'username':None,
    'status':False
}

user_dict = com.get_user_pwd(settings.REGISTER_PATH)


def login():
    pass

def register():
    pass


# 这些属于主逻辑函数
@com.auth
def article():
    print('欢迎访问文章界面')

@com.auth
def comment():
    print('欢迎访问评论页面')

@com.auth
def dariy():
    print('欢迎访问日记页面')

@com.auth
def collections():
    print('欢迎访问收藏页面')



def loginout():
    pass


def _quit():
    pass

dic = {
    1:login,
    2:register,
    3:article,
    4:comment,
    5:dariy,
    6:collections,
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
        if num in dic:
            dic[num]()
        else:
            print("选项不存在!!!")
