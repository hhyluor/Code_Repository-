# yaml.dump(数据字典,写入方式打开的文件)
import yaml

data = {'Search_Data': {
    'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
    'search_test_001': {'expect': [4, 5, 6], 'value': 456}
}
}

with open('./data_write.yaml', 'w') as f:
    yaml.dump(data, f, allow_unicode=True)
