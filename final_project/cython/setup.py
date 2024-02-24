#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 18:51:03 2024

@author: georgiosmitsos
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import numpy as np

extensions = [Extension("cythonfn", ["cythonfn.pyx"],
              include_dirs=[np.get_include()])]

setup(ext_modules=cythonize(extensions))

# setup(ext_modules=cythonize("cythonfn.pyx", 
#                             compiler_directives={"language_level":"3"}))