# 静态Web服务器-多任务版

**学习目标**

* 能够写出多线程版的多任务web服务器程序

---

### 1. 静态Web服务器的问题

目前的Web服务器，不能支持多用户同时访问，只能一个一个的处理客户端的请求，那么如何开发多任务版的web服务器同时处理多个客户端的请求?

可以使用**多线程**，比进程更加节省内存资源。

**多任务版web服务器程序的实现步骤:**

1. 当客户端和服务端建立连接成功，创建子线程，使用子线程专门处理客户端的请求，防止主线程阻塞。
2. 把创建的子线程设置成为守护主线程，防止主线程无法退出。

### 2. 静态Web服务器-多任务版的示例代码

```py
import socket
import threading


# 处理客户端的请求
def handle_client_request(new_socket):
    # 代码执行到此，说明连接建立成功
    recv_client_data = new_socket.recv(4096)
    if len(recv_client_data) == 0:
        print("关闭浏览器了")
        new_socket.close()
        return

    # 对二进制数据进行解码
    recv_client_content = recv_client_data.decode("utf-8")
    print(recv_client_content)
    # 根据指定字符串进行分割， 最大分割次数指定2
    request_list = recv_client_content.split(" ", maxsplit=2)

    # 获取请求资源路径
    request_path = request_list[1]
    print(request_path)

    # 判断请求的是否是根目录，如果条件成立，指定首页数据返回
    if request_path == "/":
        request_path = "/index.html"

    try:
        # 动态打开指定文件
        with open("static" + request_path, "rb") as file:
            # 读取文件数据
            file_data = file.read()
    except Exception as e:
        # 请求资源不存在，返回404数据
        # 响应行
        response_line = "HTTP/1.1 404 Not Found\r\n"
        # 响应头
        response_header = "Server: PWS1.0\r\n"
        with open("static/error.html", "rb") as file:
            file_data = file.read()
        # 响应体
        response_body = file_data

        # 拼接响应报文
        response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
        # 发送数据
        new_socket.send(response_data)
    else:
        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 响应头
        response_header = "Server: PWS1.0\r\n"

        # 响应体
        response_body = file_data

        # 拼接响应报文
        response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
        # 发送数据
        new_socket.send(response_data)
    finally:
        # 关闭服务与客户端的套接字
        new_socket.close()


# 程序入口函数
def main():
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口号复用, 程序退出端口立即释放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    # 绑定端口号
    tcp_server_socket.bind(("", 9000))
    # 设置监听
    tcp_server_socket.listen(128)

    while True:
        # 等待接受客户端的连接请求
        new_socket, ip_port = tcp_server_socket.accept()
        print(ip_port)
        # 当客户端和服务器建立连接程，创建子线程
        sub_thread = threading.Thread(target=handle_client_request, args=(new_socket,))
        # 设置守护主线程
        sub_thread.setDaemon(True)
        # 启动子线程执行对应的任务
        sub_thread.start()


if __name__ == '__main__':
    main()

```

### 3. 小结

1. 当客户端和服务端建立连接成功，创建子线程，使用子线程专门处理客户端的请求，防止主线程阻塞。

    ```py
    while True:
        conn_socket, ip_port = tcp_server_socket.accept()
        # 开辟子线程并执行对应的任务
        sub_thread = threading.Thread(target=handle_client_request, args=(conn_socket,))
    ```
    
2. 把创建的子线程设置成为守护主线程，防止主线程无法退出。

    ```py
    # 开辟子线程并执行对应的任务
    sub_thread = threading.Thread(target=handle_client_request, args=(conn_socket,))
    sub_thread.setDaemon(True) # 设置守护主线程
    sub_thread.start()
    ```







