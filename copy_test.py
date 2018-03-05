#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: copy_test.py
@time: 2018/1/24 16:28
"""

# l1 = [3, [1,2], 5]
# l2 = l1[:]                  # 潜copy
# print l1 == l2
# print l1 is l2
#
# l1.append(6)                # 不会修
# print l2, l1
#
# l1[1].append(6)             # 修改 l1[1] 和l2[1] 指向同一个对象
# print l2, l1
#
# l1[1].remove(1)             # 修改 l1[1] 和l2[1] 指向同一个对象
# print l2, l1
#
# l1[1] += [7,8]              # 修改 l1[1] 和l2[1] 指向同一个对象,  针对可变对象， += 就地修改列表
# print l2, l1

import copy

# class Bus:
#     def __init__(self, passengers=None):
#         if passengers is None:
#             self.passengers = []
#         else:
#             self.passengers = list(passengers)          # 浅复制
#
#     def pick(self, name):
#         self.passengers.append(name)
#
#     def drop(self, name):
#         self.passengers.remove(name)
#
#
# bus1 = Bus(['Alice', 'Bile', 'Claire', 'David'])
#
# bus2 = copy.copy(bus1)              # 浅copy  表示bus2 是bus1的浅copy的副本 passengers指向同一个列表
#
# bus3 = copy.deepcopy(bus1)          # 深copy 表示 bus2是bus1的深复制副本， passengers是另一个列表
#
# print id(bus1), id(bus2), id(bus3), 1
# print id(bus1.passengers), id(bus2.passengers), id(bus3.passengers),2
#
# bus1.drop('Bile')
#
# print bus2.passengers, 3
# print bus3.passengers, 4
#
# bus2.pick('laol1')
# print bus1.passengers, 5
# print bus2.passengers, 6
# print bus3.passengers, 7
#
# bus3.drop('David')
# print bus1.passengers, 8
# print bus2.passengers, 9
# print bus3.passengers, 10


##################################

a = [1, 2]
b = [a, 3]
a.append(b)
# print a
#
# c = copy.deepcopy(a)
# print c

for i in a:
    print i, 1