import numpy as np
import matplotlib.pyplot as plt


A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([2, 5, 11])
Q, R = np.linalg.qr(A)

print('A = ', A)
print('Q = ', Q)
print('R = ', R)

R1 = R[:2, :2]
B1 = np.dot(np.transpose(Q), B)[:2]
print(('B1 = ', B1))

X1 = np.linalg.solve(R1, B1)
print(('X1 = ', X1))

X = np.append(X1, 0)
print('Псевдорешение. Считаем Х2 = 0')
print(X)



