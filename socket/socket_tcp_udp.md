socket
    socket  是操作系统提供的网络编程接口
    Python对操作系统的socket接口进行封装提供socket模块

网络应用程序(C/S架构):
    服务端      必须先运行并且绑定端口和IP, 等待客户端连接提供服务
    客户端      拿到服务端的IP和端口号直接连接进行通讯

    UDP应用流程:
        服务端:
            创建操作系统提供UDP传输协议的编程接口, 返回UDP套接字对象
            sd = socket.socket(type=socket.SOCK_DGRAM)

            给套接字对象绑定IP和端口号(必须1024以上, 65535以内)
            sd.bind(('0.0.0.0', 9000))

            while True:
                等待客户端请求
                data, addr = sd.recvfrom(1024)

                处理客户端请求
                print("%s: %s" % (addr, data.decode()))

            关闭套接字对象
            sd.close()

        客户端:
            创建操作系统提供UDP传输协议的编程接口, 返回UDP套接字对象
            sd = socket.socket(type=socket.SOCK_DGRAM)

            while True:
                data = input("请输入发送数据: ")
                if data == 'q':
                    break
                sd.sendto(data.encode(), ('192.168.7.170', 9000))

            sd.close()

实现点对点聊天程序
    实时收发
    同步退出
    防干扰


TCP:
    TCP保证数据传输的完整性
    TCP面向连接: 三次握手
        客户端给服务器发送请求连接包
        服务器给客户端发送回应+请求连接包
        客户端给服务器发送回应连接包

    三次握手之后TCP传输数据必须回应

    TCP应用流程:
        服务端:
            创建操作系统提供TCP传输协议的编程接口, 返回TCP套接字对象
            sd = socket.socket()

            给套接字对象绑定IP和端口号(必须1024以上, 65535以内)
            sd.bind(('0.0.0.0', 9000))

            告诉操作系统监听此套接字
            sd.listen()


            while True:
                等待客户端请求
                cli_sd, addr = sd.accept()

                处理客户端请求
                data = cli_sd.recv(1024)
                cli.send(data)
                #print("%s: %s" % (addr, data.decode()))

            关闭套接字对象
            sd.close()

        客户端:
            创建操作系统提供TCP传输协议的编程接口, 返回TCP套接字对象
            sd = socket.socket()

            sd.connect(('192.168.7.170', 9000))

            while True:
                data = input("请输入发送数据: ")
                if data == 'q':
                    break
                sd.send(data.encode())
                print(sd.recv(1024).decode())

            sd.close()
