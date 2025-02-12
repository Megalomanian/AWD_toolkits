import socket  # 导入socket模块，用于网络通信
from collections import deque  # 导入deque模块，用于创建双端队列
# import sendflag  # 可能用于发送标志的模块，当前被注释掉


def start_server(host='0.0.0.0', port=1111):
    # 创建一个最大长度为500的双端队列，用于存储接收到的消息
    received_messages = deque(maxlen=500)
    
    # 创建一个TCP/IP套接字
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # 绑定套接字到指定的主机和端口
        server_socket.bind((host, port))
        # 开始监听传入的连接，最多允许5个未处理的连接
        server_socket.listen(5)
        print(f"Listening on {host}:{port}...")
        
        while True:
            # 接受一个新的连接
            client_socket, client_address = server_socket.accept()
            with client_socket:
                #print(f"Connection from {client_address}")  # 打印连接的客户端地址
                while True:
                    # 接收数据，最大字节数为1024
                    data = client_socket.recv(1024)
                    if not data:
                        break  # 如果没有数据，跳出循环
                    # 将接收到的数据解码为字符串
                    message = data.decode('utf-8')
                    
                    # 检查消息是否已经接收过
                    if message in received_messages:
                        a = 1  # 占位操作，可能用于处理重复消息
                        #print("Duplicated")  # 打印重复消息的提示
                    else:
                        print(f"Received: {message}")  # 打印接收到的消息
                        #sendflag.post_method(message)  # 可能用于发送消息的POST方法
                        #sendflag.get_method(message)  # 可能用于发送消息的GET方法
                        # 将消息添加到已接收消息的队列中
                        received_messages.append(message)
                    
                    # 向客户端发送确认消息
                    client_socket.sendall(b"Message received")

if __name__ == "__main__":
    start_server()  # 如果脚本是直接运行的，则启动服务器
