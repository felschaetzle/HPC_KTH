# -*- coding: utf-8 -*-
"""Julia set generator without optional PIL-based image drawing"""

import timeit
import numpy as np
from functools import wraps

global t_diff

t_diff = []

# area of complex space to investigate
x1, x2, y1, y2 = -1.8, 1.8, -1.8, 1.8
c_real, c_imag = -0.62772, -.42193

# decorator to time
def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 =  timeit.default_timer() #
        result = fn(*args, **kwargs)
        t2 =  timeit.default_timer()
        t_diff.append(t2-t1)
        # print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time


@timefn
def calc_pure_python(desired_width, max_iterations):
    """Create a list of complex coordinates (zs) and complex parameters (cs),
    build Julia set"""
    x_step = (x2 - x1) / desired_width
    y_step = (y1 - y2) / desired_width
    x = []
    y = []
    ycoord = y2
    while ycoord > y1:
        y.append(ycoord)
        ycoord += y_step
    xcoord = x1
    while xcoord < x2:
        x.append(xcoord)
        xcoord += x_step
    # build a list of coordinates and the initial condition for each cell.
    # Note that our initial condition is a constant and could easily be removed,
    # we use it to simulate a real-world scenario with several inputs to our
    # function
    zs = []
    cs = []
    for ycoord in y:
        for xcoord in x:
            zs.append(complex(xcoord, ycoord))
            cs.append(complex(c_real, c_imag))
    
    # print("Length of x:", len(x))
    # print("Total elements:", len(zs))
    output = calculate_z_serial_purepython(max_iterations, zs, cs)


@timefn
def calculate_z_serial_purepython(maxiter, zs, cs):
    """Calculate output list using Julia update rule"""
    output = [0] * len(zs)
    for i in range(len(zs)):
        n = 0
        z = zs[i]
        c = cs[i]
        while abs(z) < 2 and n < maxiter:
            z = z * z + c
            n += 1
        output[i] = n
    return output

if __name__ == "__main__":
    # Calculate the Julia set using a pure Python solution with
    #reasonable defaults for a laptop
    for i in range(100):
        calc_pure_python(desired_width=1000, max_iterations=300)
    
    print(f"calculate_z_serial_purepython took on average {np.mean(t_diff[0::2])} \u00B1 {np.std(t_diff[0::2])} seconds")
    print(f"calc_pure_python took on average {np.mean(t_diff[1::2])} \u00B1 {np.std(t_diff[1::2])} seconds")
    
    
    
    
    
    

