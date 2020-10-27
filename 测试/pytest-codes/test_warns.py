import pytest

# 前置被测试代码
import warnings


def make_warn():
    # 抛出异常
    warnings.warn("deprecated", DeprecationWarning)


def not_warn():
    pass


def user_warn():
    warnings.warn("user warn", UserWarning)


# with pytest.warns(预期的警告):
#    被测试的代码

def test_dep_warn():
    with pytest.warns(DeprecationWarning):
        make_warn()


def test_no_warn():
    with pytest.warns(DeprecationWarning):
        not_warn()


def test_user_warn():
    with pytest.warns(UserWarning):
        user_warn()
