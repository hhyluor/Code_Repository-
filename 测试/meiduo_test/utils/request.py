# url_prefix
# 1. 读取 server.yaml
#   {'shema':',,,',"domain":"...","port":"..."}
#   http://localhost:8000
import requests

from meiduo_test.utils.data import YamlData



def get_url_prefix():
    data = YamlData.load('server.yaml')
    url_prefix = f"{data['schema']}://{data['domain']}:{data['port']}"
    return url_prefix


# 改造请求方法,requests.[get|post...](url)
# def get(path, **kwargs):
#      """path='/login/'"""
#      url_prefix= get_url_prefix()
#      url =  f'{url_prefix}{path}'
#      resp = requests.get(url, **kwargs)
#      return resp
def default_func(url, **kwargs):
    raise NotImplementedError('没有改方法')


def request(method, path, **kwargs):
    """

    :param method: 请求方法
    :param path: 接口路径,例如: /login/
    :param kwargs:
    :return:
    """
    url_prefix = get_url_prefix()
    url = f'{url_prefix}{path}'
    # 获取 requests 的属性
    request_func = getattr(requests, method, default_func)
    resp = request_func(url, **kwargs)
    return resp


def get(path, **kwargs):
    """

    :param path: 接口路径,例如: /login/
    :param kwargs:
    :return: resp
    """
    return request('get', path, **kwargs)


def post(path, **kwargs):
    """

    :param path: 接口路径,例如: /login/
    :param kwargs:
    :return: resp
    """
    return request('post', path, **kwargs)


def delete(path, **kwargs):
    """

    :param path: 接口路径,例如: /login/
    :param kwargs:
    :return: resp
    """
    return request('delete', path, **kwargs)
