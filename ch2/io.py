#! /usr/bin/env python3

import os, stat
from sys import stderr, argv

outFileName=argv[1]

def dowork():
    totalBytesWritten = 0
    fd = os.open(outFileName, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, stat.S_IRUSR);
    assert fd >= 0
    buffer = "hello world\n".encode()
    while len(buffer):
        wc = os.write(fd, buffer)
        buffer = buffer[wc:]
        os.write(1, ("wrote %s bytes\n" % wc).encode())
        totalBytesWritten += wc
    os.write(2, f"wrote a total of {totalBytesWritten} bytes\n".encode())
    os.fsync(fd)
    os.close(fd)

dowork()

    
