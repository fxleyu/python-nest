f = open("file.txt", "w+")
f.write("Hello world!")
# f.close()
print f
ls = f.read()
print ls
'''
for line in ls:
    print line
'''
