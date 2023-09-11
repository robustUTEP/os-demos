#! /usr/bin/env python3

import os, stat
from sys import stderr

def dowork():
    totalBytesWritten = 0
    fd = os.open("/tmp/file", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, stat.S_IRWXU);
    assert fd >= 0
    buffer = "hello world\n"
    while len(buffer):
        wc = os.write(fd, buffer.encode())
        buffer = buffer[wc:]
        os.write(1, ("wrote %s bytes\n" % wc).encode())
        totalBytesWritten += wc
    print(f"wrote a total of {totalBytesWritten} bytes\n", file=stderr)
    os.fsync(fd)
    os.close(fd)

dowork()

    
