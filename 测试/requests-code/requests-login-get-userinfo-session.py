# session = requests.Session()
# session.[get|post|put...](url, ...) 和 requests 参数一样

from requests import Session

session = Session()

print(session.cookies)

# 登录

auth = {
    'username': 'admin',
    'password': 'admin1234'
}
url = 'http://localhost:8000/login/'
resp = session.post(url, json=auth)

print(session.cookies)
print(resp.json())

# 获取用户信息

url = 'http://localhost:8000/info/'
resp = session.get(url)
print(resp.json())

