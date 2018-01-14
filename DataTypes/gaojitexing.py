# 高级特性
# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L)
print(L[0:3])
print(L[:3])
print(L[-2:])
LL = list(range(100))
print(LL)
print(LL[:10])
print(LL[-10:])
print(LL[10:20])
print(LL[1:20:2])
print(LL[::20])
print(LL[:])   #复制
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])

#迭代

d = {'a':1, 'b': 2, 'c':3}
for key in d:
    print(key)

from collections import Iterable

print(isinstance('abc',Iterable))
print(isinstance([1, 2, 3],Iterable))
print(isinstance(123 ,Iterable))


for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)


for x, y in [(1, 1), (2, 4), (3,9)]:
    print(x, y)


# 列表生成式
print(list(range(1, 11)))
print([x * x for x in range(1, 11)])
print([x * x for x in range(1,11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

import os
print([d for d in os.listdir('.')])

d1 = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d1.items():
    print(k, '=' , v)

print([k + '=' + v for k, v in d1.items()])
lower = ['H','S','Y','L', 'W', 'B']
print([s.lower() for s in lower])

#  生成器

print([x * x for x in range(10)])
g = (x * x for x in range(10))
print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

for n in g:
    print(n + 1000)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield (b)
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib(10))

# 迭代器