# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/5/28
# Note  : 中介者模式

"""
意图：用一个中介者对象来封装一系列的对象交互，中介者使各对象不需要显示地相互引用，从而使其耦合松散，而且可以独立地改变
他们之间的交互

参与者：
Mediator: 中介者
中介者定义一些接口用于与各同事对象通信

ConcreteMediator: 具体中介者

Colleague class：同事 类
每一个同事类都知道它的中介者
每一同事对象在需要与其他同事通信时，与它的中介者通信
"""


class Widget(object):
    def __init__(self, mediator):
        self.mediator = mediator

    def changed(self):
        self.mediator.widget_changed(self)


class Button(Widget):
    def __init__(self, mediator):
        super(Button, self).__init__(mediator)


class EntryField(Widget):

    def __init__(self, mediator):
        super(EntryField, self).__init__(mediator)


class DialogMediator(object):

    def widget_changed(self, widget):
        raise NotImplementedError


class FontDialogMediator(DialogMediator):

    def __init__(self):
        self.btn_ok = Button(self)
        self.entry_field = EntryField(self)

    def widget_changed(self, widget):
        if widget == self.btn_ok:
            print 'widget_changed', widget
        elif widget == self.entry_field:
            print 'widget_changed', widget
