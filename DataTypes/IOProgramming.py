'''
try:
    f = open('/Users/lb/Desktop/testPythonRead/test.rtf','r',encoding='UTF-8')
    print(f.read())
finally:
    if f:
        f.close()

with open('/path/to/file','r') as f:
    print(f.read())

# 二进制文件  rb模式打开
f = open('/Users/michael/test.jpg', 'rb')
'''

'''
# 用'w'会覆盖,用'a'是append
with open('/Users/lb/Desktop/testPythonRead/test.txt', 'a') as f:
    f.write('Hello,wrold!10086')
f.close()
'''
'''
# StringIO和BytesIO
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

#BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

# 操作文件和目录
import os
print(os.name)
print(os.uname())
#环境变量
print(os.environ)
print(os.environ.get('PATH'))

#操作文件和目录
print(os.path.abspath('.'))
# os.path.join('/Users/lb/Desktop','testDir')
os.mkdir('/Users/lb/Desktop/testDir')

'''

# 序列化
import json
d = dict(name = 'Bob', age = 20, score = 99)
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s, default= lambda obj:obj.__dict__))

