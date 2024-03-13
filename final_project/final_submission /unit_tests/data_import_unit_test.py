#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 16:34:40 2024

@author: georgiosmitsos
"""

import numpy as np
import data_import

def test_import():
    train, test = data_import.import_np()
    dataset_total = np.vstack((train,test))
    
    train2, test2 = data_import.import_pd()
    dataset_total2 = np.vstack((train2,test2))
    
    assert dataset_total2.all() == dataset_total.all()
    