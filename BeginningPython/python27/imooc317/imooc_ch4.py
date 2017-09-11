# -*- coding: utf-8 -*-

'''
Created on 2017年9月11日

@author: 朱智慧
'''
# 4.2
class Person0:
    def __init__(self):
        pass

xiaoming = Person0()
xiaohong = Person0()

print xiaoming
print xiaohong
print xiaoming == xiaohong

# 4.3
p1 = Person0()
p1.name = 'Bart'

p2 = Person0()
p2.name = 'Adam'

p3 = Person0()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1, lambda p1,p2: cmp(p1.name, p2.name))

print L2[0].name
print L2[1].name
print L2[2].name

# 4.4
class Person1:
    def __init__(self, name, gender, brith, **kw):
        self.name = name
        self.gender = gender
        self.brith = brith
        for k, v in kw.iteritems():
            setattr(self, k, v)

xiaoming = Person1('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job

# 4.5
class Person2(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

p = Person2('Bob', 59)

print p.name
# print p.__score

# 4.6
class Person3(object):
    count = 0
    def __init__(self, name):
        Person3.count += 1
        self.name = name

p1 = Person3('Bob')
print Person3.count

p2 = Person3('Alice')
print Person3.count

p3 = Person3('Tim')
print Person3.count

# 4.7
class Person4(object):
    __count = 0
    def __init__(self, name):
        Person4.__count = Person4.__count + 1
        self.name = name
        print Person4.__count

p1 = Person4('Bob')
p2 = Person4('Alice')

#print Person.__count

# 4.8
class Person5(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_grade(x):
        if x.__score >= 80:
            return 'A'
        if x.__score >= 60:
            return 'B'
        return 'C'

p1 = Person5('Bob', 90)
p2 = Person5('Alice', 65)
p3 = Person5('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()


# 4.9
class Person6(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person6('Bob', 90)
print p1.get_grade
print p1.get_grade()

# 4.10
class Person7(object):
    count = 0
    @classmethod
    def how_many(cls):
        return cls.count
    def __init__(self, name):
        self.name = name
        Person7.count = Person7.count + 1

print Person7.how_many()
p1 = Person7('Bob')
print Person7.how_many()

class Person(object):
    __count = 0
    @classmethod
    def how_many(cls):
        return cls.__count
    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1

print Person.how_many()
p1 = Person('Bob')
print Person.how_many()

def calc_prod(lst):
    def prod(x,y):
        return x * y
    def f():
        return reduce(prod,lst)
    return f
 
f = calc_prod([1, 2, 3, 4])
print f()