# 静态Web服务器-返回固定页面数据

**学习目标**

* 能够写出组装固定页面数据的响应报文

---

### 1. 开发自己的静态Web服务器

**实现步骤:**

1. 编写一个TCP服务端程序
2. 获取浏览器发送的http请求报文数据 
3. 读取固定页面数据，把页面数据组装成HTTP响应报文数据发送给浏览器。
4. HTTP响应报文数据发送完成以后，关闭服务于客户端的套接字。

### 2. 静态Web服务器-返回固定页面数据的示例代码

```py
import socket


if __name__ == '__main__':
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
        # 代码执行到此，说明连接建立成功
        recv_client_data = new_socket.recv(4096)
        # 对二进制数据进行解码
        recv_client_content = recv_client_data.decode("utf-8")
        print(recv_client_content)

        with open("static/index.html", "rb") as file:
            # 读取文件数据
            file_data = file.read()


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

        # 关闭服务与客户端的套接字
        new_socket.close()
```

### 3. 小结

1. 编写一个TCP服务端程序

   ```py
   tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   # 循环接受客户端的连接请求
   while True:
       conn_socket, ip_port = tcp_server_socket.accept()
   ```

2. 获取浏览器发送的http请求报文数据

   ```py
   client_request_data = conn_socket.recv(4096)
   ```

3. 读取固定页面数据，把页面数据组装成HTTP响应报文数据发送给浏览器。

   ```py
   response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
   conn_socket.send(response_data)
   ```
4. HTTP响应报文数据发送完成以后，关闭服务于客户端的套接字。

   ```py
   conn_socket.close()
   ```



