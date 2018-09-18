#! /usr/bin/env python3

import os, sys, time, re

pid = os.getpid()               # get and remember pid

pr,pw = os.pipe()
for f in (pr, pw):
    os.set_inheritable(f, True)
print("pipe fds: pr=%d, pw=%d" % (pr, pw))

import fileinput

print("About to fork (pid=%d)" % pid)

rc = os.fork()

if rc < 0:
    print("fork failed, returning %d\n" % rc, file=sys.stderr)
    sys.exit(1)

elif rc == 0:                   #  child - will write to pipe
    print("Child: My pid==%d.  Parent's pid=%d" % (os.getpid(), pid), file=sys.stderr)
    args = ["wc", "p3-exec.py"]

    os.close(1)                 # redirect child's stdout
    os.dup(pw)
    for fd in (pr, pw):
        os.close(fd)
    print("hello from child")
             
else:                           # parent (forked ok)
    print("Parent: My pid==%d.  Child's pid=%d" % (os.getpid(), rc), file=sys.stderr)
    os.close(0)
    os.dup(pr)
    for fd in (pw, pr):
        os.close(fd)
    for line in fileinput.input():
        print("From child: <%s>" % line)
