# 1. 发起请求
# 2. 判断响应体是否是 json 格式
# 3. resp.json() 返回字典

import requests

url = 'https://postman-echo.com/ip'

resp = requests.get(url)

dict_data = resp.json()
print(type(dict_data))
print(dict_data)
