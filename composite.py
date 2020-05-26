# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/5/26
# Note  : 组合模式

"""
将对象组合成树形结构以表示‘部分-整体’的层次结构，Composite使得用户对单个对象和组合对象的使用具有一致性

Composite模式的关键是一个抽象类，它既可以表示基本图元，也可以表示图元的容器

参与者：
Component
为组合中的对象申明接口
在适当的情况下，实现所有类共有接口的缺省行为
申明一个接口用于管理子组件

Leaf:
表示叶子节点，定义图元的行为

Composite：
管理子组件
"""


class Component(object):
    def __init__(self, name):
        self.name = name

    def add(self, component):
        """Composite 的管理子节点的方法，添加component"""
        raise NotImplementedError

    def remove(self, component):
        """移除component"""
        raise NotImplementedError

    def show_name(self):
        """叶子节点的具体方法"""
        print self.name


class LeafComponent(Component):
    def __init__(self, name):
        super(LeafComponent, self).__init__(name)

    def add(self, component):
        raise NotImplementedError

    def remove(self, component):
        raise NotImplementedError


class Composite(Component):
    def __init__(self, name):
        super(Component, self).__init__(name)
        self.child_components = []

    def add(self, component):
        self.child_components.append(component)

    def remove(self, component):
        self.child_components.remove(component)


if __name__ == '__main__':
    c = Composite('Composite1')
    c.add(LeafComponent('component1'))
    c2 = Composite('Composite2')
    c.add(c2)
    c2.add(LeafComponent('asdf'))



