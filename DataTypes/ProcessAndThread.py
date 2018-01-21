'''
import os
print('Process(%s) start' % os.getpid())

pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just cteated a child process (%s).' % (os.getpid(),pid))
'''

'''
# Pool
from multiprocessing import Pool
import os, time, random
def long_time_task(name):
    print('Run task %s (%s)...' %(name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' %(name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args= (i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done')
'''

'''
# 子进程  ???
import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
'''

'''

import time, threading
# 新线程执行的代码
def loop():
    print('1thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('2thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('3thread %s ended.' % threading.current_thread().name)

print('4thread %s is runnding...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('5thread %s ended.' % threading.current_thread().name)

'''

'''
# Lock
import time, threading
balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()



t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

'''
# ThreadLocal
import threading
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()


t1 = threading.Thread(target= process_thread,args=('Alice',), name = 'Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()