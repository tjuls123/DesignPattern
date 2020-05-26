# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/5/26
# Note  : 适配器模式

"""
将一个类的接口转换成客户希望的另一个接口。Adapter模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作
有两种适配方式：
1.类适配器：通过多重继承，其中有一个是private继承(c++)
2.对象适配器：通过对象组合

参与者：
Target：
定义Client使用的与特定领域相关的接口

Adaptee:
已经存在的接口，这个接口需要适配

Adapter：
对Adaptee的接口进行适配，使之能用于Target
"""

"""类适配器"""


class Target(object):
	def request(self):
		print '普通请求'


class Adaptee(object):
	def specific_request(self):
		print '特殊的请求'


class Adapter(Target, Adaptee):

	# 适配旧的specific_request接口，让其适应新的request接口
	def request(self):
		return self.specific_request()  # 调用已有的类接口


