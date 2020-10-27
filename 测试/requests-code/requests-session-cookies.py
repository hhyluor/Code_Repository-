# session.cookies 类似于字典结构
from requests import Session

session = Session()

print(session.cookies)

# 添加 cookie
session.cookies['my-cookie'] = 'my-value'
print(session.cookies)

# 修改
session.cookies['my-cookie'] = 'my-value-updated'
print(session.cookies)

del session.cookies['my-cookie']
print(session.cookies)
