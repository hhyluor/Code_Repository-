# 定义共享的 fixture

import pytest
import requests


@pytest.fixture()
def baidu_resp():
    resp = requests.get('http://www.baidu.com')
    return resp


@pytest.fixture(autouse=True)
def auto_fixture():
    print('auto fixture')
