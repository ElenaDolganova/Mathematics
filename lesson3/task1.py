#Напишите код на Python, реализующий расчет длины вектора, заданного его координатами. (в программе)
import numpy as np
import math

x = []
x1 = [10, 10, 10]
x2 = [0, 0, -10]
for elem in range(0, (len(x1))):
    summa = x1[elem] + x2[elem]
    x.append(summa)

print(x)

length_x = math.sqrt(x[0] ** 2 + x[1] ** 2 + x[2] ** 2)
print(length_x)
