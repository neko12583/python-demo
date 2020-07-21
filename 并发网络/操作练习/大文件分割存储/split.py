"""
大文件分割（词典）（按指定行数分割成若干份）
"""
def write_file(file_name,msg):
    fw = open(file_name, "ab")
    fw.write(msg)

def split_file(rows,target_file):
    fr=open(target_file,"rb")
    row = 0
    i = 1
    while 1:
        msg = fr.readline()
        if not msg:
            break

        if str(row)!=rows:
            file_name=target_file+str(i)
            write_file(file_name,msg)
            row += 1
        else:
            i+=1
            row=1
            file_name = target_file + str(i)
            write_file(file_name, msg)

file=input("要分割的文件：")
rows=input("每次分割的行数：")
split_file(rows,file)

"""
大文件分割（词典）（分成两半）
"""
from multiprocessing import Process
import os

filename = input("File:")
size = os.path.getsize(filename) # 获取文件大小
file = filename.split('/')[-1] # 提取出真正的文件名称

# 复制上半部分
def top():
    # 因为os.path.getsize()得到的是字节码数，read(n)读到的是字符，
    # 所以一定要用二进制形式打开文件才能得到想要的一半。
    fr = open(filename,'rb')
    fw = open('top-'+file,'wb')
    n = size // 2
    # fw.write(fr.read(n))
    while n >= 1024:
        fw.write(fr.read(1024))
        n -= 1024
    else:
        fw.write(fr.read(n))
    fr.close()
    fw.close()

# 复制下半部分
def bot():
    fr = open(filename,'rb')
    fw = open('bot-'+file,'wb')
    fr.seek(size//2,0) # 将文件偏移量移动到中间
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)

    fr.close()
    fw.close()

jobs = []
# 循环创建进程
for i in [top,bot]:
    p = Process(target=i)
    jobs.append(p)
    p.start()

for i in jobs:
    i.join()