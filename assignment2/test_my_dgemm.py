#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 13:12:29 2024

@author: georgiosmitsos
"""

import numpy as np
import pytest

def dgemm_benchmark(N):
    
    np.random.seed(40)
    A = np.random.random((N,N))
    
    np.random.seed(41)
    B = np.random.random((N,N))
    
    np.random.seed(42)
    C = np.random.random((N,N))

    C_test = C + np.matmul(A,B)
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i,j] = C[i,j] + A[i,k] * B[k,j]
                
    output = np.max(abs(C-C_test))
    return output 


def test_output():
    assert dgemm_benchmark(200) < 1e-12