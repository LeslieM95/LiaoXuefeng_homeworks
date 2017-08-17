#!\usr\bin\env\python3
#-*- coding: utf-8 -*-

from multiprocessing import Process, Pipe
import os, time

def write(q):
    print('Process to write: %s' % os.getpid())
    
    for value in range(10):
        time.sleep(3)
        print('Put %s to queue///' % value)
        time.sleep(3)
        q.send(value)
        #time.sleep(3)

def read(q):
    print('Process to read: %s' % os.getpid())
    
    while True:
        
        value = q.recv()
        
        print('Get %s from queue.' % value)
        time.sleep(2)

if __name__ == '__main__':
    ps, pr = Pipe()
    pw = Process(target=write, args=(ps,))
    pr = Process(target=read, args=(pr,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
