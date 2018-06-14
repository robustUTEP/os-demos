#! /usr/bin/env python3

from sys import argv
from time import time

global val
val = int(argv[1])

def delay(sec):
    waitUntil = time() + sec
    while (time() < waitUntil):
        pass

for t in range(5):
    print (val)
    val += 1
    delay(1)
