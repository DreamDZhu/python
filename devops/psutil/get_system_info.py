import psutil # 信息监控模块

"""
cpu

"""
psutil.cpu_times() # 获取CPU 占用时间的详细信息
psutil.cpu_times(percpu=True) # 获取每个CPU占用时间的详细信息

psutil.cpu_count() # 获取逻辑CPU数量
psutil.cpu_count(logical=False) # 获取物理CPU数量

psutil.cpu_percent() # cpu 占比
psutil.cpu_percent(percpu=True) # 每个CPU占比

# 内存
psutil.virtual_memory()
mem = psutil.virtual_memory() # 全内存信息
mem.available # 使用内存 输出的是字节 比较的话需要转换

# 磁盘信息
psutil.disk_partitions() #全磁盘挂载信息
psutil.disk_usage('/') # 磁盘使用情况

psutil.disk_usage('/').total # 磁盘最大容量
psutil.disk_usage('/').used # 磁盘使用量


# 网络信息
psutil.net_io_counters() # 网络读写字节 / 包的个数
psutil.net_if_addrs() # 获取网络接口信息

psutil.net_if_stats() #网络接口状态

# 进程信息

# 获取所有的pid
#for pid in psutil.pids():
#    print(pid, end=',')

# 查找指定进程并输出 输出的字典为 {'name': 'WeChat', 'pid': 742, 'username': 'ddz'}
for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
    print(proc.info)
    #if proc.info['name'].startswith('WeChat'):

