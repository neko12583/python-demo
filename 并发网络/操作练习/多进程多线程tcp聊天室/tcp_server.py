from socket import *
from multiprocessing import Process
from signal import *

HOST = "0.0.0.0"
PORT = 60306
ADDR = (HOST, PORT)

def do_userlist():
    f=open("user","r")
    data=f.read()
    userlist=list([data])
    return userlist

def do_login(connfd, name):
    user = do_userlist()
    for i in user:
        if name == i[0] or "管理" in name:
            connfd.send(b"Fail")
            return
        else:
            connfd.send(b"OK")
            msg = "欢迎 %s 进入聊天室" % name
            for i in user:
                client=i[1]
                eval(client).send(msg.encode())
            # user[name] = connfd
            f=open("user","a")
            info="[%s,%s]" %name,connfd
            f.write(info)
            f.close()

def do_chat(name,content):
    print(name,"发送了消息:",content)
    msg = "%s : %s" % (name, content)
    user=do_userlist()
    for i in user:
        # 出去本人
        client = i[1]
        if i[0] != name:
            print("发送信息给其他用户")
            eval(client).send(msg.encode())

def do_quit(name):
    print(name,"退出聊天室")
    user = do_userlist()
    for i in user:
        if i[0]==name:
            del i
    msg = "%s 退出聊天室" % name

    for i in user:
        client = i[1]
        eval(client).send(msg.encode())

def do_request(connfd):
    while True:
        data = connfd.recv(1024)
        tmp = data.decode().split(" ", 2)
        if tmp[0] == 'L':
            do_login(connfd, tmp[1])
        elif tmp[0] == 'C':
            do_chat(tmp[1], tmp[2])
        elif tmp[0] == 'Q' or data=="":
            do_quit(tmp[1])

def main():
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)

    signal(SIGCHLD, SIG_IGN)

    while 1:
        connfd,addr=sock.accept()
        p = Process(target=do_request, args=(connfd,))
        p.daemon = True
        p.start()

    # while True:
    #     content = input("管理员消息:")
    #     if content == 'quit':
    #         break
    #     msg = "C 管理员消息 "+content
    #     connfd.send(msg.encode())

if __name__ == '__main__':
    main()



