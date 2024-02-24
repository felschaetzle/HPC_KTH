#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 18:51:02 2024

@author: georgiosmitsos
"""

import numpy as np
cimport numpy as np

def g(double[:,:] x):
   cdef np.ndarray[np.float64_t, ndim=2] x_np = np.asarray(x)
   cdef np.ndarray[np.float64_t, ndim=2] g_res_np = 1.0 / (1.0 + np.exp(-x_np))
   return g_res_np

def grad_g(double[:,:] x):
   cdef np.ndarray[np.float64_t, ndim=2] gx = g(x)
   cdef np.ndarray[np.float64_t, ndim=2] grad_g_res_np = gx * (1.0 - gx)
   grad_g_res_np = gx * (1.0 - gx)
   return grad_g_res_np

def reshape(double[:,:] theta,int input_layer_size,int hidden_layer_size,int num_labels): 
   cdef int ncut = hidden_layer_size * (input_layer_size + 1)
   cdef double[:, :] Theta1 = theta[:ncut].reshape((hidden_layer_size, input_layer_size + 1))
   cdef double[:, :] Theta2 = theta[ncut:].reshape((num_labels, hidden_layer_size + 1))
   return Theta1, Theta2

def gradient(double[:,:] theta,int input_layer_size,int hidden_layer_size,int num_labels,double[:,:] X,double[:,:] y,double lmbda,double[:,:] a1):
    """ Neural net cost function gradient for a three layer classification network.
    Input:
      theta               flattened vector of neural net model parameters
      input_layer_size    size of input layer
      hidden_layer_size   size of hidden layer
      num_labels          number of labels
      X                   matrix of training data
      y                   vector of training labels
      lmbda               regularization term
    Output:
      grad                flattened vector of derivatives of the neural network 
    """
 	
    cdef double[:, :] Theta1, Theta2, z2, a2, a3, y_k, delta3, delta2, Delta1, Delta2
    cdef double m = y.shape[0]
    cdef np.ndarray[np.float64_t, ndim=2] Theta1_grad = np.zeros((hidden_layer_size, input_layer_size+1), dtype=np.float64)
    cdef np.ndarray[np.float64_t, ndim=2] Theta2_grad = np.zeros((hidden_layer_size, input_layer_size+1), dtype=np.float64)
    
    # unflatten theta
    Theta1, Theta2 = reshape(theta, input_layer_size, hidden_layer_size, num_labels)
 	
    # Backpropagation: calculate the gradients Theta1_grad and Theta2_grad:
    a1 = np.hstack((np.ones((m,1)), X))
    z2 = a1 @ Theta1.T
    a2 = g(z2)
    a2 = np.hstack((np.ones((m,1)), a2))
    a3 = g(a2 @ Theta2.T)
    
    # Compute errors
    y_k = np.eye(num_labels)[y.flatten().astype(int)]
    delta3 = a3 - y_k.astype(float)
    delta2 = (delta3 @ Theta2[:, 1:]) * grad_g(z2)
    
    # Compute gradients
    Delta1 = delta2.T @ a1
    Delta2 = delta3.T @ a2
    Theta1_grad = Delta1 / m
    # Theta2_grad = Delta2 / m

#    # add regularization
#    # Theta2_grad[:,1:] += (lmbda/m) * Theta2[:,1:]

#    # flatten gradients
#    # grad = np.concatenate((Theta1_grad.flatten(), Theta2_grad.flatten()))

#    # return grad



