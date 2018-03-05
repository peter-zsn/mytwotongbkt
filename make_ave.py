#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: make_ave.py 局部变量 修改   ==3 中的nonloacl
@time: 2018/1/23 11:07
"""

class NameSpace:
    pass

def make_ave():

    count = 0
    total = 0

    ns = NameSpace()
    ns.count = 0
    ns.total = 0
    def ave(value):
        """python 3中的用法，把变量转换成自用变量"""
        # nonlocal count, total
        # count += 1
        # total += value
        ns.count += 1
        ns.total += value

        return ns.total / ns.count
    return ave

ave = make_ave()
print ave(1)
print ave(2)
print ave(10)