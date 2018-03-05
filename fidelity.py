#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: fidelity.py    策略----简单的折扣策略
@time: 2018/1/22 15:06
"""

from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """积分1000以上提供5%折扣"""
    return order.total() * .05 if order.customer.fidelity >=100 else 0

def bulk_item_promo(order):
    """单个商品20个以上提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def laege_order_promo(order):
    """订单中的不同商品达到10个以上 7%的折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() *.07
    return 0

joe = Customer('laowang', 0)
ann = Customer('laoli', 1000)
cart = [LineItem('wawa', 2, 100),
        LineItem('bask', 23, 50),
        LineItem('mellon', 5, 5)]

a = Order(joe, cart, fidelity_promo)
print a

b = Order(ann, cart, fidelity_promo)
print b


c = Order(joe, cart, bulk_item_promo)
print c

d = Order(ann, cart, bulk_item_promo)
print d

promos = [fidelity_promo, bulk_item_promo, laege_order_promo]
def best_promo(order):
    """自动选择最佳折扣"""
    return max(promo(order) for promo in promos)

e = Order(joe, cart, best_promo)
print e

f = Order(ann, cart, best_promo)
print f
