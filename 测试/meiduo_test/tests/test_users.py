# 测试用户名是否重复接口
# 有多个用户名要测试,借助于参数化,pytest.mark.parametrize([,,],[,,,])

import pytest

from meiduo_test.utils.data import YamlData
from meiduo_test.utils.request import get


# 读取测试的数据
# 编写测试用例

def get_names():
    data = YamlData.load('users/username.yaml')
    # data =  {"path":"...","names":["xxx", .....]}
    # [(path,name),(path,name)]
    return [(data['path'], name) for name in data['names']]


@pytest.mark.parametrize(['path', 'name'], get_names())  # [(path,name),(path,name)]
def test_name_count(path, name):
    # 测试用户名接口
    # 发起请求(path,name)
    # 验证响应状态码
    # 验证 code
    # 验证 count
    # path  = "/usernames/{username}/count/"
    # "{P}".format(P=1213)
    real_path = path.format(username=name)
    resp = get(real_path)
    assert resp.status_code == 200
    dict_data = resp.json()
    assert dict_data['code'] == 0


