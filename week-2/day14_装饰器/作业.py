# 从文件中读取账号密码  abc | 123132
# 输入账号密码进行登录，最多重试3次，如果输入的账号密码与文件中匹配则返回成功，否则返回失败
# 错误3次以后结束程序

def get_user_pwd():
    user_dict = {}
    with open('register', encoding='utf-8') as f:
        for line in f:
            line_list = line.strip().split('|')
            user_dict[line_list[0].strip()] = line_list[1].strip()
    return user_dict


def login():
    u_dict = get_user_pwd()
    count = 1
    while count < 4:
        username = input("请输入账号: ").strip()
        password = input("请输入密码:").strip()
        if username in u_dict and password == u_dict[username]:
            print("登录成功")
            return True
        else:
            print("登录失败,请重试")
        count += 1
    print("登录次数过多，登录失败")
    return False

