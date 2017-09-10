# -*- coding: utf-8 -*-
'''
Created on 2017年9月10日

@author: 朱智慧
'''
import math
import functools

# 2.3
def add(x, y, f):
    return f(x) + f(y)

print add(25, 9, math.sqrt)


# 2.4
def format_name(s):
    s = s.lower()
    return s[0].upper() + s[1:]

print map(format_name, ['adam', 'LISA', 'barT'])

# 2.5
def prod(x, y):
    return x * y

print reduce(prod, [2, 4, 5, 7, 12])

# 2.6
def is_sqr(x):
    num = math.sqrt(x)
    return num * 10 % 10 == 0

print filter(is_sqr, range(1, 101))

def is_sqr_imooc(x):
    r = int(math.sqrt(x))
    return r*r==x
print filter(is_sqr_imooc, range(1, 101))

# 2.7
def cmp_ignore_case(s1, s2):
    x = s1.upper()
    y = s2.upper()
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

# 2.8
def calc_prod(lst):
    def calc_prod_delay():
        result = 1.0
        for l in lst:
            result *= l
        return result
    return calc_prod_delay

f = calc_prod([1, 2, 3, 4])
print f()

def calc_prod_imooc(lst):
    def lazy_prod():
        def f(x, y):
            return x * y
        return reduce(f, lst, 1)
    return lazy_prod
f = calc_prod_imooc([1, 2, 3, 4])
print f()

# 2.9
# ***********
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()

# 2.10
def is_not_empty(s):
    return s and len(s.strip()) > 0
print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

print filter(lambda s : s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])


# 2.12
## 要让 @log 自适应任何参数定义的函数，可以利用Python的 *args 和 **kw，保证任意个数的参数总是能正常调用：
import time

def performance_1(f):
    def fn(*args):
        start = time.time()
        result = f(*args)
        print 'call %s() in %fs' % (f.__name__, (time.time() - start))
        return result
        
    return fn

@performance_1
def factorial_1(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial_1(1202)

# 2.13
'''
def performance(unit):
    def performance_2(f):
        def fn(*args, **kw):
            start = time.time()
            result = f(*args, **kw)
            print '[%s]call %s() in %fs' % (unit, f.__name__, (time.time() - start))
            return result
        return fn
    return performance_2
'''
def performance_2(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return r
        return wrapper
    return perf_decorator


@performance_2('ms')
def factorial_2(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial_2(10)

# 2.14
def log(f):
    @functools.wraps(f)
    def wrapper(*args, **kw):
        print 'call...'
        return f(*args, **kw)
    return wrapper
@log
def f2(x):
    pass
print f2.__name__

def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial.__name__

# 2.15
'''
sorted_ignore_case = functools.partial(sorted, cmp=cmp_ignore_case)
'''
sorted_ignore_case = functools.partial(sorted, cmp=lambda s1, s2: cmp(s1.upper(), s2.upper()))
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])
print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])


