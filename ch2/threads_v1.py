#! /usr/bin/env python3

from sys import argv
from time import time, sleep
from threading import Thread, enumerate, Lock

global count
count = 0
global countLock
countLock = Lock()

itersPerThread = int(argv[1])

threadNum = 0


class Worker(Thread):
    def __init__(self, iters):
        global threadNum
        Thread.__init__(self, name="Thread-%d" % threadNum)
        threadNum += 1
        self.iters = iters
    def run(self):
        global count, countLock
        for i in range(self.iters):
            countLock.acquire()
            count += 1
            countLock.release()

def delay(sec):
    waitUntil = time() + sec
    while (time() < waitUntil):
        pass

workers = [Worker(itersPerThread).start(), Worker(itersPerThread).start()]

while len(enumerate()) > 1:
    sleep(0.25) #    delay(0.25)
    print("activeThreads=%s, count=%d" % (enumerate(), count))
print(count)

    
