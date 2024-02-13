#cython: language_level=3
from cython.cimports.libc.stdlib import malloc, free

cdef float* a
cdef float* b
cdef float* c
cdef float scalar = 2.0

def init_arrays(int array_size):
    """initialize all float arrays with values"""
    
    a = <float*> malloc(array_size * sizeof(float))
    b = <float*> malloc(array_size * sizeof(float))
    c = <float*> malloc(array_size * sizeof(float))

    for i in range(array_size):
        a[i] = 1.0
        b[i] = 2.0
        c[i] = 0.0

def copy(int array_size):
    for j in range(array_size):
        c[j] = a[j]

def sum(int array_size):
    for j in range(array_size):
        c[j] = a[j] + b[j]

def scale(int array_size):
    for j in range(array_size):
        b[j] = scalar * c[j]

def triad(int array_size):
    for j in range(array_size):
        a[j] = b[j] + scalar * c[j]

def free_arrays():
    """ free memory allocated for arrays"""
    free(a)
    free(b)
    free(c)