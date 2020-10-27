# 1. 发起请求
# 2. 判断响应体是否是 json 格式
#   2.1 是 json json.loads(content)
#   2.2 打印消息
import json

import requests

url = 'https://postman-echo.com/ip'

resp = requests.get(url)

headers = resp.headers

content_type = headers.get('Content-Type', 'null')  # content_type

if 'application/json' in content_type:
    content = resp.content

    dict_data = json.loads(content)
    print(type(dict_data))
    print(dict_data)
else:
    print(f'content-type: {content_type}')


