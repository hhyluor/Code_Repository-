import pytest


# 前置被测试代码
def is_leap_year(year):
    # 先判断year是不是整型
    if isinstance(year, int) is not True:
        raise TypeError("传入的参数不是整数")
    elif year == 0:
        raise ValueError("公元元年是从公元一年开始！！")
    elif abs(year) != year:
        raise ValueError("传入的参数不是正整数")
    elif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("%d年是闰年" % year)
        return True
    else:
        print("%d年不是闰年" % year)
        return False


# 目标: is_leap_year('sxxx') 预期函数抛出 TypeError
# with pytest.raises(预期的异常类: TypeError):
#       调用被测试的代码 is_leap_year('sxxx')


def test_leap_year():
    with pytest.raises(TypeError):
        is_leap_year('xxxxx')


def test_lear_year_2():
    with pytest.raises(ValueError):
        is_leap_year('xxxxx')
