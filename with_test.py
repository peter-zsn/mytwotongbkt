#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: with_test.py
@time: 2018/2/2 11:18
"""
import os, sys

class Test:
    def __enter__(self):
        print 'enter'
        return 1


    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'exit'

with Test() as t:
    print("111")

    print("222")
    print(t)