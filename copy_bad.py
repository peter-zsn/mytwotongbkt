#coding=utf-8

"""
@varsion: ??
@author: 张帅男 ---- 不能使用可变参数作为参数的默认值
@file: copy_bad.py
@time: 2018/1/25 10:04
"""
# class BadBus:
#     def __init__(self, passengers=[]):
#         self.passengers = passengers
#
#     def pick(self, name):
#         self.passengers.append(name)
#
#     def drop(self, name):
#         self.passengers.remove(name)

class BadBus:
    def __init__(self, passengers=None):
        if passengers is not None:
            self.passengers = passengers
        else:
            self.passengers = []

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

bus1 = BadBus(['A', 'B'])

print bus1.passengers, 1

bus1.pick('C'), 2
bus1.drop('A'), 3
print bus1.passengers

bus2 = BadBus()
print bus2.passengers, 4

bus2.pick('D')
print bus1.passengers, 5
print bus2.passengers, 6


bus3 = BadBus()
print bus3.passengers, 7