

# 4.1
L = ['Adam', 95.5, 'Lisa', 85, 'Bart', 59]
print L

# 4.2
L = [95.5,85,59]
print L[0]
print L[1]
print L[2]
#print L[3]

# 4.3
L = [95.5,85,59]
print L[-1]
print L[-2]
print L[-3]

# 4.4
L = ['Adam', 'Lisa', 'Bart']
L.insert(2, 'Paul')
print L

# 4.5
L = ['Adam', 'Lisa', 'Paul', 'Bart']
#L.pop(2)
L.pop(3)
L.pop(2)
print L

# 4.6
L = ['Adam', 'Lisa', 'Bart']
L[0] = 'Bart'
L[-1] = 'Adam' 
print L

# 4.7
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print t

# 4.8
t = ('Adam', )
print t

# 4.9
#t = ('a', 'b', ['A', 'B'])
t = ('a', 'b', ('A', 'B'))
print t