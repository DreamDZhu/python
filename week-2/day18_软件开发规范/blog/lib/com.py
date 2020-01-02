
def get_user_pwd(path):
    user_dict = {}
    with open(path, encoding='utf-8') as f:
        for line in f:
            info_lst = line.strip().split(',')
            user_dict[info_lst[0].strip()] = info_lst[1].strip()
    return user_dict


def auth(f):
    def inner(*args, **kwargs):

        # 登录验证
        print(123123123)


        ret = f(*args, **kwargs)
        return ret
    return inner
