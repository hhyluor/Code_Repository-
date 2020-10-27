# import yaml
# yaml.load(open(yaml 文件,'r'))


import yaml

with open('./data.yaml', 'r') as f:
    data = yaml.load(f)
    print(data)
