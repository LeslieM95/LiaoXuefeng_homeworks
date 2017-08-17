#!\usr\bin\env\python3
#-*- coding: utf-8 -*-

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(5)
    end = time.time()
    print('Task %s runs %.2f seconds.' % (name, (end - start)))
    #time.sleep(0.1)

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    print('Waiting for all subprocesses done...')
    p = Pool()
    for i in range(9):
        p.apply_async(long_time_task, (i,))
    
    p.close()
    p.join()
    print('All subprocesses done.')
