# setup_function 每个测试函数执行之前被调用
# teardown_function 每个测试函数执行之后被调用

def setup_function():
    print('setup function')


def teardown_function():
    print('teardown function')


def test_1():
    print('test 1')


def test_2():
    print('test 2')


def test_3():
    print('test 3')
