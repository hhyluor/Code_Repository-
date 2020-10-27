# 捕获异常对象
# 同时匹配异常类和异常对象的消息


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


# 捕获异常对象
# with pytest.raises(预期的异常类) as 变量: 变量中存储的是捕获的异常对象

def test_leap_year_store():
    with pytest.raises(ValueError) as val_err:
        is_leap_year(0)

    print(val_err.type)


# 同时匹配异常类和异常对象的消息
# with pytest.raises(预期的异常类,match='消息匹配')
def test_leap_year_match():
    with pytest.raises(ValueError, match='传入的参数不是整数'):
        is_leap_year(-100)
