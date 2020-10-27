# pytest.mark.run(order=整数值)
# 同为正数或者负数,越小优先级越高

import pytest


@pytest.mark.run(order=2)
def test_1():
    print('test 1')


@pytest.mark.run(order=1)
def test_2():
    print('test 2')
