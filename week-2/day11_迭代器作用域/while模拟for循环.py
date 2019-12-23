ll = [11, 22, 33, 44, 55, 66, 77, 88, 99, 121123, 13123, 123, 1]

# 将可迭代对象转换成迭代器

def my_while(obj):
    obj = iter(obj)
    while 1:
        try:            # 遇到最后+1 要捕获异常后正常退出
            print(next(obj))
        except StopIteration:
            break

my_while(ll)