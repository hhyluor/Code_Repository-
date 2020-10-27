#  @pytest.mark.parametrize(参数名, [参数值 1,参数值 2,....])
#  def test_xxx(self, 参数名)
# @pytest.mark.parametrize( [参数名1,参数名2,...], [ (参数值 1,参数值 2), (参数值 3,参数值 4),...])
# def test_yyy(self, 参数名1,参数名2,...)

import pytest


@pytest.mark.parametrize('a', [1, 2, 3])
def test_1(a):
    print(a)
    print('test 1')


@pytest.mark.parametrize(['a', 'b'], [(1, 2), (3, 4), (5, 6)])
def test_2(a, b):
    print(f"a: {a} b: {b}")
    print('test 2')
