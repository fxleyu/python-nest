# 5.1
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    
    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name

student = Student("fxleyu", "man", 99)
print student.name

# 5.2
class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
    
    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name

t = Teacher('Alice', 'Female', 'English')
print t.name
print t.course

'''
Traceback (most recent call last):
  File "D:\GitRepo\python-nest\BeginningPython\python27\imooc317\imooc_ch5.py", line 23, in <module>
    t = Teacher('Alice', 'Female', 'English')
  File "D:\GitRepo\python-nest\BeginningPython\python27\imooc317\imooc_ch5.py", line 20, in __init__
    super(Person, self).__init__(name, gender)
TypeError: object.__init__() takes no parameters

>>>> super(Person, self) is object, object.__init__()
'''

# 5.3
t = Teacher('Alice', 'Female', 'English')

print isinstance(t, Person)
print isinstance(t, Student)
print isinstance(t, Teacher)
print isinstance(t, object )

# 5.4
def who_am_i(x):
    print x.whoAmI()

p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')

who_am_i(p)
who_am_i(s)
who_am_i(t)

# 5.5
import json

class Students(object):
    def read(self):
        return r'["Tim", "Bob", "Alice"]'

s = Students()

print json.load(s)

# 5.6
class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(BasketballMixin, Student):
    pass

class FTeacher(FootballMixin, Teacher):
    pass
'''
s = BStudent()
print s.skill()

t = FTeacher()
print t.skill()
'''

# 5.7
class Person1(object):
    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for k, v in kw.iteritems():
            setattr(self, k, v)

p = Person1('Bob', 'Male', age=18, course='Python')
print p.age
print p.course