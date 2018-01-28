'''

#datetime
# 获取日期和时间
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))

#获取制定日期和时间
dt = datetime(2015, 4, 19, 12, 20)
print(dt)

#把datetime转换成timestamp
print(dt.timestamp())
#timestamp 转换成 datetime
t = 1429413600.0
print(datetime.fromtimestamp(t))
#str转datetime
cday = datetime.strptime('2015-6-1 18:19:57', '%Y-%m-%d %H:%M:%S')
print(cday)
# python 文档日期格式化
# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

#datetime转str
nowDateTime = datetime.now()
print(nowDateTime.strftime('%a, %b %d %H:%M'))

#date 加减
from datetime import datetime,timedelta
now3 = datetime.now()
print(now3)
print(now3 + timedelta(hours=10))
print(now3 + timedelta(days=10))
print(now3 + timedelta(days=10,hours=12))

'''

'''
# collections
# namedtuple
from collections import namedtuple, deque, defaultdict, OrderedDict,Counter
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x)
print(p.y)
print(isinstance(p,Point))
print(isinstance(p,tuple))
Circle = namedtuple('Circle',['x', 'y', 'z'])

# deque
q = deque(['a', 'b', 'c'])
q.append('x')
print(q)
q.appendleft('y')
print(q)
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])


# Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
'''

'''
# base64
import base64
print(base64.b64encode(b'binary\x00string'))
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))
'''

# struct

'''
# hashlib
import hashlib
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())
'''

# hmac

#为了防止黑客通过彩虹表根据哈希值反推原始口令，在计算哈希的时候，
# 不能仅针对原始输入计算，需要增加一个salt来使得相同的输入也能得到不同的哈希，
# 这样，大大增加了黑客破解的难度。
'''
# itertools
import itertools
natuals = itertools.count(1)
# for n in natuals:
#     print(n)
nums = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(nums))

# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)

ns = itertools.repeat('ABC',3)
for n in ns:
    print(n)

for c in itertools.chain('ABC', 'XYZ'):
    print(c)

for key, group in itertools.groupby('ABAABBBBCCCCCCAAAA'):
    print(key,list(group))
'''

# contextlib
# 上下文

# urllib
'''
# Get
from urllib import request
import ssl
import json
url = 'https://api.douban.com/v2/book/2129650'
context = ssl._create_unverified_context()
with request.urlopen(url,context = context) as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
    print(json.loads(data))
'''

# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

# Post
'''
from urllib import request, parse

print('Login to weibo.cn...')
email = input('Email: ')
passwd = input('Password: ')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
'''