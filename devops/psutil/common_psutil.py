import os
import psutil
import signal


# 根据名称查找进程相关信息 不区分大小写
def find_procs_by_name(name):
    name = name.upper()
    ls = []
    for proc in psutil.process_iter(attrs=['name']):
        if proc.info['name'].upper() == name:
            ls.append(proc)
    return ls


# 名称与进程信息任一项匹配就输出进程信息
def find_procs_by_name_all(name):
    ls = []
    for proc in psutil.process_iter(attrs=['name', 'exe', 'cmdline']):
        if name == proc.info['name'] or \
                name == proc.info['exe'] and os.path.basename(p.info['exe']) or \
                name == proc.info['cmdline'] and proc.info['cmdline'][0]:
            ls.append(proc)
    return ls


# 根据传入的pid杀掉对应进程树
def kill_proc_tree(pid, sig=signal.SIGTERM, include_parent=True, timeout=None, on_terminate=None):
    if pid == os.getpid():
        raise RuntimeError("Do Not Kill Myself")
    parent = psutil.Process(pid)
    # recursive=True 表示递归获取子进程的子进程 False 的话表示只获取一层子进程
    children = parent.children(recursive=True)
    if include_parent:
        children.append(parent)
    for p in children:
        p.send_signal(sig)
    gone, alive = psutil.wait_procs(children, timeout=timeout, callback=on_terminate)

    return gone, alive


#print(find_procs_by_name("wechat"))
