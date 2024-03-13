# artificialneuralnetwork-python
Artificial Neural Network for Image Classification

# Original code by Philip Mocz (2023)

#Final Project by Thorben Fetz, Georgios Mitsos, Felix Schatzle for the course "Introduction to High Performance Computing" at KTH Royal Institute of Technology (2024)

### [📝 Read the Algorithm Write-up on Medium](https://philip-mocz.medium.com/create-your-own-artificial-neural-network-for-multi-class-classification-with-python-7011946af722)

Create and train your own artificial neural network to classify images of galaxies from SDSS/the Galaxy Zoo project.
Data used in this work is heavily modified and simplified from  the Galaxy Zoo 2 (Willett et al.,2013), MNRAS, 435, 2835.

# Initial code artificialneuralnetwork.py

# Profiling

Line profiling: profiling/line_profiling.txt (original code), profiling/line_profiling_vectorized.txt (vectorized code)

Memory profiling: profiling/mprofile_initial.dat (original code)

cProfiling: cProfile_initial.png (original code)
  
# Algorithmic Optimization

The optimized code is: vectorized/artificialneuralnetwork_vectorized.py

# Unit Tests

 unit_tests/data_import_unit_test.py (tests alternative data import method, calls data_import.py)

unit_tests/artificialneuralnetwork_unit_test.py (tests vectorized gradient function, calls artificialneuralnetwork.py and artificialneuralnetwork_vectorized.py)


