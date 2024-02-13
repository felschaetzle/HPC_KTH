import numpy as np
# import cupy as cp
import time


@profile
def gauss_seidel(f):
    newf = f.copy()

    for i in range(1,newf.shape[0]-1):
        for j in range(1,newf.shape[1]-1):
            newf[i,j] = 0.25 * (newf[i,j+1] + newf[i,j-1] +
                                   newf[i+1,j] + newf[i-1,j])

    return newf

size = [8,16,32,64] #,128,256,512]
timer = []
for s in size:
  x = np.random.rand(s,s)

#   t1 = time.time_ns()
  for i in range(1000):
      x = gauss_seidel(x)
#   t2 = time.time_ns()
#   diff = (t2-t1)/1000000000
#   print(diff, "grid size is:", s)
#   timer.append(diff)
