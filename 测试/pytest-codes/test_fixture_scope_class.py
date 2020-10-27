# @pytest.fixture(scope='class')
# scope='class' 在整个类当中,fixture 只会被执行一次

import pytest


@pytest.fixture(scope='class')
def baidu_resp():
    print('baidu_resp')
    return 'ok'


class TestBaidu():

    def test_1(self, baidu_resp):
        print(baidu_resp)
        print('test 1')

    def test_2(self, baidu_resp):
        print(baidu_resp)
        print('test 2')
