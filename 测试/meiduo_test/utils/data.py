import os
import yaml

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取绝对路径


# # os.path.join(BASE_DIR, 'data' ,'users/username.yaml')
#
# def get_yaml_path(file_rel_path):
#     """
#
#     :param file_rel_path:  users/username.yaml
#     :return:
#     """
#     file_abs_path = os.path.join(BASE_DIR, 'data', file_rel_path)
#     with open(file_abs_path) as f:
#         data = yaml.load(f)
#         return data
#

# 读取数据,类的方式

class YamlData():

    @classmethod
    def load(cls, file_rel_path):
        """
        读取 yaml 数据文件
        :param file_rel_path: users/username.yaml
        :return:
        """
        file_abs_path = os.path.join(BASE_DIR, 'data', file_rel_path)#拼接路径
        with open(file_abs_path) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)#解析Yaml
            return data
