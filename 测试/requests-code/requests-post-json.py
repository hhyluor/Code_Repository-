# request.post(url,json=字典)

import requests

auth = {
    'username': 'admin',
    'password': 'admin1231231'
}

url = 'http://localhost:8000/login/'

resp = requests.post(url, json=auth)

print(resp.content)

dict_data=resp.json()
print(dict_data)
