# 6.2
class Person1(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student1(Person1):

    def __init__(self, name, gender, score):
        super(Student1, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(Student: %s, %s, %s)' % (self.name, self.gender, self.score)
    __repr__ = __str__

s = Student1('Bob', 'male', 88)
print s

# 6.3
class Student2(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def __cmp__(self, s):
        diff = s.score - self.score
        if diff == 0:
            return cmp(self.name, s.name) 
        else:
            return diff

L = [Student2('Tim', 99), Student2('Bob', 88), Student2('Alice', 99)]
print sorted(L)

# 6.4
class Fib(object):

    def __init__(self, num):
        self.num = num

    def __str__(self):
        result = [0,1]
        if self.num == 1:
            return [0]
        elif self.num == 2:
            return [0,1]
        else:
            for i in range(2, self.num):
                result.append(result[i-2] + result[i-1])
            return str(result)

    def __len__(self):
        return self.num
f = Fib(10)
print f
print len(f)

'''
class Fib(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)

    __repr__ = __str__

    def __len__(self):
        return len(self.numbers)

f = Fib(10)
print f
print len(f)
'''

# 6.5
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        g = gcd(self.p, self.q)
        return '%s/%s' % (self.p / g, self.q / g)
    
    
    def __int__(self):
        return self.p / self.q

    def __float__(self):
        return self.p * 1.0 / self.q
    
    __repr__ = __str__
'''
    def __float__(self):
        return float(self.p) / self.q
'''

r1 = Rational(1, 2)
r2 = Rational(1, 4)
print r1 + r2
print r1 - r2
print r1 * r2
print r1 / r2

# 6.6
print float(Rational(7, 2))
print float(Rational(1, 3))

# 6.7
class Student3(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score
    @property
    def grade(self):
        if self.score < 60:
            return 'C'
        if self.score < 80:
            return 'B'
        return 'A'
s = Student3('Bob', 59)
print s.grade
s.score = 60
print s.grade
s.score = 99
print s.grade

# 6.8
class Person(object):
    __slots__ = ('name', 'gender')
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    __slots__ = ('score',)
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print s.score

# 6.9
class Fib1(object):
    def __call__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        return L

f = Fib1()
print f(10)