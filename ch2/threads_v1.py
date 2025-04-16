#! /usr/bin/env python3

from sys import argv
from time import time, sleep
from threading import Thread, enumerate, Lock, current_thread

global count
count = 0
countLock = Lock()              # resource proxy for count

itersPerThread = int(argv[1])

threadNum = 0

def add(a, b):
    return a + b



class Worker(Thread):
    def __init__(self, iters):
        Thread.__init__(self)
        self.iters = iters
        print(f"--{self.name} created")
    def run(self):
        global count, countLock
        print(f"--{self.name} started")
        for i in range(self.iters):
            countLock.acquire() # acquire count resource
            count = add(count, 1)
            countLock.release() # release count resource
        print(f"--{self.name} exiting")

print(f"Main thread's name is {current_thread().name}")
# enumerate() retuns the set of live threads
print(f"Number of threads before any workers created = {len(enumerate())}")

wallClockStart = time()

workers = [ Worker(itersPerThread) for i in range(2) ]

for worker in workers:
    worker.start()

while (nLiveThreads := len(enumerate())) > 1:     # while at least one worker alive...
    print(f"#threads still alive = {nLiveThreads}; count = {count}")
    sleep(0.25) #    delay(0.25)

print(f"final count = {count}, total wall clock time = {time() - wallClockStart:.2}s")

    
