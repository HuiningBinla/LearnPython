#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第1行和第2行是标准注释，
# 第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，
# 第2行注释表示.py文件本身使用标准UTF-8编码；

'a test module'
# 表示文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
__author__ = 'Michael Binla'

import sys

def test():
	args = sys.argv
	if len(args)==1:
		print("Hello,world!")
	elif len(args)==2:
		print("Hello, %s!" % args[1])
	else:
		print("Too many arguments!")
		
if __name__=="__main__":
	test()





