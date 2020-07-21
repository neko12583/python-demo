"""
  1. 主要功能 ：
     【1】 接收客户端（浏览器）请求
     【2】 解析客户端发送的请求
     【3】 根据请求组织数据内容
     【4】 将数据内容形成http响应格式返回给浏览器
  2. 特点 ：
     【1】 采用IO并发，可以满足多个客户端同时发起请求情况
     【2】 通过类接口形式进行功能封装
            1 从功能使用方法的角度分析
            2 借鉴曾经接触过的Python类
                scoket()
                    实例化对象->用户可以自己选择套接字种类
                    不同对象能够调用的方法不一样
                Process()
                    实例化对象->功能单一
                    固定的流程实现指定功能：process()->start()->join()
                    用户可选择：使用对象做什么
     【3】 做基本的请求解析，根据具体请求返回具体内容，同时处理客户端的非网页请求行为
设计思想：
    * 站在用户角度思考
    * 能够为用户做好的 尽量做
    * 不能代替使用者决定的，提供接口（参数），让用户方便传递或者调用不同的方法做选择
编写步骤：
    * 先搭建框架
        使用流程
        那些量需要用户决定，如何传递(看需求)
            哪组网页
            服务端地址
"""
from socket import *
from select import select
import re


class WebServer:
    def __init__(self, host="0.0.0.0", port=80, html=None):
        self.host = host
        self.port = port
        self.html = html
        self.__rlist = []
        self.__wlist = []
        self.__xlist = []
        self.create_socket()
        self.bind()

    def create_socket(self):
        self.sock = socket()
        self.sock.setblocking(False)

    def bind(self):
        self.address = (self.host, self.port)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sock.bind(self.address)

    def start(self):
        self.sock.listen(5)
        self.__rlist.append(self.sock)
        print("Listen the port", self.port)
        while 1:
            rs, ws, xs = select(self.__rlist, self.__wlist, self.__xlist)
            for r in rs:
                if r is self.sock:
                    connfd, addr = self.sock.accept()
                    connfd.setblocking(False)
                    self.__rlist.append(connfd)
                else:
                    try:
                        self.handle(r)
                    except:
                        self.__rlist.remove(r)
                        r.close()

    def handle(self, connfd):
        request = connfd.recv(1024 * 10).decode()
        pattern = "[A-Z]+\s+(?P<info>/\S*)"
        result = re.match(pattern, request)
        if result:
            info = result.group("info")
            print("请求内容：", info)
            self.send_response(connfd, info)
        else:
            self.__rlist.remove(connfd)
            connfd.close()

    def send_response(self, connfd, info):
        if info == "/":
            filename = self.html + "/index.html"
        else:
            filename = self.html + info
        try:
            fd = open(filename, "rb")
        except:
            response = "HTTP/1.1 404 Not Found\r\n"
            response +="Content-Type:text/html\r\n"
            response +="\r\n"
            response +="<h1>Not Find<h1>"
            response = response.encode()
        else:
            data = fd.read()
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "Content-Length:%d\r\n" % len(data)
            response += "\r\n"
            response = response.encode() + data
        finally:
            connfd.send(response)

if __name__ == '__main__':
    httpd = WebServer(host="0.0.0.0", port=8000, html="./static")
    httpd.start()

# Listen the port 8000
# 请求内容: /
# 请求内容: /images/wrap.gif
# 请求内容: /images/header.jpg
# 请求内容: /images/nav.gif
# 请求内容: /images/left-tab.gif
# 请求内容: /images/right-tab.gif
# 请求内容: /images/search_nav.gif
# 请求内容: /images/footer-bottom.gif