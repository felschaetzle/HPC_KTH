#cython: language_level=3
from cython.cimports.libc.stdlib import malloc, free

def copy(int array_size):
    cdef float* a = <float*> malloc(array_size * sizeof(float))
    cdef float* c = <float*> malloc(array_size * sizeof(float))
    
    for j in range(array_size):
        a[j] = 1.0
        c[j] = a[j]

def sum(int array_size):
    cdef float* a = <float*> malloc(array_size * sizeof(float))
    cdef float* b = <float*> malloc(array_size * sizeof(float))
    cdef float* c = <float*> malloc(array_size * sizeof(float))


    for j in range(array_size):
        a[j] = 1.0
        b[j] = 2.0
        c[j] = a[j] + b[j]

def scale(int array_size):
    cdef float* b = <float*> malloc(array_size * sizeof(float))
    cdef float* c = <float*> malloc(array_size * sizeof(float))
    cdef float scalar = 2.0

    for j in range(array_size):
        b[j] = 2.0
        b[j] = scalar * c[j]

def triad(int array_size):
    cdef float* a = <float*> malloc(array_size * sizeof(float))
    cdef float* b = <float*> malloc(array_size * sizeof(float))
    cdef float* c = <float*> malloc(array_size * sizeof(float))
    cdef float scalar = 2.0

    for j in range(array_size):
        b[j] = 2.0
        c[j] = 0.0
        a[j] = b[j] + scalar * c[j]