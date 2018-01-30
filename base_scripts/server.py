# coding=utf-8

import subprocess
import socket
import struct
import json


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  # 在链接异常终止后，再次启动会复用之前的IP端口，
                                                            # 防止资源没有释放而产生地址冲突

server.bind(('192.168.20.231',8080))  # 绑定的IP和端口
server.listen(5)        # 参数表示最大可以挂起的连接数
while True:              # 循环建立链接
    conn,client_addr=server.accept()  # 客户端的链接信息

    while True:  # 循环收发消息
        try:
            client_data=conn.recv(1024) # 表示最大收取的消息
            res = subprocess.Popen(client_data.decode('utf-8'),   # 将接收的命令交给shell执行，并将返回的
                                   shell=True,                    # 返回的错误输出和标准输出输出到管道
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout=res.stdout.read()
            stderr=res.stderr.read()
            total_size=len(stdout)+len(stderr)
            header={'total_size':total_size,'MD5':'123456','msg_type':'cmd_res'}  # 自定义报头信息
            header_json=json.dumps(header)
            header_json_bytes=bytes(header_json,encoding='utf-8')
            header_size=struct.pack('i',len(header_json_bytes))
            
            if not client_data: break   # 如果收到的消息为空就跳出循环(主要针对在Linux系统上，客户端意外断开，
                                        # Linux的服务端出现无穷循环收空包的情况)
            conn.send(header_size)      # 发送头长度信息
            conn.send(header_json_bytes)  # 发送头信息
            conn.send(stdout)
            conn.send(stderr)
        except ConnectionResetError:    # 在 Windows系统上，客户端意外断开服务端会出现ConnectionResetError的异常
            break
    conn.close()  # 关闭链接

server.close()
