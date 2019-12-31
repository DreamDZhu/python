"""
time 模块
"""

# 与时间相关的操作，封装了获取时间戳和字符串形式的时间的一些方法。

import time

print(time.time()) # 获取时间戳 1577770013.073893 ，表示从1970年1月1日0时0分0秒 到现在经过的秒数

#格式：time.struct_time(tm_year=2019, tm_mon=12, tm_mday=31, tm_hour=5, tm_min=33, tm_sec=17, tm_wday=1, tm_yday=365, tm_isdst=0（夏令时）  )
#print(time.gmtime()) # 输出格式化时间戳后的时间信息 格林威治时间
#print(time.localtime()) #输出格式化时间戳后的时间信息 本地时区

# 输出需要的字符串
#print(time.localtime().tm_year)
#print(time.gmtime(1)) #按照传入时间戳数字，格式化输出时间信息

# 格式化时间对象和字符串之间的转换 第一个参数填写要格式化的样式，第二个参数填: gmtime() 或 localtime()
s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(s)

# 反正将 第一个参数转换成 time.struct_time 格式
# time.struct_time(tm_year=2010, tm_mon=10, tm_mday=10, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=283, tm_isdst=-1)
s = time.strptime('2010-10-10',"%Y-%m-%d")
print(s)

t1 = time.localtime()
t2 = time.mktime(t1) # 将time.struct_timee 对象转换成对应的时间戳，等于 time.time()
print(t2)

# 暂停当前线程，休眠指定时间
time.sleep(1)




