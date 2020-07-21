并发网络编程
==========================

| Tedu Python 教学部 |
| --- |
| Author：吕泽|

-----------

[TOC]

## 1. 网络编程

### 1.1 网络基础知识



#### 1.1.1 什么是网络

* 什么是网络 : 计算机网络功能主要包括实现资源共享，实现数据信息的快速传递。

  ![](./img/1.jpg)

  ![](./img/2.png)

#### 1.1.2 网络通信标准

* 面临问题

  1. 不同的国家和公司都建立自己的通信标准不利于网络互连
  2. 多种标准并行情况下不利于技术的发展融合

  ![](./img/4.jpg)



* OSI 7层模型

  ![](./img/5.jpg)

  * 好处

    1. 建立了统一的通信标准

    2. 降低开发难度，每层功能明确，各司其职

    3. 七层模型实际规定了每一层的任务，该完成什么事情

* TCP/IP模型

  * 七层模型过于理想，结构细节太复杂
  * 在工程中应用实践难度大
  * 实际工作中以TCP/IP模型为工作标准流程

  ![](./img/6.jpg)
  ​

  > Telnet协议是Internet远程登录服务的标准协议和主要方式。是常用的远程控制Web服务器的方法。
  >
  > FTP是文件传输协议。
  >
  > SMTP是一种提供可靠且有效的电子邮件传输的协议。SMTP是建立在FTP文件传输服务上的一种邮件服务，主要用于系统之间的邮件信息传递，并提供有关来信的通知。
  >
  > DNS域名系统是互联网的一项服务。它作为将域名和IP地址相互映射的一个分布式数据库，能够使人更方便地访问互联网。
  >
  > HTTP是一个简单的请求-响应协议，它通常运行在TCP之上。它指定了客户端可能发送给服务器什么样的消息以及得到什么样的响应。
  >
  > IP是网际互连协议,对上可载送传输层各种协议的信息，例如TCP、UDP等；对下可将IP信息包放到链路层，通过以太网、令牌环网络等各种技术来传送。
  >
  > ARP地址解析协议是根据IP地址获取物理地址的一个TCP/IP协议。
  >
  > RARP反向地址转换协议,允许局域网的物理机器从网关服务器的 ARP 表或者缓存上请求其 IP 地址。
  >
  > ICMP控制报文协议,用于在IP主机、路由器之间传递控制消息。控制消息是指网络通不通、主机是否可达、路由是否可用等网络本身的消息。

  

* 网络协议

  * 什么是网络协议：在网络数据传输中，都遵循的执行规则。

  * 网络协议实际上规定了每一层在完成自己的任务时应该遵循什么规范。


* 需要应用工程师做的工作 ： 编写应用工功能，明确对方地址，选择传输服务。

    ![](./img/7.jpg)

#### 1.1.3  通信地址


* IP地址

  * IP地址 ： 即在网络中标识一台计算机的地址编号。

  * IP地址分类

    * IPv4 ： 192.168.1.5 
    * IPv6 ：fe80::80a:76cf:ab11:2d73

  * IPv4 特点

    * 分为4个部分，每部分是一个整数，取值分为0-255

  * IPv6 特点（了解）

    * 分为8个部分，每部分4个16进制数，如果出现连续的数字 0 则可以用 ：：省略中间的0

  * IP地址相关命令

    * ifconfig : 查看Linux系统下计算机的IP地址

      ![](./img/7.png)

    * ping  [ip]：查看计算机的连通性 

      ![](./img/8.png)

  * 公网IP和内网IP

    * 公网IP指的是连接到互联网上的公共IP地址，大家都可以访问。（将来进公司，公司会申请公网IP作为网络项目的被访问地址）
    * 内网IP指的是一个局域网络范围内由网络设备分配的IP地址。

* 端口号

  * 端口：网络地址的一部分，在一台计算机上，每个网络程序对应一个端口。

    ![](./img/3.png)

  * 端口号特点

    * 取值范围： 0 —— 65535 的整数
    * 一台计算机上的网络应用所使用的端口不会重复
    * 通常 0——1023 的端口会被一些有名的程序或者系统服务占用，个人一般使用 > 1024的端口

#### 1.1.4 服务端与客户端

* 服务端（Server）：服务端是为客户端服务的，服务的内容诸如向客户端提供资源，保存客户端数据，处理客户端请求等。

* 客户端（Client） ：也称为用户端，是指与服务端相对应，为客户提供一定应用功能的程序，我们平时使用的手机或者电脑上的程序基本都是客户端程序。

  ![](./img/10.jpg)



### 1.2 UDP 传输方法

#### 1.2.1 套接字简介

> 一种无连接的传输层协议，提供面向事务的简单不可靠信息传送服务。可靠性由上层应用实现，所以要实现udp可靠性传输，必须通过应用层来实现和控制。
>
> UDP它不属于连接型协议，因而具有资源消耗小，处理速度快的优点，所以通常音频、视频和普通数据在传送时使用UDP较多，因为它们即使偶尔丢失一两个数据包，也不会对接收结果产生太大影响。

* 套接字(Socket) ： 实现网络编程进行数据传输的一种技术手段,网络上各种各样的网络服务大多都是基于 Socket 来完成通信的。

  ![](./img/9.jpg)

* Python套接字编程模块：import  socket

#### 1.2.3  UDP套接字编程

```
"""
套接字基础函数示例
"""
import socket

# 创建一个udp套接字
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 客户端只能与服务端在同一主机上，使用("127.0.0.1",8888)访问服务端
udp_socket.bind(("127.0.0.1",8888))
udp_socket.bind(("localhost",8888))

# 客户端能够在任何主机上，使用("172.40.91.178",8888)访问服务端
udp_socket.bind(("172.40.91.178",8888))

# 客户端能够在任何主机上，如果在其他主机("172.40.91.178",8888)访问服务端
# 如果与服务端在同一主机可以使用("127.0.0.1",8888)或者("172.40.91.178",8888)
udp_socket.bind(("0.0.0.0",8888))
udp_socket.bind(("",8888))
```

```
"""
udp_client.py  udp套接字流程客户端演示
重点代码
"""

from socket import *

# 访问服务器的地址
ADDR = ('172.40.91.178',8888)

# 创建udp套接字
udp_socket = socket(AF_INET,SOCK_DGRAM)

# 循环发送接收消息
while True:
    # 发送消息
    msg = input(">>")
    # 结束循环
    if not msg:
        break
    udp_socket.sendto(msg.encode(),ADDR)
    # 接收消息
    msg,addr = udp_socket.recvfrom(1000)
    print("从服务端收到:",msg.decode())

# 关闭套接字
udp_socket.close()


```

```
"""
udp_server.py  udp套接字服务端流程
重点代码
"""
from socket import *

# 创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 绑定地址
sockfd.bind(("0.0.0.0",8888))

while True:
    # 接收消息
    data,addr = sockfd.recvfrom(1024)
    print(addr,"接收到:",data.decode()) # data是字节串
    # 发送消息
    n = sockfd.sendto(b"Thanks",addr) # 发送字节串
    print("发送了%d bytes"%n)

# 关闭套接字
sockfd.close()



```



* 创建套接字

```python
sockfd=socket.socket(socket_family,socket_type,proto=0)
功能：创建套接字
参数：socket_family  网络地址类型 AF_INET表示ipv4  #ipv6：AF_INET6
	 socket_type  套接字类型 SOCK_DGRAM 表示udp套接字 （也叫数据报套接字） 
	 proto  通常为0  选择子协议
返回值： 套接字对象
```


* 绑定地址
  * 本地地址 ： 'localhost' , '127.0.0.1'
  * 网络地址 ： '172.40.91.185' （通过ifconfig查看）
  * 自动获取地址： '0.0.0.0'

![](img/address.png)

```python
sockfd.bind(addr)
功能： 绑定本机网络地址
参数： 二元元组 (ip,port)  ('0.0.0.0',8888)
```

* 消息收发

```python		    
data,addr = sockfd.recvfrom(buffersize)
功能： 接收UDP消息
参数： 每次最多接收多少字节
返回值： data  接收到的内容
	    addr  消息发送方地址

n = sockfd.sendto(data,addr)
功能： 发送UDP消息
参数： data  发送的内容 bytes格式
	  addr  目标地址
返回值：发送的字节数
```

* 关闭套接字

```python
sockfd.close()
功能：关闭套接字
```



* 服务端客户端流程

  ![](./img/11.png)



#### 1.2.4  UDP套接字特点

* 可能会出现数据丢失的情况
* 传输过程简单，实现容易
* 数据以数据包形式表达传输
* 数据传输效率较高



### 1.3 TCP 传输方法

```
"""
希望监听套接字同时连接着多个客户端，能同时和多个客户端交互
重点代码
"""

from socket import *

# 创建TCP套接字 （不写参数默认也是tcp）
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(('0.0.0.0',8888))

# 设置监听
tcp_socket.listen(3)

# 等待客户端连接 (阻塞函数)
while True:
    print("Waiting for connect ....")
    connfd,addr = tcp_socket.accept()
    print("Connect from",addr)

    # 收发消息
    data = connfd.recv(1024)
    print("收到:",data.decode())
    connfd.send(b"Thanks")

    connfd.close()

# 关闭
tcp_socket.close()
```

```
from socket import *

while True:
    # 发送接收消息
    msg = input(">>")
    if not msg:
        break

    # 创建tcp套接字
    tcp_socket = socket()
    # 发起连接
    tcp_socket.connect(("127.0.0.1",8888))
    tcp_socket.send(msg.encode())
    data = tcp_socket.recv(1024)
    print("从服务器收到:",data.decode())
    # 关闭套接字
    tcp_socket.close()
```





#### 1.3.1 TCP传输特点



* 面向连接的传输服务
  * 传输特征 ： 提供了可靠的数据传输，可靠性指数据传输过程中无丢失，无失序，无差错，无重复。
  * 可靠性保障机制（都是操作系统网络服务自动帮应用完成的）： 
    * 在通信前需要建立数据连接
    * 确认应答机制
    * 通信结束要正常断开连接

* 三次握手（建立连接）
  * 客户端向服务器发送消息报文请求连接
  * 服务器收到请求后，回复报文确定可以连接
  * 客户端收到回复，发送最终报文连接建立

![](./img/1_%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B.png)
​					

* 四次挥手（断开连接）
  * 主动方发送报文请求断开连接
  * 被动方收到请求后，立即回复，表示准备断开
  * 被动方准备就绪，再次发送报文表示可以断开
  * 主动方收到确定，发送最终报文完成断开

![](./img/1_%E5%9B%9B%E6%AC%A1%E6%8C%A5%E6%89%8B.png)

#### 1.3.2 TCP服务端



![](./img/1_TCP_Server.png)



- 创建套接字

```python
sockfd=socket.socket(socket_family,socket_type,proto=0)
功能：创建套接字
参数：socket_family  网络地址类型 AF_INET表示ipv4
	 socket_type  套接字类型 SOCK_STREAM 表示tcp套接字 （也叫流式套接字） 
	 proto  通常为0  选择子协议
返回值： 套接字对象
```

- 绑定地址 （与udp套接字相同）



* 设置监听

```python
sockfd.listen(n)
功能 ： 将套接字设置为监听套接字，确定监听队列大小
参数 ： 监听队列大小
```

![](./img/11.jpg)

* 处理客户端连接请求 

```python
connfd,addr = sockfd.accept()
功能： 阻塞等待处理客户端请求
返回值： connfd  客户端连接套接字(相当于连接对象)
        addr  连接的客户端地址
```

* 消息收发

```python
data = connfd.recv(buffersize)
功能 : 接受客户端消息
参数 ：每次最多接收消息的大小
返回值： 接收到的内容

n = connfd.send(data)
功能 : 发送消息
参数 ：要发送的内容  bytes格式
返回值： 发送的字节数
```

6. 关闭套接字 (与udp套接字相同)



#### 1.3.3 TCP客户端 



![](./img/1_TCP_Client.png)

* 创建TCP套接字
* 请求连接

```python
sockfd.connect(server_addr)
功能：连接服务器
参数：元组  服务器地址
```

* 收发消息

> 注意： 防止两端都阻塞，recv send要配合

* 关闭套接字

![](./img/12.png)





#### 1.3.4 TCP套接字细节

* tcp连接中当一端退出，另一端如果阻塞在recv，此时recv会立即返回一个空字串。

* tcp连接中如果一端已经不存在，仍然试图通过send向其发送数据则会产生BrokenPipeError

* 一个服务端可以同时连接多个客户端，也能够重复被连接

* tcp粘包问题

  * 产生原因

    * 为了解决数据再传输过程中可能产生的速度不协调问题，操作系统设置了缓冲区
    * 实际网络工作过程比较复杂，导致消息收发速度不一致
    * tcp以字节流方式进行数据传输，在接收时不区分消息边界

    ![](./img/13.jpg)

  * 带来的影响

    * 如果每次发送内容是一个独立的含义，需要接收端独立解析此时粘包会有影响。

  * 处理方法

    * 人为的添加消息边界，用作消息之间的分割
    * 控制发送的速度

> ```
> sock.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) 实现端口复用
> ```

#### 1.3.5 TCP与UDP对比

* 传输特征
  * TCP提供可靠的数据传输，但是UDP则不保证传输的可靠性（UDP的可靠性可以在应用层实现）
  * TCP传输数据处理为字节流，而UDP处理为数据包形式
  * TCP传输需要建立连接才能进行数据传，效率相对较低，UDP比较自由，无需连接，效率较高

* 套接字编程区别
  * 创建的套接字类型不同
  * tcp套接字会有粘包，udp套接字有消息边界不会粘包
  * tcp套接字依赖listen accept建立连接（使用连接对象）才能收发消息，udp套接字则不需要
  * tcp套接字使用send，recv收发消息，udp套接字使用sendto，recvfrom
* 使用场景
  * tcp更适合对准确性要求高，传输数据较大的场景
    * 文件传输：如下载电影，访问网页，上传照片
    * 邮件收发
    * 点对点数据传输：如点对点聊天，登录请求，远程访问，发红包
  * udp更适合对可靠性要求没有那么高，传输方式比较自由的场景
    * 视频流的传输： 如直播，视频聊天
    * 广播：如网络广播，群发消息
    * 实时传输：如游戏画面
  * 在一个大型的项目中，可能既涉及到TCP网络又有UDP网络



### 1.4 数据传输过程



#### 1.4.1 传输流程

* 发送端由应用程序发送消息，逐层添加首部信息，最终在物理层发送消息包。
* 发送的消息经过多个节点（交换机，路由器）传输，最终到达目标主机。
* 目标主机由物理层逐层解析首部消息包，最终到应用程序呈现消息。

![](./img/14.png)



#### 1.4.2 TCP协议首部（了解）

![](./img/1_tcp数据包.png)



* 源端口和目的端口 各占2个字节，分别写入源端口和目的端口。

* 序号 占4字节。TCP是面向字节流的。在一个TCP连接中传送的字节流中的每一个字节都按顺序编号。例如，一报文段的序号是301，而接待的数据共有100字节。这就表明本报文段的数据的第一个字节的序号是301，最后一个字节的序号是400。

* 确认号 占4字节，是期望收到对方下一个报文段的第一个数据字节的序号。例如，B正确收到了A发送过来的一个报文段，其序号字段值是501，而数据长度是200字节（序号501~700），这表明B正确收到了A发送的到序号700为止的数据。因此，B期望收到A的下一个数据序号是701，于是B在发送给A的确认报文段中把确认号置为701。

* 确认ACK（ACKnowledgment） 仅当ACK = 1时确认号字段才有效，当ACK = 0时确认号无效。TCP规定，在连接建立后所有的传送的报文段都必须把ACK置为1。

* 同步SYN（SYNchronization） 在连接建立时用来同步序号。当SYN=1而ACK=0时，表明这是一个连接请求报文段。对方若同意建立连接，则应在响应的报文段中使SYN=1和ACK=1，因此SYN置为1就表示这是一个连接请求或连接接受报文。

* 终止FIN（FINis，意思是“完”“终”） 用来释放一个连接。当FIN=1时，表明此报文段的发送发的数据已发送完毕，并要求释放运输连接。





## 2. 多任务编程

### 2.1 多任务概述

* 多任务

   即操作系统中可以同时运行多个任务。比如我们可以同时挂着qq，听音乐，同时上网浏览网页。这是我们看得到的任务，在系统中还有很多系统任务在执行,现在的操作系统基本都是多任务操作系统，具备运行多任务的能力。

  

  ![](./img/13.png)

  



* 计算机原理 

  * CPU：计算机硬件的核心部件，用于对任务进行执行运算。

    ![](./img/14.jpg)

  * 操作系统调用CPU执行任务

    ![](./img/15.png)

  * cpu轮训机制 ： cpu都在多个任务之间快速的切换执行，切换速度在微秒级别，其实cpu同时只执行一个任务，但是因为切换太快了，从应用层看好像所有任务同时在执行。

    ![](./img/16.gif)

  * 多核CPU：现在的计算机一般都是多核CPU，比如四核，八核，我们可以理解为由多个单核CPU的集合。这时候在执行任务时就有了选择，可以将多个任务分配给某一个cpu核心，也可以将多个任务分配给多个cpu核心，操作系统会自动根据任务的复杂程度选择最优的分配方案。

    * 并发 ： 多个任务如果被分配给了一个cpu内核，那么这多个任务之间就是并发关系，并发关系的多个任务之间并不是真正的‘"同时"。
    * 并行 ： 多个任务如果被分配给了不同的cpu内核，那么这多个任务之间执行时就是并行关系，并行关系的多个任务时真正的“同时”执行。

* 什么是多任务编程

  多任务编程即一个程序中编写多个任务，在程序运行时让这多个任务一起运行，而不是一个一个的顺次执行。

  比如微信视频聊天，这时候在微信运行过程中既用到了视频任务也用到了音频任务，甚至同时还能发消息。这就是典型的多任务。而实际的开发过程中这样的情况比比皆是。

  ![](./img/12.jpg)



  * 实现多任务编程的方法 ： **多进程编程，多线程编程**

* 多任务意义

  * 提高了任务之间的配合，可以根据运行情况进行任务创建。

    比如： 你也不知道用户在微信使用中是否会进行视频聊天，总不能提前启动起来吧，这是需要根据用户的行为启动新任务。

  * 充分利用计算机资源，提高了任务的执行效率。

    * 在任务中无阻塞时只有并行状态才能提高效率

    ![](./img/17.jpg)

    

    * 在任务中有阻塞时并行并发都能提高效率

    ![](./img/18.jpg)



### 2.2 进程（Process）

> 对操作系统而言，线程是最小的执行单元，进程是最小的资源管理单元。无论是进程还是线程，都是由操作系统所管理的。
>
> 进程是应用程序的启动实例，进程拥有代码和打开的文件资源、数据资源、独立的内存空间。
>
> 线程从属于进程，是程序的实际执行者，一个进程至少包含一个主线程，也可以有更多的子线程，线程拥有自己的栈空间。
>
> 协程（Coroutines）是一种比线程更加轻量级的存在，正如一个进程可以拥有多个线程一样，一个线程可以拥有多个协程，协程不是被操作系统内核所管理的，而是完全由程序所控制，也就是在用户态执行。这样带来的好处是性能大幅度的提升，因为不会像线程切换那样消耗资源。

```
"""
练习1 ： 模拟售票系统
模拟会场的出票系统，现有入场票 500张 记为 T1--T500
由于涉及座位排布 票必须按照顺序卖出
有10个窗口同时买票 （w1--w10），每个窗口买一张票需要0.1秒 sleep(0.1)
按照上面的描述 使用10个线程模拟10个窗口，完成售票过程

思路 ： 先将500张票生成放入到一个列表中，卖出的票打印一下即刻

       w1 ---- T128
"""

from threading import Thread
from time import sleep

ticket = ["T%d" % x for x in range(1, 501)]

# 模拟每个窗口的买票过程
def sell(w):
    while ticket:
        print("%s 窗口卖出：%s"%(w,ticket.pop(0)))
        sleep(0.1)

jobs = []
for i in range(1,11):
    t = Thread(target=sell,args=("w%d"%i,))
    jobs.append(t)
    t.start()

[i.join() for i in jobs]
```



#### 2.2.1 进程概述

* 定义： 程序在计算机中的一次执行过程。

  - 程序是一个可执行的文件，是静态的占有磁盘。

  - 进程是一个动态的过程描述，占有计算机运行资源，有一定的生命周期。

    ![](./img/19.jpg)

* 进程状态

   * 三态  
       	  就绪态 ： 进程具备执行条件，等待系统调度分配cpu资源 
      
       	  运行态 ： 进程占有cpu正在运行 
      
       	  等待态 ： 进程阻塞等待，此时会让出cpu
      
      ![](./img/4_3%E6%80%81.png)
      
   * 五态 (在三态基础上增加新建和终止)
     
       	  新建 ： 创建一个进程，获取资源的过程
      
       	  终止 ： 进程结束，释放资源的过程
      
      ![](./img/4_5%E6%80%81.png)



* 进程命令

  * 查看进程信息

    ```shell
    ps -aux
    ```

    ![](./img/20.png)

    * USER ： 进程的创建者
    * PID  :  操作系统分配给进程的编号,大于0的整数，系统中每个进程的PID都不重复。PID也是重要的区分进程的标志。
    * %CPU,%MEM : 占有的CPU和内存
    * STAT ： 进程状态信息，S I 表示阻塞状态  ，R 表示就绪状态或者运行状态
    * START : 进程启动时间
    * COMMAND : 通过什么程序启动的进程

  

  * 进程树形结构

    ```shell
    pstree
    ```

    * 父子进程：在Linux操作系统中，进程形成树形关系，任务上一级进程是下一级的父进程，下一级进程是上一级的子进程。

#### 2.2.2 多进程编程

```
"""
Process 模块创建进程演示
1.将需要新进程执行的事件封装为函数
2.通过模块的Process类创建进程对象，关联函数
3.通过进程对象调用start启动进程
4.通过进程对象调用join回收进程资源
"""

import multiprocessing
from time import sleep

a = 1

# 进程执行函数
def fun():
    print("开始运行一个进程")
    global a
    print("a =",a)
    a = 1000
    sleep(2)
    print("一个进程执行结束了")

# 创建进程对象
p = multiprocessing.Process(target=fun)

# 启动进程  进程诞生， 自动的运行fun 将其作为新进程的执行内容
p.start()

print("原进程干点事")
sleep(3)
print("父进程干完了")

# 回收进程 阻塞等待新进程结束
p.join()

print("a:",a)

```



```
"""
进程对象属性
"""

from multiprocessing import Process
import time
import os,sys

def fun():
    for i in range(3):
        print(time.ctime())
        time.sleep(2)


# 创建进程对象
p = Process(target=fun,name="Tarena")

# 该子进程会随父进程的退出而结束
p.daemon = True

p.start()

print("Name:",p.name)
print("PID:",p.pid)
print("is alive:",p.is_alive())


```

```
"""
包含参数的进程函数 示例
"""
from multiprocessing import Process
from time import sleep

# 带参数的进程函数
def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

# 位置传参
# p = Process(target=worker,args=(2,"Tom"))

# 关键字传参
p = Process(target=worker,args=(2,),kwargs={"name":"Lily"})


p.start()
p.join(3)
print("=====================================")
```

```
"""
进程相关函数演示
创建多个子进程
"""

from multiprocessing import Process
from time import sleep
import os,sys

def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(),"---",os.getpid())

def th2():
    sleep(2)
    sys.exit("睡觉进程退出") # 结束进程
    print("睡觉")
    print(os.getppid(),"---",os.getpid())

def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(),"---",os.getpid())

things = [th1,th2,th3]
jobs = []
# 每次循环创建一个进程
for th in things:
    p = Process(target=th)
    jobs.append(p) # 将三个进程对象都放入列表
    p.start()

# 统一回收
for i in jobs:
    i.join()


```



* 使用模块 ： multiprocessing

* 创建流程
  【1】 将需要新进程执行的事件封装为函数

  【2】 通过模块的Process类创建进程对象，关联函数

  【3】 可以通过进程对象设置进程信息及属性

  【4】 通过进程对象调用start启动进程

  【5】 通过进程对象调用join回收进程资源

* 主要类和函数使用

```python
Process()
功能 ： 创建进程对象
参数 ： target 绑定要执行的目标函数 
	   args 元组，用于给target函数位置传参
	   kwargs 字典，给target函数键值传参
```

```python
p.start()
功能 ： 启动进程
```

> 注意 : 启动进程此时target绑定函数开始执行，该函数作为新进程执行内容，此时进程真正被创建

```python
p.join([timeout])
功能：阻塞等待回收进程
参数：超时时间
```



* 进程执行现象理解 （难点）
  * 新的进程是原有进程的子进程，子进程复制父进程全部内存空间代码段，一个进程可以创建多个子进程。
  * 子进程只执行指定的函数，其余内容均是父进程执行内容，但是子进程也拥有其他父进程资源。
  * 各个进程在执行上互不影响，也没有先后顺序关系。
  * 进程创建后，各个进程空间独立，相互没有影响。
  * multiprocessing 创建的子进程中无法使用标准输入（input）。



* 进程对象属性
  * p.name  进程名称
  * p.pid   对应子进程的PID号
  * p.is_alive() 查看子进程是否在生命周期
  * p.daemon  设置父子进程的退出关系  
    * 如果设置为True则该子进程会随父进程的退出而结束
    * 要求必须在start()前设置
    * 如果daemon设置成True 通常就不会使用 join()



#### 2.2.3 进程处理细节



* 进程相关函数

```
os.getpid()
功能： 获取一个进程的PID值
返回值： 返回当前进程的PID 
```

```
os.getppid()
功能： 获取父进程的PID号
返回值： 返回父进程PID
```

```
sys.exit(info)
功能：退出进程
参数：字符串 表示退出时打印内容
```



##### 孤儿和僵尸

```
"""
僵尸进程处理方法
"""
from multiprocessing import Process
from time import sleep
from signal import  *

# 父进程忽略子进程退出，交给系统处理
signal(SIGCHLD,SIG_IGN)

# 带参数的进程函数
def worker():
	for i in range(3):
		print("I'm Tom")
		print("I'm working...")

p = Process(target=worker)
p.start()
print(p.pid)

# p.join() # 处理僵尸

while True:
	pass
```



  ```
  
  
  
  * 孤儿进程 ： 父进程先于子进程退出，此时子进程成为孤儿进程。
  
    * 特点： 孤儿进程会被系统进程收养，此时系统进程就会成为孤儿进程新的父进程，孤儿进程退出该进程会自动处理。
  
  * 僵尸进程 ： 子进程先于父进程退出，父进程又没有处理子进程的退出状态，此时子进程就会称为僵尸进程。
  
    * 特点： 僵尸进程虽然结束，但是会存留部分进程信息资源在内存中，大量的僵尸进程会浪费系统的内存资源。
  
    * 如何避免僵尸进程产生
  
      1.  使用join()回收
  
      2.  在父进程中使用signal方法处理
  
         ```python```
         from signal import *
         signal(SIGCHLD,SIG_IGN)
  ```

​         

#### 2.2.5 创建进程类

```
"""
自定义进程类
"""

from multiprocessing import Process
import time


def fun2():
    while 1:
        print("函数2在运行")
        time.sleep(1)
        print("函数2还在运行")

# 自定义一个类
class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__() # 加载父类__init__

    # 复杂的进程事件
    def fun1(self):
        while 1:
            print("函数1在运行",self.value)
            time.sleep(1)
            print("函数1还在运行")

    # 整个事件的逻辑控制
    def run(self):
        self.fun1()

p = MyProcess(3)
p.start()  # 运行run，将其作为一个独立进程运行
fun2()     # 主进程
p.join()
```



进程的基本创建方法将子进程执行的内容封装为函数。如果我们更热衷于面向对象的编程思想，也可以使用类来封装进程内容。

* 创建步骤
  
  【1】 继承Process类
  
  【2】 重写`__init__`方法添加自己的属性，使用super()加载父类属性
  
  【3】 重写run()方法
  
* 使用方法
  
  【1】 实例化对象
  
  【2】 调用start自动执行run方法
  
  【3】 调用join回收进程



#### 2.2.4 进程池

```
"""
进程池演示

* 函数事件必须在 进程池创建之前声明
* 父进程退出，进程池就会被销毁
"""

from multiprocessing import Pool
from time import sleep,ctime
import random

# 进程池函数
def worker(msg,sec):
    print(ctime(), '---', msg)
    sleep(sec)

#　创建进程池
pool = Pool(4)

# 向进程池事件队列中加入事件
for i in range(10):
    msg = "Tedu-%d"%i
    pool.apply_async(func=worker,args=(msg,random.randint(1,5)))

# 关闭进程池　－－》　不能加新的事件了
pool.close()

#　阻塞等待回收进程池中的进程
pool.join()

```

> 进程事件Event
>
> ```
> python线程的事件用于主线程控制其他线程的执行，事件主要提供了三个方法 set、wait、clear。
> 
> 事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞，如果“Flag”值为True，那么event.wait 方法时便不再阻塞。
> 
> clear：将“Flag”设置为False
> set：将“Flag”设置为True
> ```

* 必要性
  
  【1】 进程的创建和销毁过程消耗的资源较多
  
  【2】 当任务量众多，每个任务在很短时间内完成时，需要频繁的创建和销毁进程。此时对计算机压力较大
  
  【3】 进程池技术很好的解决了以上问题。
  
  > 节约资源，避免频繁创建和销毁进程
  
* 原理

  创建一定数量的进程来处理事件，事件处理完进	程不退出而是继续处理其他事件，直到所有事件全都处理完毕统一销毁。增加进程的重复利用，降低资源消耗。



* 进程池实现

1. 创建进程池对象，放入适当的进程

```python	  
from multiprocessing import Pool

Pool(processes)
功能： 创建进程池对象
参数： 指定进程数量，默认根据系统自动判定
```
> python中，进程池内部会维护一个进程序列。当需要时，程序会去进程池中获取一个进程
> 如果进程池序列中没有可供使用的进程，那么程序就会等待，直到进程池中有可用进程为止。 
2. 将事件加入进程池队列执行

```python
pool.apply_async(func,args,kwds)
功能: 使用进程池执行 func事件
参数： func 事件函数
      args 元组  给func按位置传参
      kwds 字典  给func按照键值传参
```
> apply 从进程池里取一个进程并同步执行 
> apply_async 从进程池里取出一个进程并异步执行 
3. 关闭进程池

```python
pool.close()
功能： 关闭进程池
```

4. 回收进程池中进程

```python
pool.join()
功能： 回收进程池中进程
```



#### 2.2.5 进程通信

```
"""
进程间通信演示
"""

from multiprocessing import Process,Queue

#　消息队列 (在父进程中创建)
q = Queue()

def request():
    name = "Levi"
    passwd = "123"
    # 存入消息队列
    q.put(name)
    q.put(passwd)

def handle():
    # 从消息队列获取
    name = q.get()
    passwd = q.get()
    print("用户名:",name)
    print("密　码:",passwd)

p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()
```

```
"""
练习２：　使用进程池完成
拷贝一个指定的目录　（目录下全都是普通文件没有子目录）　

os.mkdir("xxx")　创建一个文件夹
os.listdir() 遍历文件夹

将原目录加所有的文件，拷贝到新目录下即可　
把每个文件的拷贝作为一个要执行的事件，然后创建进程池开启４个进程执行这些文件拷贝事件
"""

from multiprocessing import Pool,Queue
import os

q = Queue() # 创建消息队列

# 进程池函数 --> 拷贝一个文件
def copy(old_folder,new_folder,file):
    """
    :param old_folder: 从哪拷贝
    :param new_folder: 拷贝到哪
    :param file: 拷贝什么文件
    """
    fr = open(old_folder+'/'+file,'rb')
    fw = open(new_folder+'/'+file,'wb')
    while True:
        data = fr.read(1024)
        if not data:
            break
        n = fw.write(data)
        q.put(n) #  已经拷贝的字节数
    fr.close()
    fw.close()

# 获取文件夹大小
def get_size(dir):
    total_size = 0
    for file in os.listdir(dir):
        total_size += os.path.getsize(dir+'/'+file)
    return total_size

def main():
    old_folder = input("要拷贝的目录:")
    new_folder = old_folder + "-备份"
    os.mkdir(new_folder)
    total_size = get_size(old_folder) # 获取目录大小

    #　创建进程池
    pool = Pool(4)

    # 向进程池事件队列中加入事件
    for file in os.listdir(old_folder):
        pool.apply_async(func=copy,args=(old_folder,new_folder,file))

    copy_size = 0
    while copy_size < total_size:
        copy_size += q.get() # 从消息队列中实时获取已经拷贝的字节数
        print("拷贝了%.2f%%"%(copy_size/total_size*100))

    pool.close()
    pool.join()

main()
```



* 必要性： 进程间空间独立，资源不共享，此时在需要进程间数据传输时就需要特定的手段进行数据通信。

> 共享内存就是允许两个或多个进程共享一定的存储区。就如同 malloc() 函数向不同进程返回了指向同一个物理内存区域的指针。当一个进程改变了这块地址中的内容的时候，其它进程都会察觉到这个更改。因为数据不需要在客户机和服务器端之间复制，数据直接写到内存，不用若干次数据拷贝，所以这是最快的一种IPC。
>
> 注：共享内存没有任何的同步与互斥机制，所以要使用信号量来实现对共享内存的存取的同步。

* 常用进程间通信方法：消息队列，套接字等。

* 消息队列使用
  * 通信原理： 在内存中开辟空间，建立队列模型，进程通过队列将消息存入，或者从队列取出完成进程间通信。
  * 实现方法

	```python
	from multiprocessing import Queue
	
	q = Queue(maxsize=0)
	功能: 创建队列对象
	参数：最多存放消息个数
	返回值：队列对象
	
	q.put(data,[block,timeout])
	功能：向队列存入消息
	参数：data  要存入的内容
		block  设置是否阻塞 False为非阻塞
		timeout  超时检测
	
	q.get([block,timeout])
	功能：从队列取出消息
	参数：block  设置是否阻塞 False为非阻塞
		 timeout  超时检测
	返回值： 返回获取到的内容
	
	q.full()   判断队列是否为满
	q.empty()  判断队列是否为空
	q.qsize()  获取队列中消息个数
	q.close()  关闭队列
	```

> 管道：单向的、先进先出的，它把一个进程的输出和另一个进程的输入连接在一起。一个进程（写进程）在管道的尾部写入数据，另一个进程（读进程）在管道的头部读出数据。数据被一个进程读出后，将被从管道中删除，其它读进程将再不能读到这些数据。管道提供了简单的流控制机制，进程试图读空管道时，进程将阻塞。同样，管道已经满时，进程再试图向管道写入数据，进程将阻塞。 管道是一个固定大小的缓冲区。在Linux中，该缓冲区的大小为1页，即4K（这里现在为65536byte）字节，使得它的大小不象文件那样不加检验地增长。使用单个固定缓冲区也会带来问题，比如在写管道时可能变满，当这种情况发生时，随后对管道的write()调用将默认地被阻塞，等待某些数据被读取，以便腾出足够的空间供write()调用写。
>
> * Pipe常用于两个进程，两个进程分别位于管道的两端
>
> * Pipe方法返回（conn1,conn2）代表一个管道的两个端，Pipe方法有duplex参数，默认为True，即全双工模式，若为FALSE，conn1只负责接收信息，conn2负责发送，
>
> * send和recv方法分别为发送和接收信息。

**群聊聊天室 **

> 功能 ： 类似qq群功能
>
> 【1】 有人进入聊天室需要输入姓名，姓名不能重复
>
> 【2】 有人进入聊天室时，其他人会收到通知：xxx 进入了聊天室
>
> 【3】 一个人发消息，其他人会收到：xxx ： xxxxxxxxxxx
>
> 【4】 有人退出聊天室，则其他人也会收到通知:xxx退出了聊天室
>
> 【5】 扩展功能：服务器可以向所有用户发送公告:管理员消息： xxxxxxxxx
>

```
"""
服务器
"""

from socket import *

# 服务器地址
HOST = "0.0.0.0"
PORT = 8000
ADDR = (HOST,PORT)

# 存储用户  {name:address..}
user = {}

# 处理登录请求
def do_login(sock,name,address):
    if name in user:
        sock.sendto(b"Fail",address)
        return
    else:
        sock.sendto(b"OK", address)
        # 通知其他人
        msg = "欢迎 %s 进入聊天室"%name
        for i in user:
            sock.sendto(msg.encode(),user[i])
        # 存储用户
        user[name] = address
        # print(user)

# 处理聊天
def do_chat(sock,name,content):
    msg = "%s : %s"%(name,content)
    for i in user:
        # 除去本人
        if i != name:
            sock.sendto(msg.encode(),user[i])

# 退出
def do_quit(sock,name):
    del user[name] # 从字典中删除用户
    msg = "%s 退出聊天室"%name
    # 通知其他人
    for i in user:
        sock.sendto(msg.encode(), user[i])

# 程序启动函数
def main():
    sock = socket(AF_INET,SOCK_DGRAM) # UDP
    sock.bind(ADDR)

    # 循环接收用户请求
    while True:
        # 接收用户请求 (所有客户端的所有请求都向这里发送)
        data,addr = sock.recvfrom(1024)
        tmp = data.decode().split(" ",2) # 切割出前2项
        # 根据请求调用模块
        if tmp[0] == 'L':
            # tmp-->['L','name']
            do_login(sock,tmp[1],addr)
        elif tmp[0] == 'C':
            # tmp--> ['C','name','content']
            do_chat(sock,tmp[1],tmp[2])
        elif tmp[0] == 'Q':
            # tmp -> ['Q',name]
            do_quit(sock,tmp[1])





if __name__ == '__main__':
    main()


```

```
"""
chat room 客户端
发送请求，获取结果
"""

from socket import *
from multiprocessing import Process
import sys

# 服务器地址
ADDR = ('127.0.0.1',8000)

# 接收消息
def recv_msg(sock):
    while True:
        data,addr = sock.recvfrom(4096)
        print(data.decode())

# 发送消息
def send_msg(sock,name):
    while True:
        content = input("发言:")
        if content == "quit":
            msg = "Q " + name
            sock.sendto(msg.encode(),ADDR)
            sys.exit("您已退出聊天室") # 父进程退出
        msg = "C %s %s"%(name,content)
        sock.sendto(msg.encode(),ADDR) # 发送消息给服务器


# 进入聊天室
def login(sock):
    while True:
        name = input("Name:")
        msg = "L " + name # 根据协议，整理发送的消息格式 L name
        sock.sendto(msg.encode(),ADDR)
        result,add = sock.recvfrom(128)
        if result.decode() == "OK":
            print("进入聊天室")
            return name
        else:
            print("该用户已存在")

def main():
    sock = socket(AF_INET,SOCK_DGRAM)
    name = login(sock) # name 进入聊天室

    # 创建子进程
    p = Process(target=recv_msg,args=(sock,))
    p.daemon = True # 父进程退出时子进程也退出
    p.start()
    send_msg(sock,name) # 发送消息



if __name__ == '__main__':
    main()
```





### 2.3 线程 (Thread)

> 线程是CPU调度和分派的基本单位。 进程是操作系统的基本单位。
>
> 协程：一种比线程更加轻量级的存在，正如一个进程可以拥有多个线程一样，一个线程可以拥有多个协程。协程不是被操作系统内核所管理的，而是完全由程序所控制，也就是在用户态执行。这样带来的好处是性能大幅度的提升，因为不会像线程切换那样消耗资源。
>
> 协程不是进程也不是线程，而是一个特殊的函数，这个函数可以在某个地方挂起，并且可以重新在挂起处外继续运行。所以说，协程与进程、线程相比并不是一个维度的概念。

#### 2.3.1 线程概述

* 什么是线程
  【1】 线程被称为轻量级的进程，也是多任务编程方式

  【2】 也可以利用计算机的多cpu资源

  【3】 线程可以理解为进程中再开辟的分支任务

* 线程特征
  【1】 一个进程中可以包含多个线程
  
  【2】 线程也是一个运行行为，消耗计算机资源
  
  【3】 一个进程中的所有线程共享这个进程的资源

  【4】 多个线程之间的运行同样互不影响各自运行
  
  【5】 线程的创建和销毁消耗资源远小于进程
  
  
  
  ![](./img/21.jpg)

#### 2.3.2 多线程编程

```
"""
线程示例演示2
"""
from threading import Thread
from time import sleep

# 含有参数的线程函数
def fun(sec,name):
    print("含有参数的线程")
    sleep(sec)
    print("%s线程执行完毕"%name)

# 创建多个线程
jobs = []
for i in range(5):
    t = Thread(target=fun,args=(2,),kwargs={"name":'T%d'%i})
    jobs.append(t) # 存储线程对象
    t.start()

# 回收线程
[i.join() for i in jobs]
```



* 线程模块： threading

![](./img/22.jpg)



* 创建方法

  【1】 创建线程对象

```
from threading import Thread 

t = Thread()
功能：创建线程对象
参数：target 绑定线程函数
     args   元组 给线程函数位置传参
     kwargs 字典 给线程函数键值传参
```

​	【2】 启动线程

```
 t.start()
```

​	【3】 回收线程

```
 t.join([timeout])
```


* 线程对象属性
  * t.setName()  设置线程名称
  * t.getName()  获取线程名称
  * t.is_alive()  查看线程是否在生命周期
  * t.setDaemon()  设置daemon属性值
  * t.isDaemon()  查看daemon属性值
    * daemon为True时主线程退出分支线程也退出。要在start前设置，通常不和join一起使用。



#### 2.3.3 创建线程类

```
"""
自定义线程类演示
"""

from threading import Thread
import time

class MyThread(Thread):
    def __init__(self,song):
        self.song = song
        super().__init__() # 加载父类方法

    def run(self):
        for i in range(3):
            print("playing %s:%s"%(self.song,time.ctime()))
            time.sleep(2)

t = MyThread("凉凉")
t.start() # 运行run方法，作为线程
t.join()


```





1. 创建步骤
   【1】 继承Thread类
   
   【2】 重写`__init__`方法添加自己的属性，使用super()加载父类属性
   
   【3】 重写run()方法
   
2. 使用方法
   【1】 实例化对象

   【2】 调用start自动执行run方法

   【3】 调用join回收线程



#### 2.3.4 线程同步互斥

> 同步是指：当程序1调用程序2时，程序1停下不动，直到程序2完成回到程序1来，程序1才继续执行下去。 
> 异步是指：当程序1调用程序2时，程序1径自继续自己的下一个动作，不受程序2的的影响。
>
> 同步意味着有序     异步意味着无序

```
"""
event 线程同步互斥方法示例
"""

from threading import Thread,Event

s = None # 线程通信变量
e = Event() # event对象

# 线程函数
def 杨子荣():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set() # 解除主线程阻塞


t = Thread(target=杨子荣)
t.start()

# 主线程做验证
print("数对口令就是自己人")
e.wait() # 阻塞等待验证通知
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死他.... 无情啊....")

t.join()

```
> e = Event()     # e为事件对象
>
> 对象方法：wait、clear、set
>
> 事件处理的机制：全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞，如果“Flag”值为True，那么event.wait 方法时便不再阻塞。
>
> clear：将“Flag”设置为False 
>
> set：将“Flag”设置为True
```
"""
练习2 ： 有两个线程同时运行，一个线程负责打印 1---52 52个数字
        另一个线程打印  A-Z 26个字母
        要求打印的的顺序是12A34B56C....5152Z
        使用同步互斥方法进行打印顺序的管控
"""

from threading import Thread,Lock

lock1 = Lock()
lock2 = Lock()

def print_num():
    for i in range(1,53,2):
        lock1.acquire()
        print(i)
        print(i+1)
        lock2.release()

def print_char():
    for i in range(65,91):
        lock2.acquire()
        print(chr(i))
        lock1.release()

t1 = Thread(target = print_num)
t2 = Thread(target = print_char)

lock2.acquire() # lock2先上锁

t1.start()
t2.start()
t1.join()
t2.join()


```



* 线程通信方法： 线程间使用全局变量进行通信

* 共享资源争夺
  * 共享资源：多个进程或者线程都可以操作的资源称为共享资源。对共享资源的操作代码段称为临界区。
  * 影响 ： 对共享资源的无序操作可能会带来数据的混乱，或者操作错误。此时往往需要同步互斥机制协调操作顺序。

* 同步互斥机制

  * 同步 ： 同步是一种协作关系，为完成操作，多进程或者线程间形成一种协调，按照必要的步骤有序执行操作。

    ![](./img/7_%E5%90%8C%E6%AD%A5.png)

  * 互斥 ： 互斥是一种制约关系，当一个进程或者线程占有资源时会进行加锁处理，此时其他进程线程就无法操作该资源，直到解锁后才能操作。

![](./img/7_%E4%BA%92%E6%96%A5.png)



* 线程Event

```python		  
from threading import Event

e = Event()  创建线程event对象

e.wait([timeout])  阻塞等待e被set

e.set()  设置e，使wait结束阻塞

e.clear() 使e回到未被设置状态

e.is_set()  查看当前e是否被设置
```



* 线程锁 Lock

```python
from  threading import Lock

lock = Lock()  创建锁对象
lock.acquire() 上锁  如果lock已经上锁再调用会阻塞
lock.release() 解锁

with  lock:  上锁再执行目标代码
...
...
	 with代码块结束自动解锁
```



#### 2.3.5 死锁

* 什么是死锁

  死锁是指两个或两个以上的线程在执行过程中，由于竞争资源或者由于彼此通信而造成的一种阻塞的现象，若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁。

![](./img/%E6%AD%BB%E9%94%81.jpg)

* 死锁产生条件

  * 互斥条件：指线程使用了互斥方法，使用一个资源时其他线程无法使用。

  * 请求和保持条件：指线程已经保持至少一个资源，但又提出了新的资源请求，在获取到新的资源前不会释放自己保持的资源。

  * 不剥夺条件：不会受到线程外部的干扰，如系统强制终止线程等。

  * 环路等待条件：指在发生死锁时，必然存在一个线程——资源的环形链，如 T0正在等待一个T1占用的资源；T1正在等待T2占用的资源，……，Tn正在等待已被T0占用的资源。

* 如何避免死锁
  * 逻辑清晰，不要同时出现上述死锁产生的四个条件
  * 通过测试工程师进行死锁检测



#### 2.3.6 GIL问题

* 什么是GIL问题 （全局解释器锁）

  由于python解释器设计中加入了解释器锁，导致python解释器同一时刻只能解释执行一个线程，大大降低了线程的执行效率。




* 导致后果
  因为遇到阻塞时线程会主动让出解释器，去解释其他线程。所以python多线程在执行多阻塞任务时可以提升程序效率，其他情况并不能对效率有所提升。

* GIL问题建议


    * 尽量使用进程完成无阻塞的并发行为
    
    * 不使用c作为解释器 （Java  C#）
    
     Guido的声明：<http://www.artima.com/forums/flat.jsp?forum=106&thread=214235>



* 结论 
  * GIL问题与Python语言本身并没什么关系，属于解释器设计的历史问题。
  * 在无阻塞状态下，多线程程序程序执行效率并不高，甚至还不如单线程效率。
  * Python多线程只适用于执行有阻塞延迟的任务情形。



#### 2.3.7 进程线程的区别联系

* 区别联系

1. 两者都是多任务编程方式，都能使用计算机多核资源
2. 进程的创建删除消耗的计算机资源比线程多
3. 进程空间独立，数据互不干扰，有专门通信方法；线程使用全局变量通信
4. 一个进程可以有多个分支线程，两者有包含关系
5. 多个线程共享进程资源，在共享资源操作时往往需要同步互斥处理
6. Python线程存在GIL问题，但是进程没有。

* 使用场景

  ![](./img/23.jpg)

1. 任务场景：一个大型服务，往往包含多个独立的任务模块，每个任务模块又有多个小独立任务构成，此时整个项目可能有多个进程，每个进程又有多个线程。
3. 编程语言：Java,C#之类的编程语言在执行多任务时一般都是用线程完成，因为线程资源消耗少；而Python由于GIL问题往往使用多进程。



## 3. 网络并发模型



### 3.1 网络并发模型概述

* 什么是网络并发

  在实际工作中，一个服务端程序往往要应对多个客户端同时发起访问的情况。如果让服务端程序能够更好的同时满足更多客户端网络请求的情形，这就是并发网络模型。

  ![](./img/24.jpg)

* 循环网络模型问题

  循环网络模型只能循环接收客户端请求，处理请求。同一时刻只能处理一个请求，处理完毕后再处理下一个。这样的网络模型虽然简单，资源占用不多，但是无法同时处理多个客户端请求就是其最大的弊端，往往只有在一些低频的小请求任务中才会使用。



### 3.2 多任务并发模型

多任务并发模型具体指多进程多线程网络并发模型，即每当一个客户端连接服务器，就创建一个新的进程/线程为该客户端服务，客户端退出时再销毁该进程/线程，多任务并发模型也是实际工作中最为常用的服务端处理模型。



* 优点：能同时满足多个客户端长期占有服务端需求，可以处理各种请求。
* 缺点： 资源消耗较大
* 适用情况：客户端请求较复杂，需要长时间占有服务器。

#### 3.1.1 多进程并发模型

```
"""
重点代码！！
多进程tcp并发模型

步骤：
创建网络套接字用于接收客户端请求
等待客户端连接
客户端连接，则创建新的进程具体处理客户端请求
主进程继续等待其他客户端连接
如果客户端退出，则销毁对应的进程
"""

from socket import *
from multiprocessing import Process
from signal import *
import sys

# 全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

# 处理客户端请求
def handle(connfd):
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        print("客户端:",data)
        connfd.send(b"OK")
    connfd.close()


def main():
    # tcp套接字
    s = socket()
    s.bind(ADDR)
    s.listen(3)

    print("Listen the port %d..."%PORT)
    # 处理僵尸进程
    signal(SIGCHLD,SIG_IGN)

    # 循环连接客户端
    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt as e:
            s.close()
            sys.exit("服务端退出！！")

        # 创建子进程处理客户端具体请求事务
        p = Process(target = handle,args=(c,))
        p.daemon = True  # 如果父进程退出，所有服务立即终止则可以加
        p.start()

if __name__ == '__main__':
    main()
```



* 创建网络套接字用于接收客户端请求
* 等待客户端连接
* 客户端连接，则创建新的进程具体处理客户端请求
* 主进程继续等待其他客户端连接
* 如果客户端退出，则销毁对应的进程

> 多进程并发即运行多个独立的程序，优势在于并发处理的任务都由操作系统管理 

#### 3.1.2 多线程并发模型

```
"""
重点代码！
多线程并发模型
步骤 ： 原理基本同多进程并非
"""

from socket import *
from threading import Thread
import sys

# 全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

# 处理客户端请求
def handle(connfd):
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        print("客户端:",data)
        connfd.send(b"OK")
    connfd.close()

def main():
    # tcp套接字
    s = socket()
    s.bind(ADDR)
    s.listen(3)

    print("Listen the port %d..." % PORT)

    # 循环接收客户端的连接请求
    while True:
        try:
            c,addr = s.accept()
            print("Connect from ",addr)
        except KeyboardInterrupt :
            s.close()
            sys.exit("服务端退出") # 进程退出

        # 创建线程处理客户端连接
        t = Thread(target=handle,args=(c,))
        t.start()

if __name__ == '__main__':
    main()
```



- 创建网络套接字用于接收客户端请求
- 等待客户端连接
- 客户端连接，则创建新的线程具体处理客户端请求
- 主线程继续等待其他客户端连接
- 如果客户端退出，则销毁对应的线程

> 多线程并发则由程序员管理并处理并发任务，这种并发方式可以方便地在线程之间共享数据（前提是不能互斥）

**ftp 文件服务器**

【1】 分为服务端和客户端，要求可以有多个客户端同时操作。

【2】 客户端可以查看服务器文件库中有什么文件。

【3】 客户端可以从文件库中下载文件到本地。

【4】 客户端可以上传一个本地文件到文件库。

【5】 使用print在客户端打印命令输入提示，引导操作





### 3.3 IO并发模型



#### 3.2.1 IO概述

* 什么是IO

  在程序中存在读写数据操作行为的事件均是IO行为，比如终端输入输出 ,文件读写，数据库修改和网络消息收发等。

* 程序分类
  * IO密集型程序：在程序执行中有大量IO操作，而运算操作较少。消耗cpu较少，耗时长。
  
  > 建议使用多线程
  
  * 计算密集型程序：程序运行中运算较多，IO操作相对较少。cpu消耗多，执行速度快，几乎没有阻塞。
  
  > 建议使用多进程
  
* IO分类：阻塞IO ，非阻塞IO，IO多路复用，异步IO等。

#### 3.2.2 阻塞IO

> 阻塞调用是指调用结果返回之前，当前线程会被挂起。函数只有在得到结果之后才会返回。
>
> 常见的阻塞形式有：网络I/O阻塞、磁盘I/O阻塞、用户输入阻塞等

  * 定义：在执行IO操作时如果执行条件不满足则阻塞。阻塞IO是IO的默认形态。
  * 效率：阻塞IO效率很低。但是由于逻辑简单所以是默认IO行为。
  * 阻塞情况
    * 因为某种执行条件没有满足造成的函数阻塞
      e.g.  accept   input   recv
    * 处理IO的时间较长产生的阻塞状态
      e.g. 网络传输，大文件读写



#### 3.2.3 非阻塞IO 

> 非阻塞和阻塞的概念相对应，指在不能立刻得到结果之前，该函数不会阻塞当前线程，而会立刻返回。
>
> 仅当程序封装的级别可以囊括独立的子程序单元时，它才可能存在非阻塞状态。

* 定义 ：通过修改IO属性行为，使原本阻塞的IO变为非阻塞的状态。

- 设置套接字为非阻塞IO

	```
	sockfd.setblocking(bool)
	功能：设置套接字为非阻塞IO
	参数：默认为True，表示套接字IO阻塞；设置为False则套接字IO变为非阻塞
	```



- 超时检测 ：设置一个最长阻塞时间，超过该时间后则不再阻塞等待。

  ```
  sockfd.settimeout(sec)
  功能：设置套接字的超时时间
  参数：设置的时间(秒)
  ```


#### 3.2.4 IO多路复用

* 定义

  同时监控多个IO事件，当哪个IO事件准备就绪就执行哪个IO事件。以此形成可以同时处理多个IO的行为，避免一个IO阻塞造成其他IO均无法执行，提高了IO执行效率。

* 具体方案
  * select方法 ： windows  linux  unix
  * poll方法： linux  unix
  * epoll方法： linux
  
  

* select 方法

```python
rs, ws, xs=select(rlist, wlist, xlist[, timeout])
功能: 监控IO事件，阻塞等待IO发生
参数：rlist  列表  读IO列表，添加等待发生的或者可读的IO事件
      wlist  列表  写IO列表，存放要可以主动处理的或者可写的IO事件
      xlist  列表 异常IO列表，存放出现异常要处理的IO事件
      timeout  超时时间

返回值： rs 列表  rlist中准备就绪的IO
        ws 列表  wlist中准备就绪的IO
	   xs 列表  xlist中准备就绪的IO
```



* poll方法

```python
p = select.poll()
功能 ： 创建poll对象
返回值： poll对象
```

```python	
p.register(fd,event)   
功能: 注册关注的IO事件
参数：fd  要关注的IO
      event  要关注的IO事件类型
  	     常用类型：POLLIN  读IO事件（rlist）
		      POLLOUT 写IO事件 (wlist)
		      POLLERR 异常IO  （xlist）
		      POLLHUP 断开连接 
		  e.g. p.register(sockfd,POLLIN|POLLERR)

p.unregister(fd)
功能：取消对IO的关注
参数：IO对象或者IO对象的fileno
```

```python
events = p.poll()
功能： 阻塞等待监控的IO事件发生
返回值： 返回发生的IO
        events格式  [(fileno,event),()....]
        每个元组为一个就绪IO，元组第一项是该IO的fileno，第二项为该IO就绪的事件类型
        # 【int，int】
```

> fileno : 文件描述符
>
> 事件类型 : 事件类型里面的地址内容

> 文件描述符：每个IO在系统中都有一个系统分配的 >= 0 的不重复的整数编号
>
> 查看方法：print(file.fileno)

* epoll方法

  使用方法 ： 基本与poll相同

  生成对象改为 epoll()

  将所有事件类型改为EPOLL类型

  

  * epoll特点
    * epoll 效率比select poll要高
    * epoll 监控IO数量比select要多
    * epoll 的触发方式比poll要多 （EPOLLET边缘触发）



#### 3.2.5 IO并发模型

利用IO多路复用等技术，同时处理多个客户端IO请求。

* 优点 ： 资源消耗少，能同时高效处理多个IO行为
* 缺点 ： 只针对处理并发产生的IO事件
* 适用情况：HTTP请求，网络传输等都是IO行为，可以通过IO多路复用监控多个客户端的IO请求。



* 并发服务实现过程

  【1】将关注的IO准备好，通常设置为非阻塞状态。
  
  【2】通过IO多路复用方法提交，进行IO监控。
  
  【3】阻塞等待，当监控的IO有发生时，结束阻塞。
  
  【4】遍历返回值列表，确定就绪IO事件。
  
  【5】处理发生的IO事件。
  
  【6】继续循环监控IO发生。

```
"""
select
"""
from socket import *
from select import *

ADDR=("0.0.0.0",8888)

tcp_socet=socket()
tcp_socet.bind(ADDR)
tcp_socet.listen(5)

tcp_sockfd.setblocking(False)

rlist=[tcp_socet]
wlist=[]
xlist=[]

while 1:
    rs,ws,xs=select(rlist,wlist,xlist)
    for r in rs:
        if r==tcp_socet:
            connfd,addr=r.accept()
            print("Connect from",addr)
            connfd.setblocking(False)
            rlist.append(connfd)
        else:
            data=r.recv(1024).decode()
            if not data:
                r.close()
                rlist.remove(r)
                print("客户端",r,"退出了")
                continue
            print("客户端:",data)
            # r.send(b"ok")
            wlist.append(r)

    for w in wlist:
        w.send(b"ok")
        wlist.remove(w)
```

```
"""
poll
"""
from socket import *
from select import *

ADDR = ("0.0.0.0", 8888)

tcp_socet = socket()
tcp_socet.bind(ADDR)
tcp_socet.listen(5)

p = poll()
p.register(tcp_socet, POLLIN)

map = {tcp_socet.fileno(): tcp_socet}

while 1:
    events = p.poll()
    for fileno, event in events:
        # (fileno,event)
        if fileno == tcp_socet.fileno():
            connfd,addr=map[fileno].accept()
            print("Connect from",addr)
            connfd.setblocking(False)
            p.register(connfd,POLLIN)
            map[connfd.fileno()]=connfd
        elif event==POLLIN:
            data=map[fileno].recv(1024).decode()
            if not data:
                print("关闭")
                try:
                    p.unrigster(fileno)
                except:
                    print("客户端退出")
                map[fileno].close()
                del map[fileno]
                continue
            print("收到：",data)
            p.register(fileno,POLLOUT)
            # map[fileno].send(b"ok")
        elif event & POLLOUT:
            map[fileno].send(b"ok")
            p.register(fileno,POLLIN)
```
```
"""
epoll
"""
from socket import *
from select import *

ADDR = ("0.0.0.0", 8888)

tcp_socket = socket()
tcp_socket.bind(ADDR)
tcp_socket.listen(5)

p = epoll()
p.register(tcp_socket, EPOLLIN)

map = {tcp_socket.fileno(): tcp_socket}

while 1:
    events = p.poll()
    for fileno, event in events:
        # (fileno,event)
        if fileno == tcp_socket.fileno():
            connfd,addr=map[fileno].accept()
            print("Connect from",addr)
            connfd.setblocking(False)
            p.register(connfd,EPOLLIN)
            map[connfd.fileno()]=connfd
        elif event==EPOLLIN:
            data=map[fileno].recv(1024).decode()
            if not data:
                print("关闭")
                try:
                    p.unrigster(fileno)
                except:
                    print("客户端退出")
                map[fileno].close()
                del map[fileno]
                continue
            print("收到：",data)
            p.unregister(fileno)
            p.register(fileno, EPOLLOUT)
            # map[fileno].send(b"ok")
        elif event & EPOLLOUT:
            map[fileno].send(b"ok")
            p.unregister(fileno)
            p.register(fileno, EPOLLIN)
```

```
"""
客户端模板
"""
from socket import *

tcp_socket=socket()
tcp_socket.connect(("127.0.0.1",8888))

while 1:
    msg=input(">>")
    if not msg:
        print("客户端退出")
        break
    tcp_socket.send(msg.encode())
    data=tcp_socket.recv(1024).decode()
    print("服务器：",data)
```

|        |      平台支持       | 监控数量 | 执行效率 |
| :----: | :-----------------: | :------: | :------: |
| select |     优秀（全）      |   1024   |   一般   |
|  poll  | 良好（Linux，Unix） |  无限制  |   一般   |
| epoll  |    较差（Linux）    |  无限制  |   较高   |

> select、poll 是在操作系统映射IO对象，操作系统轮询，有IO口就绪，操作系统返回应用层有IO就绪，应用层再遍历IO口，查找就绪的IO口，然后重新映射。
>
> epoll 是在系统层开辟空间，存储要关注的IO对象，操作系统轮询，有IO口就绪，操作系统直接返回应用层就绪的IO对象，应用层不用遍历查找就绪的IO口，也不用重新向操作系统传递要关注的IO对象。
>
> epoll 边缘触发（EPOLLET）：一般如果IO发生了，没有处理，会一直提醒，但是边缘触发只会提醒一次，但是下次又有IO发生了，会一起提醒，除非该IO不再就绪。

## 4. web服务

### 4.1 HTTP协议

#### 4.1.1 协议概述

* 用途 ： 网页获取，数据的传输
* 特点
  * 应用层协议，使用tcp进行数据传输
  * 简单，灵活，很多语言都有HTTP专门接口
  * 无状态：数据传输过程中不记录传输内容（记录缓存是浏览器，不是http，像是不用重复登录，便是记录了缓存）
  * 有丰富的请求类型
  * 可以传输的数据类型众多

> 80是HTTP协议默认使用的端口号
>
> 超文本：多种数据类型：文本、图片、视频等等
>
> 目前使用的是1.1版本

#### 4.1.2 网页访问流程

1. 客户端（浏览器）通过tcp传输，发送http请求给服务端
2. 服务端接收到http请求后进行解析
3. 服务端处理请求内容，组织响应内容
4. 服务端将响应内容以http响应格式发送给浏览器
5. 浏览器接收到响应内容，解析展示

![](./img/2_%E7%BD%91%E7%AB%99%E8%AE%BF%E9%97%AE.png)

> 浏览器输入网址-->域名（DNS）解析-->服务器地址-->将请求组织为HTTP请求格式-->tcp发送给服务端
>
> 服务器里有前端代码和后端代码，前段复责展示页面，后端负责逻辑运算
>
> 服务器 web server 接收请求，解析请求-->处理-->将响应组织为HTTP相应格式
>
> 浏览器接收响应，解析-->将数据展示出来

#### 4.1.2 HTTP请求

- 请求行 ： 具体的请求类别和请求内容

```
	GET    （空格）     /    （空格）    HTTP/1.1
	请求类别         请求内容             协议版本
```

​		  请求类别：每个请求类别表示要做不同的事情 

```
		GET : 获取网络资源
		POST ：提交一定的信息，得到反馈
		HEAD ： 只获取网络资源的响应头
		PUT ： 更新服务器资源（上传）
		DELETE ： 删除服务器资源
```

> 换行：\r\n

- 请求头：对请求的进一步解释和描述

```
Accept-Encoding: gzip
```

- 空行
- 请求体: 请求参数或者提交内容

 ![](./img/request.jpg)

#### 4.1.3 HTTP响应

- 响应行 ： 反馈基本的响应情况

```
HTTP/1.1     200       OK
版本信息    响应码   附加信息
```

​	响应码 ： 

```
1xx  提示信息，表示请求被接收
2xx  响应成功
3xx  响应需要进一步操作，重定向
4xx  客户端错误
5xx  服务器错误
```

- 响应头：对响应内容的描述

```
Content-Type: text/html
Content-Length:109\r\n
```

- 空行
- 响应体：响应的主体内容信息

![](./img/response.png)

> 返回码详情
>
> **1xx（临时响应）用于表示临时响应并需要请求者执行操作才能继续的状态代码**
>
> 100——客户必须继续发出请求
>
> 101——客户要求服务器根据请求转换HTTP协议版本
>
> **2xx（成功）用于表示服务器已成功处理了请求的状态代码**
>
> 200——操作成功
>
> 201——提示知道新文件的URL
>
> 202——接受和处理、但处理未完成
>
> 203——返回信息不确定或不完整
>
> 204——请求收到，但返回信息为空
>
> 205——服务器完成了请求，用户代理必须复位当前已经浏览过的文件
>
> 206——服务器已经完成了部分用户的GET请求
>
> **3xx（已重定向）要完成请求，您需要进一步进行操作。通常，这些状态代码是永远重定向的。**
>
> 300——请求的资源可在多处得到
>
> 301——删除请求数据
>
> 302——在其他地址发现了请求数据，#url-rewrite 地址重定向
>
> 303——建议客户访问其他URL或访问方式
>
> 304——客户端已经执行了GET，但文件未变化 。#读取缓存  ctrl+F5刷掉本地缓存，再次从服务器端获取资源
>
> 305——请求的资源必须从服务器指定的地址得到
>
> 306——前一版本HTTP中使用的代码，现行版本中不再使用
>
> 307——申明请求的资源临时性删除
>
> **4xx（请求错误）这些状态代码表示，请求可能出错，已妨碍了服务器对请求的处理。**
>
> 400——错误请求，如语法错误
>
> 401——请求授权失败
>
> 402——保留有效ChargeTo头响应
>
> 403——请求不允许
>
> 404——没有发现文件、查询或URl
>
> 405——用户在Request-Line字段定义的方法不允许
>
> 406——根据用户发送的Accept拖，请求资源不可访问
>
> 407——类似401，用户必须首先在代理服务器上得到授权
>
> 408——客户端没有在用户指定的饿时间内完成请求
>
> 409——对当前资源状态，请求不能完成
>
> 410——服务器上不再有此资源且无进一步的参考地址
>
> 411——服务器拒绝用户定义的Content-Length属性请求
>
> 412——一个或多个请求头字段在当前请求中错误
>
> 413——请求的资源大于服务器允许的大小
>
> 414——请求的资源URL长于服务器允许的长度
>
> 415——请求资源不支持请求项目格式
>
> 416——请求中包含Range请求头字段，在当前请求资源范围内没有range指示值，请求也不包含If-Range请求头字段
>
> 417——服务器不满足请求Expect头字段指定的期望值，如果是代理服务器，可能是下一级服务器不能满足请求
>
> **5xx（服务器错误）这些状态代码表示，服务器在尝试处理请求时发生内部错误。这些错误可能是服务器本身的错误，而不是请求出错。**
>
> 500——服务器产生内部错误
>
> 501——服务器不支持请求的函数
>
> 502——服务器暂时不可用，有时是为了防止发生系统过载
>
> 503——服务器过载或暂停维修
>
> 504——关口过载，服务器使用另一个关口或服务来响应用户，等待时间设定值较长
>
> 505——服务器不支持或拒绝支请求头中指定的HTTP版本

### 4.2 web 服务程序实现

  1. 主要功能 ：
	  	【1】 接收客户端（浏览器）请求
	
	【2】 解析客户端发送的请求
	
	【3】 根据请求组织数据内容
	
	【4】 将数据内容形成http响应格式返回给浏览器
	
  2. 特点 ：
        【1】 采用IO并发，可以满足多个客户端同时发起请求情况

        【2】 通过类接口形式进行功能封装

        【3】 做基本的请求解析，根据具体请求返回具体内容，同时处理客户端的非网页请求行为

```
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
```



## 并发技术探讨（扩展）（更高并发量，更快响应时间，更强的稳定性）

### 高并发问题

* 衡量高并发的关键指标

  - 响应时间(Response Time) ： 接收请求后处理的时间

  - 吞吐量(Throughput)： 响应时间+QPS+同时在线用户数量

  - 每秒查询率QPS(Query Per Second)： 每秒接收请求的次数

  - 每秒事务处理量TPS(Transaction Per Second)：每秒处理请求的次数（包含接收，处理，响应）

  - 同时在线用户数量：同时连接服务器的用户的数量

* 多大的并发量算是高并发

  * 没有最高，只要更高

    比如在一个小公司可能QPS2000+就不错了，在一个需要频繁访问的门户网站可能要达到QPS5W+

  * C10K问题

    早先服务器都是单纯基于进程/线程模型的，新到来一个TCP连接，就需要分配1个进程（或者线程）。而进程占用操作系统资源多，一台机器无法创建很多进程。如果是C10K就要创建1万个进程，那么单机而言操作系统是无法承受的，这就是著名的C10k问题。创建的进程线程多了，数据拷贝频繁， 进程/线程切换消耗大， 导致操作系统崩溃，这就是C10K问题的本质！

### 更高并发的实现

​		为了解决C10K问题，现在高并发的实现已经是一个更加综合的架构艺术。涉及到进程线程编程，IO处理，数据库处理，缓存，队列，负载均衡等等，这些我们在后面的阶段还会学习。此外还有硬件的设计，服务器集群的部署，服务器负载，网络流量的处理等。

![](./img/25.jpg)



实际工作中，应对更庞大的任务场景，网络并发模型的使用有时也并不单一。比如多进程网络并发中每个进程再开辟线程，或者在每个进程中也可以使用多路复用的IO处理方法。

​	 