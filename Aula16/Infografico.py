import numpy as np
from numpy.linalg import in
np.set_printoptions(precision=5, suppress=True)
A = np.matrix([[1, 2, 1], [0, 1, 3],
[3, 2, 0]])
Ainversa = inv(A)
produto = A * Ainversa
print("Matriz A")
print(A)
print("Inversa de A")
print(Ainversa)
print("produto de A * Ainversa, igual amatriz identidade")
print(produto)