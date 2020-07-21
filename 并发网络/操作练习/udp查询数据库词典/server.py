from socket import *
import pymysql

def get_mean(word):
    db=pymysql.connect(host="localhost",
                       port=3306,
                       user="root",
                       password="123456",
                       database="dict",
                       charset="utf8")
    cur=db.cursor()
    sql="select mean from words where word=%s limit 1;"
    cur.execute(sql,word)
    mean = cur.fetchone()
    cur.close()
    db.close()
    return mean[0]

def main():
    udp_socket = socket(AF_INET, SOCK_DGRAM)
    udp_socket.bind(("0.0.0.0", 60306))
    while 1:
        data, addr = udp_socket.recvfrom(1024)
        msg = data.decode()
        if msg == "##":
            break
        print("收到", addr, "要查询的单词:", msg)
        target_word = [(msg)]
        mean=get_mean(target_word)
        if mean:
            udp_socket.sendto(mean.encode(), addr)
        else:
            udp_socket.sendto("Not Find".encode(), addr)
        print("已响应客户端请求")
    print("服务端退出")
    udp_socket.close()


if __name__ == '__main__':
    main()










