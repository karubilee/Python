print('Hello world')

# 使用__shots__
class Student1(object):
    pass


s = Student1()
s.name = 'Michael'
print(s.name)

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)
#太小的项目不值得用??>

# @property
s = Student1()
s.scrore = 9999
# 不合理


class Student(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value<0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


s = Student()
s.set_score(60)
print(s.get_score())

# s.set_score(999)

class Student2(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100!')
        self._score = value


class Student3(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

s2 = Student2()
s2.score = 99

# 上面的birth是可读写属性，
# 而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

# 多重继承

class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass

# 各种动物
class Animal(object):
    pass


# 大类:
class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Runnable(object):
    def run(self):
        print('Running')


class Flyable(object):
    def fly(self):
        print('Flying')


# 各种动物
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird):
    pass


# 定制类
class Student4(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__

print(Student4('Michael'))

s4 = Student4('Lb')

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


for n in Fib():
    print(n)


class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, item):
        if attr == 'score':
            return 99

