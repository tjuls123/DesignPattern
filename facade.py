# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/5/26
# Note  : 外观模式

"""
意图：为子系统中的一组接口提供一个一致的界面，facade模式定义了一个高层接口，这个接口使得这一子系统更加容易使用
让外部通过facade与内部子系统进行通信



参与者：
Facade:
知道哪些子系统负责处理请求
将客户的请求代理给适当的子对象

Subsystem
"""


class Facade(object):

    def compile(self):
        s = Scanner()
        s.scan()

        p = Parser()
        p.parse()


class Scanner(object):

    def scan(self):
        print 'scan'


class Parser(object):
    def parse(self):
        print 'parse'


if __name__ == '__main__':
    c = Facade()
    c.compile()



