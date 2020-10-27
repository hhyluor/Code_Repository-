# 定义 fixture
# @pytest.fixture()
# def fixture_name():
#    .....
# 使用
# def test_baidu(和 fixture 同名的参数):
#      参数的值是 fixture 函数的返回值

import pytest
import requests


@pytest.fixture()
def baidu_response():
    resp = requests.get('http://www.baidu.com')
    print(resp.status_code)
    return resp


def test_baidu_status_code(baidu_response):
    # baidu_response = baidu_response()
    print(baidu_response)
    assert baidu_response.status_code == 200, '状态码不是 200'
