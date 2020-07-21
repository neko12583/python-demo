from socket import *

chat={"有货":'目前还有货哦亲'
      ,"发货":'我们发的是顺丰快递,当天18点前的订单在18点发货,18点后的第二天18点发哦.'
      ,"退货":'老板说只要商品完好无损支持七天无理由退货哦'
     }
tcp_socket=socket()
tcp_socket.bind(("0.0.0.0",60306))
tcp_socket.listen(3)
while 1:
    print("等待连接中...")
    connfd, addr = tcp_socket.accept()
    print("已连接",addr)
    connfd.send("有什么能帮到您?".encode())
    while 1:
        data=connfd.recv(1024)
        if not data:
            break
        client_msg=data.decode()
        print("收到客户端信息：",client_msg)
        mark=1
        for key in chat:
            if key in client_msg:
                msg=chat[key]
                connfd.send(msg.encode())
                mark=0
        if mark==1:
            connfd.send("小白不太明白您的意思.".encode())

