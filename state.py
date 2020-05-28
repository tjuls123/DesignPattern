# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/5/28
# Note  : 状态模式

"""
意图：允许一个对象在其内部状态改变时改变它的行为，对象看起来似乎修改了它的类


参与者：
Subject:目标
目标知道他的观察者，可以有任意个观察者观察同一个目标
提供注册和删除观察的接口

Observer：观察者
定义一个更新接口，当目标有变化时，通知观察者

ConcreteSubject: 具体的目标

ConcreteObserver: 具体的观察者

"""