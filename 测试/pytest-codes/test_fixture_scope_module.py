# @pytest.fixture(scope='module')
# scope='module' 在整个模块中只会被调用一次

import pytest


@pytest.fixture(scope='module')
def baidu_resp():
    print('baidu resp')
    return 'ok'


def test_1(baidu_resp):
    print(baidu_resp)
    print('test 1')


def test_2(baidu_resp):
    print(baidu_resp)
    print('test 2')


class TestBaidu():

    def test_3(self, baidu_resp):
        print(baidu_resp)
        print('test 3')

    def test_4(self, baidu_resp):
        print(baidu_resp)
        print('test 4')
