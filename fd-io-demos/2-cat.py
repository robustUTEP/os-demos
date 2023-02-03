#! /usr/bin/env python3
#
# cat.py.  Demo of os file open/read/close semantics.
#

import os
import sys



def printFromFd(ifd):
    numReads = 1
    while True:
        ibuf = os.read(ifd, 100)
        if not len(ibuf): break
        numReads += 1
        os.write(1, ibuf)
     # summary to stderr
    os.close(ifd)
    os.write(2, f"EOF on {numReads}th call to read()\n".encode())
    

filesToPrint = sys.argv[1:]     # all params are file names

if len(filesToPrint):
    for fname in filesToPrint:
        os.write(2, f"copying file: {fname}\n".encode()) # to stderr
        fd = os.open(fname, os.O_RDONLY)
        printFromFd(fd)
else:
    os.write(2, "copying from stdin\n".encode()) # to stderr
    printFromFd(0)              # stdin by default (no files)
