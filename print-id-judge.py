#!/usr/bin/python3
try:
	with open("ans.txt") as f:
		print(f.read(), end="")
except:
	print(u"ans.txt文件不存在")
