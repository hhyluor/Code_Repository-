# with pytest.warns((预期警告类1,预期警告类2,...)) as record:
#     被测试代码
# record 类似于数组,数组中的元素是捕获的警告对象

import warnings
import pytest


def warn_message():
    warnings.warn("user", UserWarning)
    warnings.warn("runtime", RuntimeWarning)


def test_warns():
    with pytest.warns((UserWarning, RuntimeWarning)) as records:
        warn_message()

    print(len(records))
    print(records[0].message)
    print(records[1].message)
