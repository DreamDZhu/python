# 装饰器的应用：登录认证


status_dict = {
    'username': None,
    'status': False
}

user_dict = {}


# 注册
def load_info():
    with open('register.txt', encoding='utf-8') as f:
        for line in f:
            info_lst = line.strip().split(',')
            user_dict[info_lst[0].strip()] = info_lst[1].strip()


load_info()


def register():
    print("进入注册系统，输入Q退出注册系统")
    while True:
        username = input("请输入要注册的用户名: ").strip()
        password = input("请输入要注册的密码: ").strip()
        if username.upper() == "Q" or password.upper() == "Q":
            return False
        if username in user_dict:
            print("用户名已被注册!!")
            continue
        user_dict[username] = password

        with open('register.txt','a+',encoding='utf-8') as f:
            f.write(f'{username},{password}\n')
            print('注册成功')
            return True

# 登录


def login():
    count = 0
    while count < 3:
        username = input("请输入你的用户名: ").strip()
        password = input("请输入你的密码: ").strip()
        if username in user_dict and password == user_dict[username]:
            print("登录成功,enjoy!")
            status_dict['username'] = username
            status_dict['status'] = True
            return True
        else:
            print("账号密码错误!")
            count += 1
    return False

# 登录认证判断 装饰器需要完成，访问被装饰函数之前，写一个三次登录认证的功能


def auth(f):
    def inner(*args, **kwargs):
        # 在这里检测三次登录认证
        if not status_dict['status']:
            login_staus = login()
            if not login_staus:
                print("您未登录，无法使用其他功能!")
                return False
        # 执行真正的函数
        ret = f(*args, **kwargs)
        return ret
    return inner


@auth
def article():
    print("欢迎访问文章页面")


@auth
def comment():
    print("欢迎访问评论页面")


@auth
def dariy():
    print("欢迎访问日记页面")


switch = {
    '1': register,
    '2': login,
    '3': article,
    '4': comment,
    '5': dariy
}

while True:
    print("请输入要执行的操作:1.注册,2.登录,3.访问文章,4.访问评论,5.访问日记")
    input_opt = input().strip()
    if input_opt in switch:
        switch.get(input_opt, lambda: "nothing")()
    else:
        print("不存在该项!")
