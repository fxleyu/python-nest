# 7.2
L = []
x = 1
while x <= 100:
    L.append(x * x)
    x += 1
print sum(L)

# 7.3
def square_of_sum(L):
    sum = 0
    for num in L:
        sum += num * num
    return sum
    

print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])

# 7.4
import math

def quadratic_equation(a, b, c):
    x1 = (-b - math.sqrt(b*b -4*a*c)) * 1.0 / (2 * a) 
    x2 = (-b + math.sqrt(b*b -4*a*c)) * 1.0 / (2 * a) 
    return x1, x2

print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)

# 7.5
def move(n, a, b, c):
    if n ==1:
        print a, '-->', c
        return
    move(n-1, a, c, b)
    print a, '-->', c
    move(n-1, b, a, c)
move(4, 'A', 'B', 'C')

# 7.6
# OK:
def fn1(a, b=1, c=2):
    pass
# Error:
# SyntaxError: non-default argument follows default argument
# def fn2(a=1, b):
    pass

def greet(name='world'):
    print "hello, " + name + "."

greet()
greet('Bart')

# 7.7
def average(*args):
    print args
    sum = 0.0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)
print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)