#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: pass_setter.py
@time: 2018/2/5 14:23
"""
class Test(object):

    def __init__(self, name):
        self.name = name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password + 50


t = Test("校长")
t.password = 10000
print t.password

