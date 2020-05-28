# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/5/28
# Note  : 观察者模式

"""
意图：定义对象间的一种一对多的依赖关系，当一个对象的状态发生改变时，所有依赖于它的对象都得到通知被自动更新

订阅-发布模式


参与者：
Subject:目标
目标知道他的观察者，可以有任意个观察者观察同一个目标
提供注册和删除观察的接口

Observer：观察者
定义一个更新接口，当目标有变化时，通知观察者

ConcreteSubject: 具体的目标

ConcreteObserver: 具体的观察者

"""


class Subject(object):

    def __init__(self):
        self.observer_list = []

    def add_observer(self, observer):
        self.observer_list.append(observer)

    def remove_observer(self, observer):
        self.observer_list.remove(observer)

    def notify(self):
        for observer in self.observer_list:
            observer.update(self)


class Observer(object):

    def __init__(self):
        pass

    def update(self, subject):
        print 'Observer.update', subject


class StudentObserver(Observer):
    def update(self, subject):
        print 'StudentObserver.update', subject


class TeacherObserver(Observer):
    def update(self, subject):
        print 'TeacherObserver.update', subject


if __name__ == '__main__':
    so = StudentObserver()
    to = TeacherObserver()

    s = Subject()
    s.add_observer(so)
    s.add_observer(to)

    s.notify()
