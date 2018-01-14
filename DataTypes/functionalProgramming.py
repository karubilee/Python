# # 高阶函数
#
# # 变量可以指向函数
# f = abs
# print(f(-10))
# print(abs(-10))
#
# # 函数名也是变量
# # abs = 10
# # abs(-10)
#
# # 传入函数
# def add(x, y, f):
#     return f(x) + f(y)

# print(add(-10 ,5,f))


# map / reduce
def f(x):
    return x * x


print(list(map(f,[1, 2, 3, 4, 5])))
print(list(map(str,[1, 2, 3, 4, 5])))

from functools import reduce
def add(x, y):
    print('x = ', x, 'y = ', y)
    return x + y

print(reduce(add,[1, 3, 5, 7, 9,11]))

def fn(x, y):
    return x * 10 + y

print(reduce(fn,[1, 3, 5, 7, 9]))

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

llll = map(char2num, '1111111111')
print(next(llll))
print(next(llll))
print(next(llll))
print(next(llll))
print(next(llll))



print(reduce(fn,map(char2num, '12345')))

# # str2Int funtion
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#
#
# def str2int(s):
#     def fn(x, y):
#         return x * 10 + y
#     def char2num(s):
#         return DIGITS[s]
#     return reduce(fn,map(char2num, s))
#
#
# print(str2int('123456789'))


# 简化版
def char2num2(s):
    return DIGITS[s]


def str2int2(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# filter

def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

def not_empty(s):
    return s and s.strip()





def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        yield n
        it =  filter(_not_divisible(n), it)  #  构造新序列


# sorted
# 排序算法
print(sorted([36, 5, -12, 9,-21]))
print(sorted([36, 5, -12, 9,-21], key=abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
Ltest = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def lowName(t):
    return t[0].lower()

print(sorted(Ltest,key=lowName))


# 返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1,3,5,7,9)
print(f)
print(f())
# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
#
# >>> f1 = lazy_sum(1, 3, 5, 7, 9)
# >>> f2 = lazy_sum(1, 3, 5, 7, 9)
# >>> f1==f2
# False
# f1()和f2()的调用结果互不影响。

#  闭包
def funcName(name):
    def inner_func(age):
        print('name',name,'age',age)
    return inner_func

bb = funcName('sy')
print(bb)
bb(18)

# 匿名函数
print(list(map(lambda x: x* x,[1,2,3,4,5])))
f = lambda x: x * x
print(f(5))

def build(x, y):
    return lambda: x * x + y * y

lam = build(5,5)
print(lam())

# 装饰器
def now():
    print('2018-01-05')
f = now
f()
print(now.__name__)
print(f.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('call %s() ' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2017-01-05')


now()

# 偏函数

print(int('12345'))
print(int('12345', base=8))

def int2(x, base=2):
    return int(x, base)
print(int2('1000000'))
# 把一些函数某些参数固定住,.返回一个新的函数.调用新函数更简单
import functools
int3 = functools.partial(int, base=2)



























