#! /usr/bin/env python3


from os import getpid
from sys import argv, stderr, exit
from time import time, sleep

if len(argv) != 2:
    print (f"USAGE: {argv[0]} message", file=stderr)
    exit(1)


str = argv[1]
pid = getpid()

def delay(sec):
    sleep(sec) # tell os to not run for <sec> seconds


for t in range(5):
    print("(pid=%d) %s" % (pid, str))
    delay(1)
