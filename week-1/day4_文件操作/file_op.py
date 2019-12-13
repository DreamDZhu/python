#f = open("yesterday", encoding="utf-8") # 获得文件句柄
# 读模式，只能读，不能写入数据
f = open("yesterday",'r')
# for line in f.readline():
#     print(line)

for i in range(5): # 打印前5行
    print(f.readline())

count = 0
# 打印第5-第10行功能
for index,line in enumerate(f.readlines()): #f.readlines() 可以获取到文件所有信息，并通过\n将信息切割成一个列表
    if index == 9:
        print("======一条分割线======")
        continue
    print(line.split())

#print(f.read())
print("----data-----")
#print(f.read()) # 这次的f.read 不会有任何输出
# 在python 的文件处理中，当我们执行read()后，文件指针会移动到文件尾部。文件操作维护的是文件的指针。所以文件读完一遍以后，再次执行read()。那这个时候指针已经在文件尾部了，所以不会输出任何信息

# 如果要多次读取同一文件，要将光标移动到文件头的位置

# 写模式，只能写文件，不能读，读会报错
w = open('yesterday2','w')
w.write("测试信息\n")
w.write("测试信息")







