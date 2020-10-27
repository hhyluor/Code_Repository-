# 跳过测试方法 pytest.mark.skip 强制跳过
# pytest.mark.skipif(condition=bool 表达式,reason) 有条件跳过, 原因必须给

import pytest


@pytest.mark.skip(reason='就是任性')
def test_1():
    print('test 1')
    assert 1 == 0


def test_2():
    print('test 2')
    assert 1 == 1


@pytest.mark.skipif(condition=True, reason='xxxx')
def test_3():
    print('test 3')
    assert 2 == 1
