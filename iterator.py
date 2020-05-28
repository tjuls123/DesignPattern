# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/5/28
# Note  : 迭代器模式

"""
意图：提供一个方法顺序访问一个聚合对象中各个元素，而又不需要暴露该对象的内部表示

迭代器需要由相应的聚合对象去创建，因为只有聚合对象知道如何迭代自己

参与者：
Iterator：
定义访问和遍历元素的接口

ConcreteIterator：
具体迭代器实现迭代器接口

Aggregate:
聚合定义创建相应迭代的接口

ConcreteAggregate:
具体的聚合对象
"""
