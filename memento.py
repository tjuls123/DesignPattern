# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/5/28
# Note  : 备忘录

"""
意图：在不破坏封装的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态，这样以后就可将该对象回复到 原先保存的状态

一个备忘录是一个对象，它存储另一个对象在某个瞬间的内部状态，，后者称为备忘录的原发器，只有原发器可以向备忘录存取信息，备忘录对其他对象不可见

1.必须保存一个对象在某一时刻的状态，以便后面恢复
2.如果用一个接口直接获取对象状态，会暴露对象的实现细节并且破坏对象的封装性


参与者：
Memento: 备忘录
备忘录存储原发器的内部状态
防止原发器以外的对象访问备忘录（友元类)

Originator:原发器
原发器创建一个备忘录，用以保存当前的状态
使用备忘录恢复状态

Caretaker: 负责人
负责保存备忘录
不能对备忘录的内容进行修改和获取


"""


class State(object):
    def __init__(self):
        self.name = ''
        self.score = 0
        self.id_card = 12


class Originator(object):
    def __init__(self):
        self.state = State()

    def create_memento(self):
        return Memento(self.state)

    def set_memento(self, memento):
        self.state = memento.get_state()


class Memento(object):

    def __init__(self, state):
        self.state = state

    # 只允许Originator访问，其他对象不能访问，C++私有函数+友元类
    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state
