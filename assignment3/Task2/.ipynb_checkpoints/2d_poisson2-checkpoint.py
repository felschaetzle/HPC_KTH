import numpy as np
import matplotlib.pyplot as plt
import cythonfn_poisson2

def poisson_2d():
    size = 64
    x = np.random.rand(size,size)
    
    x[[-1,0],:] = 0 # boundary conditions
    x[:,[-1,0]] = 0

    for i in range(1000): # number of iterations
        x = cythonfn_poisson.gauss_seidel(x,size)

if __name__ == "__main__":
    poisson_2d()
    
    
