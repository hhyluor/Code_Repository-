# 导入 django.test.TestCase
from django.test import TestCase
# 导入 User 模型类
from users.models import User
from requests import Session

# 测试类必须继承自 TestCase
class UserTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        # print('Up class 整个类只执行一次,所有测试方法之前')
        #登录
        cls.session = Session()
        # data =  {
        #     'username': 'admin',
        #     'password': '123456abc',
        #     'remembered': True
        # }
        data =  {
            'username': 'admin',
            'password': '123456abc',
            'remembered': True
        }
        url = 'http://localhost:8000/login/'
        resp = cls.session.post(url, json=data)
        # 获取 json 响应
        result = resp.json()
        # 检查是否登录成功
        if result['code'] != 0:
            print('登录失败')

    @classmethod
    def tearDownClass(cls):
        # print('Down class 整个类只执行一次,所有测试方法之后')
        #退出
        # 退出登录
        url = 'http://localhost:8000/logout/'
        cls.session.delete(url)

    # # 在每一个测试方法执行之前被调用
    # def setUp(self):
    #     print('在每一个测试方法执行之前被调用')
    #
    # # 在每一个测试方法执行之后被调用
    # def tearDown(self):
    #     print('在每一个测试方法执行之前被调用')

    def test_info(self):
        # 调用获取用户信息接口
        url = 'http://localhost:8000/info/'
        resp = self.session.get(url)
        # 获取 json 响应
        result = resp.json()
        # 检查是否获取成功
        if result['code'] != 0:
            print('获取用户信息失败')
        else:
            print(result)

    # def test_history(self):
    #     # 调用获取用户浏览历史接口
    #     url = 'http://localhost:8000/browse_histories/'
    #     resp = self.session.get(url)
    #     # 获取 json 响应
    #     result = resp.json()
    #     # 检查是否获取成功
    #     if result['code'] != 0:
    #         print('获取用户浏览历史失败')
    #     else:
    #         print(result)

    def test_addresses(self):
        # 调用查看地址列表接口
        url = 'http://localhost:8000/addresses/'
        resp = self.session.get(url)
        # 获取 json 响应
        result = resp.json()
        # 检查是否获取成功
        if result['code'] != 0:
            print('获取地址列表失败')
        else:
            print(result)