CFLAGS=-g -O2 -pthread
LDFLAGS=-g -O2 -pthread -lpthread

all: cpu io mem threads_v1 threads_v0

cpu: cpu.o common.o
io: io.o common.o
mem: mem.o common.o

threads_v1: threads_v1.o common.o

threads_v0: threads_v0.o common.o

clean: 
	rm -f cpu io mem threads_v1 threads_v0 *.o
