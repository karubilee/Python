import math

help(abs)
print(abs(-199))
help(max)
print(max(3, 65, 64.999))
print(int('123'))
print(float('12.34'))
print(str(12.34))
print(bool(1))
print(bool(''))
print('asdasd')
a = abs
a(-1)


def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(10))

print(my_abs(-10))


def nop():
    pass


# abs('1')
# print(my_abs('1'))


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

# 函数的参数


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))
# 一 必选参数在前,默认参数在后,否则python的解释器会报错,
# 二 是如何设置默认参数,当函数有多个参数时,把变化大的参数放前面,变化小的参数放后面,
# 变化小的参数就可以作为默认参数.


def enroll(name, gender, age=6, city='Beijing'):
    print('name', name)
    print('gender', gender)
    print('age', age)
    print('city', city)
    print('end')

enroll('Sarah', 'F')
enroll('bob', 'F', 8)
enroll('Ann', 'M', city='sz')


def add_end(L=[]):
    L.append('END')
    return L


print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
print(add_end([1, 2, 3]))

def add_end2(L=None):
    if L is None:
        L = []
    L.append('End')
    return L


print(add_end2())
print(add_end2())

#  可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
numArr = [1, 2, 3, 4]
print(calc(*numArr))

# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age', age, 'other', kw)


person('Michael', 30)
person('Mike', 40, city='sz')


extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24,**extra)

# 命名关键字参数
def person1(name, age, **kw):
    if 'city' in kw:
        #有city参数
        return
    if 'job' in kw:
        #有job参数
        pass
    print('name:', name, 'age:', age, 'other', kw)


person1('Jack', 24, city='beijing', zipcode='engineer')


def person2(name, age, *, city, job):
    print(name, age, city, job)


person2('ooxx', 19, city='sz',job='student')


def person3(name, age, *, city='sz', job):
    print(name, age, city, job)


person3('Jack', 55, job='Engineer')

# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、
# 可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：
# 必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


def f1(a, b, c=0, *args, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'kw = ', kw)


f1(1, 2)
f1(1,2,c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 8888)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d' : 88, 'x': '#'}
f2(*args, **kw)

# 小结
# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#
# 默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#
# 要注意定义可变参数和关键字参数的语法：
#
# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
#
# 以及调用函数时如何传入可变参数和关键字参数的语法：
#
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
#


# 递归函数

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)


print(fact(100))












