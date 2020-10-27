# 发送 cookies
# requests.[get|post...](url , cookies=字典)


import requests

url = 'https://postman-echo.com/cookies'

cookies = {
    'my-cookie-1': 'my-cookie-1-value',
    'my-cookie-2': 'my-cookie-2-value'
}

resp = requests.get(url, cookies=cookies)

print(resp.content)

dict_data = resp.json()

print(dict_data)
