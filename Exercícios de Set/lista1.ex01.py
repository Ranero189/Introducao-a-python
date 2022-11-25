import numpy as np
from numpy import linalg
from numpy.random import default_rng

rng = default_rng()

num = rng.choice(range(1, 171), size=(3, 3), replace=False)

print("Matrix original")

print(num)

print()

print("Determinante da matrix")

print(np.linalg.det(num))