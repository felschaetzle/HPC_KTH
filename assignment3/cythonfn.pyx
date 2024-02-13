
def copy(array_size, c, a):
    for j in range(array_size):
        c[j] = a[j]

def sum(array_size, c, a, b):
    for j in range(array_size):
        c[j] = a[j] + b[j]

def scale(array_size, b, scalar, c):
    for j in range(array_size):
        b[j] = scalar * c[j]

def triad(array_size, a, b, scalar, c):
    for j in range(array_size):
        a[j] = b[j] + scalar * c[j]