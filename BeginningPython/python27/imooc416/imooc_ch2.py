import os

f = open("file.txt", "w+")
f.write("Hello world!")
# f.close()
print f
#f = open("file.txt")
print f.tell()
f.seek(-1, os.SEEK_CUR)
ls = f.read()
print ls
'''
for line in ls:
    print line
'''
list_f = []
for i in range(20352):
    f = open("file.txt")
    list_f.append(f)
    #print "%d : %d" % (i, f.fileno())

'''
508 : 511
Traceback (most recent call last):
  File "D:\GitRepo\python-nest\BeginningPython\python27\imooc416\imooc_ch2.py", line 14, in <module>
IOError: [Errno 24] Too many open files: 'file.txt'
'''