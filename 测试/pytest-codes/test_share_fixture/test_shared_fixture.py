# 定义测试方法,引用共享的 fixture


def test_1():
    print('test 1')


class TestFixture():
    def test_2(self, baidu_resp):
        print(baidu_resp)
        print('test 2')

    def test_3(self, baidu_resp):
        print(baidu_resp)
        print('test 3')

    def test_4(self):
        print('test 4')
