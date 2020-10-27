# 发送自定义请求头
# requests.[get|post|put...](url, headers= 字典)

import requests

url = 'https://postman-echo.com/headers'

headers = {
    'my-header': 'my-header-value',
    'my-header2': 'my-header-value-2'
}

resp = requests.get(url, headers=headers)

print(resp.content)

dict_data = resp.json()
print(dict_data)
