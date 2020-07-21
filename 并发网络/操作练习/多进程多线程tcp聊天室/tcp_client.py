from socket import *
from multiprocessing import Process
from signal import *
import sys

ADDR = ('176.140.6.132', 60306)

def recv_msg(connfd):
    while True:
        data = connfd.recv(4096)
        if connfd=="":
            sys.exit("服务端已退出")
        msg = "\n"+data.decode()+"\n发言:"
        print(msg,end="")

def send_msg(connfd,name):
    while True:
        try:
            content = input("发言(输入'quit'或直接回车退出):")
        except:
            content = "quit"

        if content == "quit":
            msg = "Q " + name
            connfd.send(msg.encode())
            sys.exit("您已退出聊天室")  # 父进程退出
        msg = "C %s %s" % (name, content)
        connfd.send(msg.encode())

def control(connfd):
    while True:
        name = input("Name:")
        msg = "L " + name
        connfd.send(msg.encode())
        result = connfd.recv(1024)
        if result.decode() == "OK":
            print("进入聊天室")
            return name
        else:
            print("该用户已存在")

def main():
    connfd = socket()
    connfd.connect(ADDR)

    name=control(connfd)

    signal(SIGCHLD,SIG_IGN)

    p = Process(target=recv_msg, args=(connfd,))
    p.daemon = True
    p.start()

    send_msg(connfd, name)

if __name__ == '__main__':
    main()