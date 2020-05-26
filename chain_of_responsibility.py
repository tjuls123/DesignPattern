# -*- coding:utf-8 -*-
# Author: lsn5884@corp.netease.com
# Date  : 2020/4/29
# Note  :


class Handler(object):

	def __init__(self, next_handler=None):
		self.next_handler = next_handler

	def set_next_handler(self, next_handler):
		self.next_handler = next_handler

	def get_next_handler(self):
		return self.next_handler

	def handle_request(self, request):
		pass

