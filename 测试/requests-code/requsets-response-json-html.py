# 1. 发起请求
# 2. 判断响应体是否是 json 格式
# 3. resp.json() 如果服务器的结果不是 json格式那么会报错


import requests

url = 'http://www.baidu.com'

resp = requests.get(url)

print(resp.text)
resp.json()