#! /usr/bin/env python3

import os, stat

def dowork():
    fd = os.open("/tmp/file", os.O_WRONLY | os.O_CREAT | os.O_TRUNC, stat.S_IRWXU);
    assert fd >= 0
    buffer = "hello world\n"
    rc = os.write(fd, buffer.encode())
    assert rc == len(buffer)
    os.write(1, ("wrote %s bytes\n" % rc).encode())
    os.fsync(fd)
    os.close(fd)

dowork()

    
