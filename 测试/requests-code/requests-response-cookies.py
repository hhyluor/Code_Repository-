# resp.cookies 读取服务器颁发的 cookie


import requests

url = 'https://postman-echo.com/cookies'

resp = requests.get(url)

cookies = resp.cookies

print(cookies)
