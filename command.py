# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/5/28
# Note  : 命令模式

"""
意图：将 一个请求封装为一个对象，从而使你可用不同的请求对客户进行参数化，对请求排队或者记录请求日志，以及支持可撤销的操作
 如果将一个请求封装为对象，则很容易的可以把这个对象丢进一个队列里面，队列只管处理这个请求
Command模式是回调机制的一个面向对象的替代品，类似于c++的函数对象

参与者：
Command：
申明执行操作的接口

ConcreteCommand：
具体的实现者

Receiver:
接收者，知道如何执行一个命令
"""

import abc


class Application(object):
	def open(self):
		print 'Application.open'


class Document(object):
	def paste(self):
		print 'Document.paste'


class Command(object):

	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def execute(self):
		raise NotImplementedError


class OpenCommand(Command):

	def __init__(self, application):
		self.application = application

	def execute(self):
		self.application.open()


class PasteCommand(Command):
	def __init__(self, document):
		self.document = document

	def execute(self):
		self.document.paste()


class MacroCommand(Command):
	def __init__(self):
		self.child_command = []

	def execute(self):
		for command in self.child_command:
			command.execute()

	def add(self, command):
		self.child_command.append(command)

	def remove(self, command):
		self.child_command.remove(command)


if __name__ == '__main__':
	application = Application()
	document = Document()

	oc = OpenCommand(application)  # 将参数封装在对象中

	pc = PasteCommand(document)

	oc.execute()
	pc.execute()
