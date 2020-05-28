# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/5/28
# Note  : 模板方法

"""
意图：定义一个操作中的算法骨架，而将一些步骤延迟到子类中，模板方法使得子类不改变一个算法的框架，而重新定义一些算法的某些特定步骤


参与者：
AbstractClass: 抽象类
定义抽象的原语操作，具体的子类将重新定义它以实现一个算法，

ConcreteClass: 具体的实现类

"""
import abc


class Animal(object):
    __metaclass__ = abc.ABCMeta

    def one_day(self):
        self.eat()
        self.rest()
        self.bathe()
        self.sleep()

    def eat(self):
        raise NotImplementedError

    def rest(self):
        raise NotImplementedError

    def bathe(self):
        raise NotImplementedError

    def sleep(self):
        raise NotImplementedError


class Human(Animal):
    def eat(self):
        pass

    def rest(self):
        pass

    def bathe(self):
        pass

    def sleep(self):
        pass
