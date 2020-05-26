# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/5/26
# Note  : 建造者模式
import abc


class Product(object):
	"""产品类，由不同的部件组成"""
	def __init__(self):
		self.parts = []

	def add(self, part):
		self.parts.append(part)

	def show_product(self):
		for part in self.parts:
			print part


class Builder(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def build_part_a(self):
		raise NotImplementedError

	@abc.abstractmethod
	def build_part_b(self):
		raise NotImplementedError

	def get_result(self):
		raise NotImplementedError


class ConcreteBuilder1(Builder):
	def __init__(self):
		self.product = Product()

	def build_part_a(self):
		self.product.add('part a')

	def build_part_b(self):
		self.product.add('part b')

	def get_result(self):
		return self.product


class ConcreteBuilder2(Builder):
	def __init__(self):
		self.product = Product()

	def build_part_a(self):
		self.product.add('part aa')

	def build_part_b(self):
		self.product.add('part bb')

	def get_result(self):
		return self.product


class Director(object):
	def construct(self, builder):
		builder.build_part_a()
		builder.build_part_b()


if __name__ == '__main__':
	director = Director()
	cb1 = ConcreteBuilder1()
	cb2 = ConcreteBuilder2()
	director.construct(cb1)
	cb1.get_result().show_product()

	director.construct(cb2)
	cb2.get_result().show_product()
