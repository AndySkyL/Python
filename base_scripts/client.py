
import socket
import struct
import json

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('192.168.20.180',8080))

while True:
    send_data=input(">>: ").strip()
    if not send_data: continue        # 禁止输入空，防止死锁
    client.send(send_data.encode('utf-8'))  # 发送的文件为bytes类型
    header_size=client.recv(4)
    header_json_lens=struct.unpack('i',header_size)[0]
    header_json_bytes=client.recv(header_json_lens)
    header_json=json.loads(header_json_bytes.decode('utf-8'))
    total_size=header_json['total_size']
    file_MD5=header_json['MD5']
    print(file_MD5)
    data_size=0
    server_data=b''
    while total_size > data_size:
        server_data+=client.recv(1024)
        data_size=len(server_data)

    print(server_data.decode('gbk'))   # 在windows上，系统命令的返回结果为GBK格式
client.close()
