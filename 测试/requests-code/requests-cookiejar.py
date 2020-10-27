# jar = requests.cookies.RequestsCookieJar() 生成 cookie
# jar.set(key,value) 可以设置多个
# requests.get(url, cookies=jar)


import requests
from requests.cookies import RequestsCookieJar

jar = RequestsCookieJar()

jar.set('my-cookie-1', 'my-value-1')
jar.set('my-cookie-2', 'my-value-2')

url = 'https://postman-echo.com/cookies'

resp = requests.get(url, cookies=jar)

print(resp.content)

dict_data = resp.json()
print(dict_data)
