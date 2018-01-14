# 类和实例
# class Student(object):
#     pass
#
#
# bart = Student()
# print(bart)
#
# bart.name = 'Bart Simson'
# print(bart.name)
#
# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.name, self.score))
#
#     def get_grade(self):
#         if self.score >= 90:
#             return 'A'
#         elif self.score >= 60:
#             return 'B'
#         else:
#             return 'C'
#
#
# bart = Student('Bart Simpson', 59)
# print(bart.name, bart.score)
# bart.print_score()
#
# lisa = Student('Lisa', 99)
# bart = Student('Bart', 59)
# print(lisa.name, lisa.get_grade())
# print(bart.name, bart.get_grade())


# 访问限制
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s :%s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

# 参数检查
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('bart', 59)

#  继承和多态
class Animal(object):
    def run(self):
        print('Animal is running...')



class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()


a = list()
b = Animal()
c = Dog()


def run_twice(animal):
    animal.run()
    animal.run()

class Timer(object):
    def run(self):
        print('Start...')

run_twice(Timer())
#不用子类有run方法也可以.



# 获取对象实例
print(type(123))
print(type('123'))
print(type(123.123))
print(type(abs))
print(type(type))
if type(123) == type(455):
    print('yes')

if type(123) == int:
    print('yes')

# 对于class的继承关系来说，使用type()就很不方便。
# 我们要判断class的类型，可以使用isinstance()函数。
a = Animal()
b = Dog()
print(isinstance(a,Animal))
print(isinstance(123 ,str))
print(isinstance([1, 2, 3], (list, tuple)))

# 使用dir()
#q返回对象所有属性和方法
print(dir('abc'))

print(len('abc'))
print('abc'.__len__())

class Myobject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x

obj = Myobject()
print(hasattr(obj,'x'))
print(obj.x)
print(hasattr(obj,'y'))
setattr(obj,'y',19)
print(hasattr(obj,'y'))
print(obj.y)
print(getattr(obj, 'z', 404))

# 实例属性和类属性
class Student(object):
    name  = 'Student'

s = Student()
print(s.name)
print(Student.name)
s.name = 'Michael'
print(s.name)
print(Student.name)
del s.name # 如果删除实例的name属性
print(s.name)

