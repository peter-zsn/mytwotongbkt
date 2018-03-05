#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: letgo.py
@time: 2018/2/7 10:22
"""

import requests
import time
import json

rank_url = "https://pet-chain.baidu.com/data/market/queryPetsOnSale"

cookies = {
    "BAIDUID": "E5A7011A426CDCEBFCED8AA7701E02F0",
    "FG": "1",
    "PSTM": "1516244043",
    "BIDUPSID": "C5C0C133A99819A931601B4FA988F563",
    "__cfduid": "dcc6e770e9089682069e4006dad152e451516841884",
    "BDORZ": "B490B5EBF6F3CD402E515D22BCDA1598",
    "BDUSS":"lhNeU1vZWpsZlIzdlJOUElmVXJ6bXJOUXdvVDdvclkwN2o3M29MNGpSOTNvNkJhQVFBQUFBJCQAAAAAAAAAAAEAAA"
            "AeJmqacHl0aG9u1cUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHcWeVp3Fnlab",
    "H_PS_PSSID": "25638_1463_21085_18560_17001_20927",
    "PSINO":"1",
    "BDRCVFR[feWj1Vr5u3D]": "I67x6TjHwwYf0",
    "locale": "zh"
}

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) '
                  'AppleWebKit/602.1.50 (KHTML, like Gecko) '
                  'CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
    "Host": "pet-chain.baidu.com",
    "Origin": "pet-chain.baidu.com",
    "Content-Type": "application/json"
}

data = {
    "appId": 3,
    "lastAmount": "",
    "lastRareDegree": "",
    "pageNo": 1,
    "pageSize": 10,
    "petIds":"",
    "querySortType": "AMOUNT_ASC",
    "requestId": int(time.time()),
    "tpl": "wallet"
}


r = requests.post(rank_url, data=data, cookies=cookies, headers=headers)
print r.status_code
