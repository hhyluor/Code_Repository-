# @pytest.fixture(scope='function')
# scope='function' 每一个引用该 fixture 的测试用例执行之前,fixture 函数都会被调用

import pytest


@pytest.fixture(scope='function')
def baidu_resp():
    print('baidu resp')
    return 'ok'


def test_1(baidu_resp):
    print('test 1')


def test_2(baidu_resp):
    print('test 2')
