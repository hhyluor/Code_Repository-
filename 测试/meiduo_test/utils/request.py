# url_prefix
# 1. 读取 server.yaml
#   {'shema':',,,',"domain":"...","port":"..."}
#   http://localhost:8000
import requests

from utils.data import YamlData



def get_url_prefix():#解析出封装地址端口
    data = YamlData.load('server.yaml')
    url_prefix = f"{data['schema']}://{data['domain']}:{data['port']}"
    return url_prefix


# 改造请求方法,requests.[get|post...](url)#封装请求方法和路径和地址
# def get(path, **kwargs):
#      """path='/login/'"""
#      url_prefix= get_url_prefix()
#      url =  f'{url_prefix}{path}'
#      resp = requests.get(url, **kwargs)
#      return resp
def default_func(url, **kwargs):#默认方法,没有找到属性时,调用此方法
    raise NotImplementedError('没有改方法')


def request(method, path, **kwargs):#封装多个请求与一体,减少重复代码
    """

    :param method: 请求方法
    :param path: 接口路径,例如: /login/
    :param kwargs:
    :return:
    """
    url_prefix = get_url_prefix()
    url = f'{url_prefix}{path}'
    # 获取 requests 的属性,是个函数,就是requests.method函数变量
    request_func = getattr(requests, method, default_func)
    #request_func = requests.method
    resp = request_func(url, **kwargs)
    # if method == "get":
    #     resp = requests.get(url, **kwargs)
    # elif method == "post":
    #     resp = requests.post(url, **kwargs)
    # elif method == "delete":
    #     resp = requests.delete(url, **kwargs)
    # else:
    #     print('方法不支持')
    #     return None
    # return resp
    return resp


def get(path, **kwargs):
    """

    :param path: 接口路径,例如: /login/
    :param kwargs:
    :return: resp
    """
    return request('get', path, **kwargs)#调用封装的request,形成了多态.


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
