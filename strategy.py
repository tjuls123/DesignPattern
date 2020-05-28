# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/5/28
# Note  : 策略模式

"""
意图：定义一系列算法，把他们一个个封装起来，并且使它们可相互替换，本模式使得算法可独立于使用它的客户而变化




参与者：
Strategy: 策略
定义所支持算法的公共接口，

ConcreteStrategy：具体的算法策略

Context：上下文

"""


class Strategy(object):

    def discount(self, price):
        raise NotImplementedError


class HalfDiscountStrategy(Strategy):
    def discount(self, price):
        return price * 0.5


class FullMinusStrategy(Strategy):
    def discount(self, price):
        if price >= 20:
            return price - 10
        return price


class Context(object):
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        self.strategy = strategy

    def discount(self, price):
        if self.strategy:
            return self.strategy.discount(price)
        return price
