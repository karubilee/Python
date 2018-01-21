# 错误处理
# def foo():
#     r = some_function()
#     if r == (-1):
#         return (-1)
#     # do something
#     return r
#
# def bar()
#     r = foo()
#     if r == (-1):
#         print('Error')
#     else:
#         pass

'''
try:
    print('try...')
    r  = 10 / 2
    print('resut:', r)
except ZeroDivisionError as e:
    print('except', e)
finally:
    print('finally')
print('END')

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error')
finally:
    print('finally...')
print('END')

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

main()
'''



'''

# 调用栈

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

main()

'''

'''

# 记录错误
import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('END')
'''


# 抛出错误
class FooError(ValueError):
    pass
def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invaild value:%s' % s)
    return 10/n
# foo('0')

def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

# bar()

##### 调试 #####
#print 不用看了经常用哈哈哈

'''
# 断言
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n

def main():
    foo('0')

main()
'''

'''
# logging
import logging
logging.basicConfig(level = logging.INFO)
#  不知道怎么用

#pdb
import pdb
s = '0'
n = int(s)
pdb.set_trace()
print(10 / n)
'''

# 单元测试
import unittest
from myDict import Dict
class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')


    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')


    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']


    def test_attererror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


    def setUp(self):
        print('setUp')


    def tearDown(self):
        print('tearDown...')

if __name__ == '__main__':
    unittest.main()


#setup
#teardown

# 文档测试