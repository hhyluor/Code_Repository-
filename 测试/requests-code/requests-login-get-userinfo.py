# 1. 登录
# resp = requests.post(url, json=字典)
# resp.content 查看请求结果
# 2. 获取用户信息
# resp = requests.get(url)
# resp.content 查看用户信息

import requests

# 登录
auth = {
    'username': 'admin',
    'password': 'admin1234'
}
url = 'http://localhost:8000/login/'
resp = requests.post(url, json=auth)
content = resp.content
dict_data = resp.json()
print(dict_data)

# 获取用户信息
url = 'http://localhost:8000/info/'
resp = requests.get(url)
dict_data = resp.json()
print(dict_data)
