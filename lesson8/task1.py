import numpy as np

A = np.array([[1, 2, 3], [4, 0, 6], [7, 8, 9]])
B = np.array([12, 2, 1])
xx = np.linalg.solve(A, B)
print(xx)

det_a = np.linalg.det(A)
BT = np.transpose([B])
print('det_a', det_a, '!= 0')

C = np.concatenate((A, BT), axis=1)
#  сравним ранг основной и ранг расширенной матрицы
ar = np.linalg.matrix_rank(A, 0.00001)
cr = np.linalg.matrix_rank(C, 0.00001)
print('сравним ранги основной и расширенной матриц ar, cr:', ar, cr)
xyz = np.linalg.lstsq(A, B)
print('deсision')
print('xyz - решение с помощью мнк - lstsq()\n', xyz)
print('xх - точное решение - solve()\n', xx)
