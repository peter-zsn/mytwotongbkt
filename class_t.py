#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: class_t.py
@time: 2018/1/26 11:29
"""

class Test:
    D = 1
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod   # 返回函数的静态方法。该方法不强制要求传递参数
    def sta_test(a, b):
        print a, b

    def saas(self):
        print 'sasa'

    @classmethod    # 修饰符对应的函数不需要实例化 第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等
    def cla_test(cls):
        print cls.D
        cls.sta_test(5, 6)

test = Test(1, 2)
test.saas()
test.sta_test(3, 4)
test.cla_test()

Test.cla_test()
Test.sta_test(7, 8)