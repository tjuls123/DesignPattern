# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/5/26
# Note  : 代理模式

"""
意图：为其他对象提供一种代理以控制对这个对象的访问

1.远程代理：为不同地址空间的提供局部访问
2.虚代理：根据需要创建开销很大的对象
3.保护代理：控制访问权限
4.智能指引

参与者：
Proxy:


Subject:
定义realSubject和Proxy的公用接口，这样在任何使用realSubject的地方也可以使用Proxy

realSubject
"""

import abc


class Subject(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def request(self):
        raise NotImplementedError


class Proxy(Subject):

    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        self.real_subject.request()


class RealSubject(Subject):

    def request(self):
        print 'RealSubject'

