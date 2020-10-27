# fixture 中
# yield 语句之前的代码相当于 setup
# 之后的代码相当于 teardown
# yield 变量,变量作为 fixture 的返回值,传递给测试方法

import pymysql
import pytest


@pytest.fixture()
def data():
    # 建立数据库连接
    # 查询数据
    # yield 数据
    # 关闭连接
    print('连接建立')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='meiduo_mall')

    cursor = conn.cursor()
    query = 'select * from tb_users'
    cursor.execute(query)

    data = cursor.fetchall()

    yield data

    cursor.close()
    conn.close()
    print('连接关闭')


def test_data(data):
    print(data)
