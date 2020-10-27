import pytest


def check_password(password):
    """
    检查密码是否合法

    :param password: 长度是 8 到 16
    :return:
    """
    pwd_len = len(password)
    if pwd_len < 8:
        return False
    elif pwd_len > 16:
        return False
    else:
        return True


# pytest.fixtrure(params=[参数 1,参数 2,....]) # 遍历 params 列表
# def fixture_name(request):
#     .....
#     return request.param # 返回当前的参数

# def test_xxx(fixture_name):


@pytest.fixture(params=['1234567', '12345678', '123456789', '1234567890123456', '12345678901234567'])
def password(request):
    return request.param


def test_password(password):
    print(password)
    print(check_password(password))
