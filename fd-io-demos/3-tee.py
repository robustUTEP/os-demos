#! /usr/bin/env python3
#
# cat.py.  Demo of os file open/read/close semantics.
#

import os
import sys

progName = sys.argv[0]
oFileName = sys.argv[1]             # name of output file

def err(msg):
    os.write(2, f"{progName}: {msg}\n".encode());
    sys.exit(1)

try:
    oFileFd = os.open(oFileName, os.O_WRONLY)
except:
    err(f"can't open file <{oFileName}>")


ofds = [1, oFileFd]              # write to both stdout and oFile via their fds
fdToFname = {1:"stdout", oFileFd:oFileName} # for error messages

try:
    os.lseek(oFileFd, 0, os.SEEK_END)   #  seek to end of output file
except:
    err(f"seek to end of {oFileName} failed")

numReads = 1
while True:
    try:
        ibuf = os.read(0, 100)      # from stdin
    except:
        err("can't read from stdin")
    if not len(ibuf): break     # EOF
    numReads += 1
    for ofd in ofds:
        obuf = bytes(ibuf)  # copy of input buffer
        try:
            while len(obuf):
                numBytes = os.write(ofd, obuf)
                obuf = obuf[numBytes:] # slice off numBytes
        except:
            err(f"failed write to {fdToFname[ofd]}")
# summary to stderr
os.write(2, f"EOF on {numReads}th call to read()\n".encode())
