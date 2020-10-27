# setup_class 类方法,在所有测试方法执行之前被调用,只会被调用一次
# teardown_class 类方法,在所有测试方法执行之后被调用,只会被调用一次
# setup_method 在每个测试方法执行之前被调用
# teardown_method 在每个测试方法执行之后被调用


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

    def test_1(self):
        print('test_1')

    def test_2(self):
        print('test_2')

    def test_3(self):
        print('test_3')
