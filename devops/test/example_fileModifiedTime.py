# encoding=utf-8

"""
根据时间匹配路径的文件
可以用来批量删除文件
"""

import os
import datetime

path = "/Users/ddz/Downloads"
TIME_FORM = "%Y-%m-%d %H:%M:%S"
print(f"当前时间: {datetime.datetime.now().strftime(TIME_FORM)}")

day = 10
hour = 10
minute = 10
second = 10

# 获取当前时间
now = datetime.datetime.now()
for root, dirs, files in os.walk(path):
    for file in files:
        # 获取文件的绝对路径
        absPathFile = os.path.join(root, file)
        # 获取修改时间并转化为datetime
        modifiedTime = datetime.datetime.fromtimestamp(os.path.getmtime(absPathFile))
        # 获取时间差
        diffTime = now - modifiedTime
        # 转换打印信息
        diffTime_day = diffTime.days
        diffTime_hour = diffTime.seconds//3600
        diffTime_minute = (diffTime.seconds % 3600)//60

        if diffTime_day < day:
            print(
                f"{absPathFile}".ljust(25),
                f"修改时间[{modifiedTime.strftime(TIME_FORM)}] "
                f"距今[{diffTime_day:3d}天"
                f"{diffTime_hour:2d}时"
                f"{diffTime_minute:2d}分]"
            )

