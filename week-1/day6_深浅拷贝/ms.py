# 默写
ll = []
while True:
    username = input("请输入用户名:")
    if username.upper() == "N":
        break
    password = input("请输入密码:")
    dic = {}
    dic['username'] = username
    dic['password'] = password
    ll.append(dic)
print(ll)

