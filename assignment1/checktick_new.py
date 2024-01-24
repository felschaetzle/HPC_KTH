#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: georgiosmitsos
"""

import numpy as np
import time
import timeit


#time.time()

def checktick():
   M = 200
   timesfound = np.empty((M,))
   for i in range(M):
      t1 =  time.time() # get timestamp from timer
      t2 = time.time() # get timestamp from timer
      while (t2 - t1) < 1e-16: # if zero then we are below clock granularity, retake timing
          t2 = time.time() # get timestamp from timer
      t1 = t2 # this is outside the loop
      timesfound[i] = t1 # record the time stamp
   minDelta = 1000000
   Delta = np.diff(timesfound) # it should be cast to int only when needed
   minDelta = Delta.min()
   return minDelta

print(f"Granularity for time.time(): {checktick():.2E} seconds")




#time.time_ns()

def checktick():
    M = 200
    timesfound = np.empty((M,))
    for i in range(M):
        t1 =  time.time_ns() # get timestamp from timer
        t2 = time.time_ns() # get timestamp from timer
        while (t2 - t1) < 1e-16: # if zero then we are below clock granularity, retake timing
            t2 = time.time_ns() # get timestamp from timer
        t1 = t2 # this is outside the loop
        timesfound[i] = t1 # record the time stamp
    minDelta = 1000000
    Delta = np.diff(timesfound) # it should be cast to int only when needed
    minDelta = Delta.min()
    return minDelta/1e9

print(f"Granularity for time.time_ns(): {checktick():.2E} seconds")




# timeit.default_timer()

def checktick():
   M = 200
   timesfound = np.empty((M,))
   for i in range(M):
      t1 =  timeit.default_timer() # get timestamp from timer
      t2 = timeit.default_timer() # get timestamp from timer
      while (t2 - t1) < 1e-16: # if zero then we are below clock granularity, retake timing
          t2 = time.time() # get timestamp from timer
      t1 = t2 # this is outside the loop
      timesfound[i] = t1 # record the time stamp
   #minDelta = 1000000
   Delta = np.diff(timesfound) # it should be cast to int only when needed
   minDelta = Delta.min()
   return minDelta

print(f"Granularity for timeit: {checktick():.2E} seconds")




