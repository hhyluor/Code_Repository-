# 测试方法标记为预期失败
# 一般可能在被测试的代码还没有完成的情况,打标记

# @pytest.mark.xfail(condition=bool 表达式,reason=原因)

import pytest


def upgrade_python_to_4():
    raise NotImplemented('xxxx')


@pytest.mark.xfail(condition=True, reason='python 目前最高版本是 3.9')
def test_upgrade_python_to_4():
    upgrade_python_to_4()
