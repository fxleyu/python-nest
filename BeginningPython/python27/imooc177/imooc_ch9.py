# 9.1
for i in range(1,101):
    if i % 7 == 0:
        print i

# 9.2
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print index + 1, '-', name

L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(range(1, len(L)+1), L):
    print index, '-', name

# 9.3
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for score in d.itervalues():
    sum += score
print sum / len(d)

# 9.4
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for k, v in d.iteritems():
    sum = sum + v
    print k, ':', v
print 'average', ':', sum / len(d)