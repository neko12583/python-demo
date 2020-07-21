from socket import *

udp_socket=socket(AF_INET,SOCK_DGRAM)
addr=("127.0.0.1",60306)

while 1:
    msg=input("请输入内容：")
    udp_socket.sendto(msg.encode(),addr)
    if msg=="##":
        print("客户端退出")
        break
    data,addr1=udp_socket.recvfrom(1024)
    print("从服务器接收到：",data.decode())
udp_socket.close()




