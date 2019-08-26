#! /usr/bin/env python3

from os import getpid
from sys import argv
from time import time

global val
val = int(argv[1])
pid = getpid()

def delay(sec):
    waitUntil = time() + sec
    while (time() < waitUntil):
        pass

for t in range(5):
    print("(pid=%d) val=%d" % (pid, val))
    delay(1)
    val += 1
