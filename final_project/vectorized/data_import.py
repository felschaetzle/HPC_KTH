#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:34:40 2024

@author: georgiosmitsos
"""

import numpy as np
import pandas as pd

# @profile
def import_np():
    train = np.genfromtxt('train.csv', delimiter=',')
    test = np.genfromtxt('test.csv', delimiter=',')
    
    return train, test

# @profile
def import_pd():
    temp_train = pd.read_csv('train.csv', delimiter=',',header=None)
    temp_test = pd.read_csv('test.csv', delimiter=',',header=None)
    train2 = temp_train.to_numpy(dtype='float64')
    test2 = temp_test.to_numpy(dtype='float64')
    
    return train2, test2
    
if __name__== "__main__":
    train, test = import_np()
    train2, test2 = import_pd()
    