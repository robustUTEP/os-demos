#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "common.h"

int value;

int
main(int argc, char *argv[])
{
    if (argc != 2) { 
	fprintf(stderr, "usage: mem <value>\n"); 
	exit(1); 
    } 
    int *p = &value;                   // memory for pointer is on "stack"
    assert(p != NULL);
    // printf("(pid:%d) addr of main:     %llx\n", (int) getpid(), (unsigned long long) main);
    printf("(pid:%d) addr of p:        %llx\n", (int) getpid(), (unsigned long long) &p);
    printf("(pid:%d) addr stored in p: %llx\n", (int) getpid(), (unsigned long long) p);
    *p = atoi(argv[1]); // assign value to addr stored in p
    while (1) {
	Spin(1);
	*p = *p + 1;
	printf("(pid:%d) p=0x%llx, *p=%d\n", getpid(), (long long)p, *p);
    }

    return 0;
}

