# setup_module ,整个模块只会被调用一次,在所有测试函数以及所有的测试类之前被调用
# teardown_module ,整个模块只会被调用一次,在所有测试函数以及所有的测试类之后被调用


def setup_module():
    print('setup module 整个模块只会被调用一次,在所有测试函数以及所有的测试类之前被调用')


def teardown_module():
    print('teardown moudle 整个模块只会被调用一次,在所有测试函数以及所有的测试类之后被调用')


def setup_function():
    print('setup function')


def teardown_function():
    print('teardown function')


def test_1():
    print('test 1')


def test_2():
    print('test 2')


class TestUpDown():
    @classmethod
    def setup_class(cls):
        print('setup class 在所有测试方法执行之前被调用')

    @classmethod
    def teardown_class(cls):
        print('teardown class 在所有测试方法执行之后被调用')

    def setup_method(self):
        print('setup method 在每个测试方法执行之前被调用')

    def teardown_method(self):
        print('teardown method 在每个测试方法执行之后被调用')

    def test_3(self):
        print('test_3')

    def test_4(self):
        print('test_4')
