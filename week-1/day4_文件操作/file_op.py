#f = open("yesterday", encoding="utf-8") # 获得文件句柄
# 读模式，只能读，不能写入数据
f = open("yesterday",'r')
# for line in f.readline():
#     print(line)

# for i in range(5): # 打印前5行
#     print(f.readline())
#
# count = 0

# 打印第5-第10行功能
for index,line in enumerate(f.readlines()): #f.readlines() 可以获取到文件所有信息，并通过\n将信息切割成一个列表
    if index == 0:
        #print("======一条分割线======")
        break
    print(line.split())

#print(f.read())
# print("----data-----")
#print(f.read()) # 这次的f.read 不会有任何输出
# 在python 的文件处理中，当我们执行read()后，文件指针会移动到文件尾部。文件操作维护的是文件的指针。所以文件读完一遍以后，再次执行read()。那这个时候指针已经在文件尾部了，所以不会输出任何信息

# 如果要多次读取同一文件，要将光标移动到文件头的位置

f = open("yesterday",'r')
print(f.tell()) #打印文件指针位置 ，按照字符数来进行计数
print(f.readline())
print(f.tell())

f.seek(0) #将指针指向文件指定字符位置
print(f.encoding) # 打印文件编码
f.fileno() #返回文件在操作系统中的编号
f.flush()  #强制将缓冲区中的数据，刷新到硬盘中去


# 写模式，只能写文件，不能读，读会报错
# w = open('yesterday2','w')
# w.write("测试信息\n")
# w.write("测试信息")

# 大文件处理 ：当我们读取一个数十G 的文件时，我们不能一次性将文件读取到内存中去，会导致内存溢出 。
# 我们可以一行行读，每读取新行就释放旧的行，直到文件执行结束

# 这样写，就是一行行的读 这时，f就成为了迭代器
# count = 0
# for line in f:
#     count += 1
#     if count == 9:
#         print("---一条分割线---")
#         count += 1
#         continue
#     print(line)






