import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

@profile
def poisson_2d():
    size = 64
    x = np.random.rand(size,size)
    
    x[[-1,0],:] = 0 # boundary conditions
    x[:,[-1,0]] = 0

    for i in range(1000): # number of iterations
        x = gauss_seidel(x)

@profile
def gauss_seidel(f):
    newf = f.copy()

    for i in range(1,newf.shape[0]-1):
        for j in range(1,newf.shape[1]-1):
            newf[i,j] = 0.25 * (newf[i,j+1] + newf[i,j-1] +
                                   newf[i+1,j] + newf[i-1,j])

    return newf

if __name__ == "__main__":
    poisson_2d()
    
    
