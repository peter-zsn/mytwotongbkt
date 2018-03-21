#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: token_test.py
@time: 2018/1/24 9:08
"""
import time
import hashlib
import base64
import random

# token = 'mdq3nzmwox0wnda2mzm5mjg3fta0mdkxmji0mda'
token = 'Njc1NzE1OX0wNDMxMjM3NjY0fTA0MzQzNTI1MDU'
# token = 'MzU3NDkzOX0wNDA2MjczMTMwfTA0MDQ3NDc2Nzk'

SECRET_KEY = '*****'

def strxor(s, key):
    "异或加密"
    key = key & 0xff
    a = bytearray(s)
    b = bytearray(len(a))
    for i, c in enumerate(a):
        b[i] = c ^ key
    return str(b)


def create_checkcode(user_id, expire_time):
    """
    快速计算session校验码
    """
    return user_id ^ expire_time ^ int(SECRET_KEY)


def decode_token(token):
    if not token:
        return
    # try:
        # 填充base64被去掉的等号
    token += '=' * (-len(token)%4)
    token = base64.b64decode(token)
    print token, 11111111111
    token = strxor(token, int(SECRET_KEY))
    print token, 22222
    user_id, expire_time, code = token.split('|')
    user_id = int(user_id)
    expire_time = int(expire_time)
    code = int(code)
    print user_id, expire_time, code
    # except Exception, e:
    #     print e
    #     return
    print time.localtime(expire_time)
    nowt = time.time()
    if nowt > expire_time:
        print 3333333333
        return
    checkcode = create_checkcode(user_id, expire_time)
    if code != checkcode:
        return
    return {'user_id':user_id, 'expire':expire_time}


print decode_token(token)
