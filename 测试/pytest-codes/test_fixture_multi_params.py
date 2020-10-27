# username 和 password 都是 params
# def test_xxx(username,password)
# 此方法会执行 len(usernames) * len(passwords) 笛卡尔积

import pytest


@pytest.fixture(params=['admin', 'root', 'super'])
def username(request):
    return request.param


@pytest.fixture(params=['1234', '12345', '123456', '1234567'])
def password(request):
    return request.param


def test_username_password(username, password):
    print(f'username: {username}====password: {password}')
