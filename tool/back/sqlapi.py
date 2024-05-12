import requests
import json
from global_var import *
import time

gId = ''

def query(url, data, getDbs, getTables, dumpTable, db, tbl):
    # delete(url, data, getDbs, getTables, dumpTable, db, tbl)
    return f(url, data, getDbs, getTables, dumpTable, db, tbl)
    return

# def delete(url, data, getDbs, getTables, dumpTable, db, tbl):
#     if getTaskID() != '':
#         gId = getTaskID()
#         response = requests.get(url=f'http://127.0.0.1:7000/admin/{gId}/flush')
#         if response.status_code == 200:
#             time.sleep(1)
#             create(url, data, getDbs, getTables, dumpTable, db, tbl)
#     return

def f(url0, data0, getDbs, getTables, dumpTable, db, tbl):
    try:
        response = requests.get(
        url='http://127.0.0.1:7000/task/new')

        if response.status_code == 200:
            time.sleep(1)
            id = response.json().get('taskid')
            response2 = requests.post(
            url=f'http://127.0.0.1:7000/option/{id}/set',
            data=json.dumps({'url': url0, 
                            'data': data0,
                            'getDbs':getDbs,
                            'getTables':getTables,
                            'dumpTable':dumpTable,
                            'db':db,
                            'tbl':tbl,
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
                    return response4
    except:
        print("can not extract database.....")