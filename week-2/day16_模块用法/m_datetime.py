"""
datetime 模块：日期与时间

封装了一些和日期，时间相关的类

date
time
timedelta
"""
import time
import datetime

# date类

# print 2019-12-31
d = datetime.date(2019, 12, 31)

# 获取d 对象的各个属性
print(d.year, d.month, d.day)

# time类
t = datetime.time(12, 59, 59)

print(t.hour, t.minute, t.second)

# datetime类 datetime 模块中的类，主要是用于数学计算
dt = datetime.datetime(2019, 12, 31, 23, 59, 59)
print(dt)

# timedelta 时间变化量
td = datetime.timedelta(days=1, seconds=10)
tdd = datetime.date(2010, 10, 10)

# 参与数学运算
# 创建时间对象
# while True:
#     tdd += td
#     print(tdd)
#     time.sleep(1)

# 时间变化量的计算，是否会产生进位 答案是会产生进位的
td = datetime.timedelta(seconds=10)
tdd = datetime.datetime(2010, 10, 10, 10, 10, 59)

res = td + tdd
print(res) # 2010-10-10 10:11:09

# 练习：计算某一年的二月份有多少天
# 普通算法：根据年份，计算是否是闰年，是：29天，否：28天
# 用datetime模块，
# 首先创建出指定年份的3月1号，然后减一天，如果是29就是闰年，28天就不是

def check_year(year):
    dd = datetime.date(year,3,1)
    dt = datetime.timedelta(days=1)

    dd = dd - dt
    if dd.day == 28:
        print("No")
    else:
        print("YES")

check_year(2019)
check_year(2020)

# 和时间段进行运算的结果类型：与非timedelta 类型的变量保持一致



