# session.headers 字典
# session.[get|post....] 发起请求会自动携带 session.headers
# session.headers 有默认值

# session.[get|post....](url ,header=临时请求头), 临时请求头不会更新到 session.headers中


from requests import Session

session = Session()
print(session.headers)  # 有默认请求头

# 自定义请求头
session.headers['Auth-Token'] = 'xxxxxyyyyytoken'
print(session.headers)


url = 'https://postman-echo.com/headers'

resp = session.get(url)
print(resp.content)
print(resp.json())

# 临时请求头

resp = session.get(url, headers={'my-header': 'my-value'})
print(resp.content)
print(resp.json())

print(session.headers)
