# requests 发起请求

# 导入 requests 包
# requests.[get|post|put](url)
import requests

get_url = 'https://postman-echo.com/get'

resp = requests.get(get_url)

print(resp)

post_url = 'https://postman-echo.com/post'
resp = requests.post(post_url)
print(resp)
