# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/4/29
# Note  : 职责链模式

"""
意图：使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系，将这些对象连成一条链，并且沿着这条链传递请求，直到有一个
对象处理它为止

参与者：
Handler：
定义一个处理请求的接口
实现后继链

ConcreteHandler：
具体负责处理请求
可访问后继者
如果可以处理，那么处理请求，否则传递给后继
"""


class Handler(object):

	def __init__(self, next_handler=None):
		self.next_handler = next_handler

	def set_next_handler(self, next_handler):
		self.next_handler = next_handler

	def get_next_handler(self):
		return self.next_handler

	def handle_request(self, request):
		pass


class ConcreteHandler1(Handler):
	def __init__(self, next_handler=None):
		super(ConcreteHandler1, self).__init__(next_handler)

	def handle_request(self, request):
		if request == 'request1':
			print 'ConcreteHandler1 handle the %s' % request
		elif self.next_handler:
			self.next_handler.handle_request(request)


class ConcreteHandler2(Handler):
	def __init__(self, next_handler=None):
		super(ConcreteHandler2, self).__init__(next_handler)

	def handle_request(self, request):
		if request == 'request2':
			print 'ConcreteHandler2 handle the %s' % request
		elif self.next_handler:
			self.next_handler.handle_request(request)


if __name__ == '__main__':
	ch2 = ConcreteHandler2()
	ch1 = ConcreteHandler1(ch2)

	ch1.handle_request('request2')
	ch1.handle_request('request1')
