import numpy as np
import scipy.linalg

#    Вычислите LU-разложение матрицы:
A = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73]])
P, L, U = scipy.linalg.lu(A)

print("P = ", P)
print("L = ", L)
print("U = ", U)

det_a = np.linalg.det(A)
print("det A = ", det_a, '!= 0')

print('---------------------')
#   Придумать вектор правых частей и решить лин систему

B = np.array([[1, 10, 100]])
BT = np.transpose(B)
C = np.concatenate((A, BT), axis=1)
print('C', C)

#  сравним ранг основной и ранг расширенной матрицы
ar = np.linalg.matrix_rank(A, 0.00001)
cr = np.linalg.matrix_rank(C, 0.00001)
print('сравним ранги основной и расширенной матриц ar, cr:\n', ar, '=', cr)

X = np.linalg.solve(A, BT)
print("X = ", X)

