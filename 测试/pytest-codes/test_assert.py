# assert bool表达式 [,msg]

import requests


def test_baidu():
    # 请求百度
    # 判断状态码是否 200
    url = 'http://www.baidu.com'
    resp = requests.get(url)
    print(resp.status_code)

    assert resp.status_code == 100, '状态码不是 100'


