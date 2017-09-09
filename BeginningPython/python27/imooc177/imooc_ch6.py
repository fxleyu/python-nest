# 6.1
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59,
    'Paul': 73
}

# 6.2
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print 'Adam:', d.get('Adam')
print 'Lisa:', d['Lisa']
print 'Bart:', d['Bart']

# 6.3
d = {
    95 : 'Adam',
    85 : 'Lisa',
    59 : 'Bart'
}


# 6.4
d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart'
}
d[72] = 'Paul'


# 6.5
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for name in d:
    print name + ":", d[name]

print d

# 6.6
s = set(['Adam', 'Lisa', 'Bart', 'Paul'])

# 6.7
s = set(['Adam', 'Lisa', 'Bart', 'Paul','adam', 'lisa', 'bart', 'paul'])
print 'adam' in s
print 'bart' in s

# 6.8
months = set(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
    print 'x1: ok'
else:
    print 'x1: error'

if x2 in months:
    print 'x2: ok'
else:
    print 'x2: error'

# 6.9
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print x[0] + ":", x[1]

# 6.10
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for name in L:
    if name in s:
        s.remove(name)
    else:
        s.add(name)
print s

print s
