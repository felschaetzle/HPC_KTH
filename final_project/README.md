# artificialneuralnetwork-python
Artificial Neural Network for Image Classification

# Original code by Philip Mocz (2023)

### [📝 Read the Algorithm Write-up on Medium](https://philip-mocz.medium.com/create-your-own-artificial-neural-network-for-multi-class-classification-with-python-7011946af722)

]Create and train your own artificial neural network to classify images of galaxies from SDSS/the Galaxy Zoo project.
Data used in this work is heavily modified and simplified from  the Galaxy Zoo 2 (Willett et al.,2013), MNRAS, 435, 2835.

# Final Project by Thorben Fetz, Georgios Mitsos, Felix Schatzle (2024) 

for the course "DD2358 Introduction to High Performance Computing" at KTH Royal Institute of Technology 

# Initial code: artificialneuralnetwork.py

# Profiling

Line profiling: profiling/line_profiling.txt (original code), profiling/line_profiling_vectorized.txt (vectorized code)

Memory profiling: profiling/mprofile_initial.dat (original code)

cProfiling: cProfile_initial.png (original code)
  
# Algorithmic Optimization

The optimized code is: vectorized/artificialneuralnetwork_vectorized.py

# GPU Optimization

The two jupyter notebooks are placed in the "colab" folder. Import the notbooks to your Google Colab. To establish a runtim benchmark, run "ColabBenchmark.ipynb". This contains the original code.

 "PyTorchOptimization.ipynb" contains both, our refactored neural network with the same architecture and the simplest possible PyTorch network. To train a network, deceide which model you want to use, and execute the according cell. Afterwards, the cell that contains the line "main()" executes to training process.

# Documentation

Documentation of the codes in docs/documentation

# Unit Tests

docs/unit_tests/data_import_unit_test.py (tests alternative data import method, calls data_import.py)

docs/unit_tests/artificialneuralnetwork_unit_test.py (tests vectorized gradient function, calls artificialneuralnetwork.py and artificialneuralnetwork_vectorized.py)


