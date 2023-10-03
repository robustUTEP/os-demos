#! /usr/bin/env python3

import sys, os

debug = 0



progName = sys.argv[0]
filenames = sys.argv[1:]


from buf import BufferedFdWriter, BufferedFdReader, bufferedCopy

byteWriter = BufferedFdWriter(1) # stdout

if debug: print(f"argv={sys.argv}; filenames={filenames}")

if len(filenames):              # filenames specified
    for filename in filenames:
        fd = os.open(filename, 0)
        if debug: print(f"opening {filename}, fd={fd}\n")
        byteReader = BufferedFdReader(fd)
        bufferedCopy(byteReader, byteWriter)
        byteReader.close()
    byteWriter.flush()
else:                           # no params: copy from stdin
    byteReader = BufferedFdReader(0) # stdion
    bufferedCopy(byteReader, byteWriter)
    
    


