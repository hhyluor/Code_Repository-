# 发送查询字符串数据

# 1. 通过 requests.[get|post|...](url, params= 字典)
# 2. 手动拼接 url 'http://www.example.com?a=1&b=2'

import requests

url = 'https://postman-echo.com/get'

params = {
    'a': 1,
    'b': 2,
    'c': [3, 4]
}
resp = requests.get(url, params=params)
dict_data = resp.json()
print(dict_data)

print('手动拼接 url')

url = 'https://postman-echo.com/get?d=5&e=6&f=7&f=8'
resp = requests.get(url)
dict_data = resp.json()
print(dict_data)
