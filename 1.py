#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: 1.py
@time: 2018/1/18 13:48
"""

import threading
import requests
import json

url = 'https://mapi.m.jxtbkt.cn/account/login/web'
token = 'NDgwMDAyfTA0MDY3NTk4MDh9MDQwOTIzNzkwNA'
code_2 = 0
code_4 = 0

with open('1.json') as f:
    config = f.read()
    DATABASES_CONFIG = json.loads(config)

data = DATABASES_CONFIG['RECORDS']


class Test(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.data = i
    def run(self):
        global code_2, code_4
        username = self.data['username']
        password = self.data['password']

        r = requests.post(url, data={'username': username, "password":password})
        if r.status_code == 200:
            print r.json()['message']
            code_2 += 1
        if r.status_code == 500:
            print 111, username, password
            print r.json()['message'].encode('utf-8')
            code_4 += 1
        if r.status_code not in (200, 500):
            print r.status_code
if __name__ == "__main__":
    Th = []
    for i in range(len(data)):
        test = Test(data[i])
        Th.append(test)
    for t in Th:
        t.start()
    for t in Th:
        t.join()
    print code_4
    print code_2
    print 'over'