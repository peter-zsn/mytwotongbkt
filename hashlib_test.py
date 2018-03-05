#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: hashlib_test.py
@time: 2018/2/3 9:15
"""

import random
import hashlib

def get_random_string(length=12,
                      allowed_chars='abcdefghijklmnopqrstuvwxyz'
                                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    return ''.join(random.choice(allowed_chars) for i in range(length))


def sha1_encode_password(password, salt=''):
    if not salt:
        salt = get_random_string()
    print salt
    hash = hashlib.sha1(salt + password).hexdigest()
    return "sha1$%s$%s" % (salt, hash)



if __name__ == "__main__":
    password = '111111'
    a = sha1_encode_password(password)
    print a

    en_pass = 'sha1$3ctCHmMFQajN$1084aaead829bd8c510dd77ac2bf87e84625a755'
    algorithm, salt, hash = en_pass.split('$', 2)
    print algorithm, salt, hash
    b = sha1_encode_password(password, salt)
    print b