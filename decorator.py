# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/5/26
# Note  : 装饰模式

"""
意图：动态的给一个对象添加一些额外的职责，就增加功能来说，decorator模式相比于生成子类更加灵活



参与者：
Component
定义一个对象接口，可以给这些对象动态的添加职责

ConcreteComponent:
定义一个对象，可以给这个对象添加一些职责

Decorator：
维持一个指向Component的指针，并定义一个与Component接口一致的接口

ConcreteDecorator:
具体的Decorator
"""

import abc


class Component(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def draw(self):
        raise NotImplementedError

    @abc.abstractmethod
    def resize(self):
        raise NotImplementedError


class ConcreteComponent(Component):
    def draw(self):
        print 'draw ConcreteComponent'

    def resize(self):
        print 'resize ConcreteComponent'


class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def draw(self):
        self.component.draw()

    def resize(self):
        self.component.resize()


class ConcreteDecorator(Decorator):
    def __init__(self, component):
        super(ConcreteDecorator, self).__init__(component)

    def draw(self):
        super(ConcreteDecorator, self).draw()
        print 'draw ConcreteDecorator'  # 额外的职责

    def resize(self):
        super(ConcreteDecorator, self).resize()
        print 'resize ConcreteDecotator'


if __name__ == '__main__':
    cc = ConcreteComponent()
    cd = ConcreteDecorator(cc)
    cd.draw()
    cd.resize()

