#! /usr/bin/env python3
#
# read.py.  Demo of os read semantics.
#

from os import read, write

numReads = 1

ibuf = read(0, 100)
while len(ibuf):
    sbuf = ibuf.decode()
    write(1, f"### Read {numReads}: <{sbuf}> ###\n".encode())
    ibuf = read(0, 100)
    numReads += 1
write(1, f"EOF on {numReads}th call to read()\n".encode())
