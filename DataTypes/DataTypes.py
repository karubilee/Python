#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#字符串
print('hello worlds')
print('this is new line')
print('I\'m ok')
print('HI,%s,you have %d' % ('lwb', 5000))
print('Hello,{0},成绩提升了{1: .1f}%' .format('小明', 17.1))
lb = 'lb'
print(lb)

# list和tuple
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[-1])    #取最后一位#
print(classmates[-2])    #取最后第2位#
classmates.append('ada')
classmates.insert(1, 'HHH')
classmates.pop()    #删除末尾元素
classmates.pop(1)
classmates[1] = 'sabi'
L = ['Apple',123,True]

# 条件判断
age = 11
if age >= 18:
    print('your age is %s' % (age))
elif age >100:
    print('your age is ',age)
else:
    print ('what')

# birth = input('birth: ')
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

# 循环
names = ['lwb', 'hsy', 'xiaobaby1','xiaobaby2']
for name in names:
    print(name)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

Lfor =  ['Bart', 'Lisa', 'Adam']
for name in Lfor:
    print('Hello,%s'%(name))

nBreak = 1
while nBreak <= 100:
    if nBreak > 10:
        break
    print(nBreak)
    nBreak = nBreak + 1
print('END')

nContinue = 0
while nContinue < 10:
    nContinue = nContinue + 1
    if nContinue % 2 == 0:
        continue
    print(nContinue)
# dict
dNameScores = {'Mi': 95, 'B': 75, 'Tracy': 85}
print(dNameScores['Mi'])

print('Mi' in dNameScores)
print(dNameScores.get('M'))
dNameScores.pop('Mi')

# set
s = set([1, 1, 2, 3])
print(s)
s.add(4)
print(s)
s.remove(4)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
