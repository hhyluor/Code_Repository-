# pytest.mark.usefixtures('应用 fixture 名称')
# def test_xx()
# 在 test_xx 执行 会先调用 fixture 函数

import pytest


@pytest.fixture()
def mkdir():
    print('mkdir')


@pytest.mark.usefixtures('mkdir')
def test_1():
    print('test 1')


@pytest.mark.usefixtures('mkdir')
def test_2():
    print('test 2')
