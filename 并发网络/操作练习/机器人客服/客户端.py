from socket import *

tcp_socket=socket()
tcp_socket.connect(("0.0.0.0",60306))
data=tcp_socket.recv(1024)
print("从客户端收到：",data.decode())
while 1:
    msg=input(">>")
    if not msg:
        break
    tcp_socket.send(msg.encode())
    data=tcp_socket.recv(1024)
    print("从客户端收到：",data.decode())

print("客户端已退出")
tcp_socket.close()