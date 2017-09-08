
# 5.1
score = 3;
if score >= 60 :
    print 'passed'
    
# 5.2
score = 55
if score >= 60:
    print 'passed'
else:
    print 'failed'

# 5.3
score = 85

if score >= 90:
    print 'excellent'
elif score >= 80:
    print 'good'
elif score >= 60:
    print 'passed'
else:
    print 'failed'

# 5.4
L = [75, 92, 59, 68]
sum = 0.0
for item in L:
    sum += item
print sum / 4

# 5.5
sum = 0
x = 1
while x <= 100:
    sum += x
    x += 1
print sum

# 5.6
sum = 0
x = 1
n = 1
while True:
    if n > 20:
        break
    if n != 1:
        x *= 2
    sum += x
    n += 1
print sum

sum = 0
x = 1
n = 1
while True:
    if n > 20:
        break
    sum = sum + x
    x = x * 2
    n = n + 1
print sum

# 5.7
sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break
    if x % 2 == 0:
        continue
    sum += x
print sum

# 5.8
for x in [ 1,2,3,4,5,6,7,8,9 ]:
    for y in [0,1,2,3,4,5,6,7,8,9]:
        if x < y:
            print x * 10 + y