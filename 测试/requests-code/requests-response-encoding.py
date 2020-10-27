# resp.text 通过 resp.content.decode(编码)
# 编码是 requests 自己猜测的,编码可能和原始的网站编码个是不一致,那么会出现乱码
# 手动修改编码格式 resp.encoding ='utf-8' ;resp.text=resp.content.decode('utf-8')


import requests

resp = requests.get('http://www.baidu.com')
print(resp.encoding)
text = resp.text
print(text)

print('自定义编码格式')

resp.encoding = 'utf-8'
text = resp.text
print(text)
