# pytest --reruns n n是重新测试的次数

def test_1():
    print('test 1')
    assert False, '故意失败'
