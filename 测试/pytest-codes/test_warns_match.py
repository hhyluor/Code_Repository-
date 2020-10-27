# with pytest.warns(预期的警告类, match=匹配的消息内容)
# 两个条件同时成立,那么测试通过

import pytest
import warnings


def make_warn():
    warnings.warn('user warn', UserWarning)


def test_warn():
    with pytest.warns(UserWarning, match='user warn'):
        make_warn()
