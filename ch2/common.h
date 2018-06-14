#ifndef __common_h__
#define __common_h__

#include <sys/time.h>
#include <sys/stat.h>
#include <assert.h>
#include <pthread.h>

double 
GetTime();

void
Spin(int howlong);

void
Pthread_create(pthread_t *t, const pthread_attr_t *attr, 
	       void *(*start_routine)(void *), void *arg);

void
Pthread_join(pthread_t thread, void **value_ptr);


void
Pthread_mutex_lock(pthread_mutex_t *mutex);

void
Pthread_mutex_unlock(pthread_mutex_t *mutex);

void
Pthread_mutex_init(pthread_mutex_t *mutex, pthread_mutexattr_t *attr);

#endif // __common_h__
