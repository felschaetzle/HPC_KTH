#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 16:42:08 2024

@author: georgiosmitsos
"""

import numpy as np
from timeit import default_timer as timer
from functools import wraps

global t_diff, t_tot
t_diff = []
t_tot = []

def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 =  timer()
        result = fn(*args, **kwargs)
        t2 = timer()
        t_diff.append(t2-t1)
        return result
    return measure_time


def dgemm_alt(N):
    np.random.seed(40)
    A = np.random.rand(N,N)
    A_list = A.tolist()
    
    np.random.seed(41)
    B = np.random.rand(N,N)
    B_list = B.tolist()
    
    np.random.seed(42)
    C = np.random.rand(N,N)
    C_list = C.tolist()
    
    C = dgemm_numpy(N,A,B,C)
    C_list = dgemm_list(N,A_list,B_list,C_list)
    
    return C, C_list


@timefn
def dgemm_numpy(N,A,B,C):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i,j] = C[i,j] + A[i,k] * B[k,j]            
    return C 
    
    
@timefn
def dgemm_list(N,A_list,B_list,C_list):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C_list[i][j] = C_list[i][j] + A_list[i][k] * B_list[k][j]            
    return C_list

if __name__ == "__main__":
    n = 5 # run n times to calculate average and standard deviation
    for i in [10,50,80,120,160,200]:
        for ii in range(n):
            dgemm_alt(i)
        t_tot.append([np.mean(t_diff[0::2]),np.std(t_diff[0::2]),np.mean(t_diff[1::2]),np.std(t_diff[1::2])])
        t_diff = []


