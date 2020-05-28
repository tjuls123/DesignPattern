# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/5/28
# Note  : 访问者模式

"""
意图：表示一个作用于某对象结构中的各元素的操作。它使你可以在不改变各 元素的类的前提下定义作用于这些 元素的新操作

参与者：
Visitor: 访问者

ConcreteVisitor: 具体的访问者

Element: 元素
定义一个accept操作，它以一个访问者为参数

ConcreteElement：具体的元素
实现accept操作
ObjectStructure:对象结构

"""


class Visitor(object):

    def visit_element_a(self, element):
        raise NotImplementedError

    def visit_element_b(self, element):
        raise NotImplementedError


class ConcreteVisitor(Visitor):
    def visit_element_a(self, element):
        pass

    def visit_element_b(self, element):
        pass


class Element(object):

    def accept(self, visitor):
        raise NotImplementedError


class ConcreteElementA(Element):

    def accept(self, visitor):
        print 'ConcreteElementA.accept', visitor
        visitor.visit_element_a(self)


class ConcreteElementB(Element):

    def accept(self, visitor):
        print 'ConcreteElementB.accept', visitor
        visitor.visit_element_b(self)
