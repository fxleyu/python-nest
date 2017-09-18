# -*- coding: utf-8 -*-
f = open('file.txt')

print f.fileno() # 文件描述符
print f.mode  # 文件打开权限
print f.encoding # 文件的编码格式
print f.closed # 文件是否关闭

import sys 
print sys.stdin.encoding
print sys.stdin.mode

# 3.1
f = open("imooc.txt", "w")
a = unicode.encode(u'慕课', 'utf-8')
print a
f.write(a)
f.close()