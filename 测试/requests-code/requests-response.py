# 响应状态码、响应头、响应体
# 1. 发起请求 requests.[method](url) 返回响应对象
# 2. resp.status_code  响应状态码
# resp.headers 响应头
# resp.content 字节码数据
# resp.text 字符串


import requests

resp = requests.get('http://www.baidu.com')

status_code = resp.status_code
print(f'响应状态码:{status_code}')

headers = resp.headers  # 字典

print('响应头')
print(headers)

bytes_body = resp.content  # 响应体的字节码类型

print('字节码数据')
print(bytes_body)

text = resp.text  # 字符串格式 ; resp.content.decode(编码:utf-8)
print(text)
