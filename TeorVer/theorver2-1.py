import numpy as np
import matplotlib.pyplot as plt


def combinations(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))


# Задача 1
# Контрольная работа состоит из пяти вопросов. На каждый вопрос приведено четыре варианта ответа, один из которых
# правильный. Составьте закон распределения числа правильных ответов при простом угадывании. Найдите M(X), D(X).
n = 5
p = 1 / 4
q = 1 - p

i = 0
x_probabilities = np.zeros([5])
x_values = np.arange(0, 5)
d_values = np.zeros([5])
while i < 5:
    x_probabilities[i] = (combinations(n, i) * p ** i * q ** (n - i))
    i = i + 1

print("x_values", x_values)
print('x_probabilities', x_probabilities)
plt.plot(x_values, x_probabilities)

plt.xlabel('x_values')
plt.ylabel('x_probabilities')
plt.xlim(0, 5)
plt.ylim(0, 0.4)
plt.grid(True)
plt.show()

m = x_values.dot(x_probabilities)
# print("M = ", m,)
d_values = (x_values - m) ** 2
# print('d_values', d_values)
d = d_values.dot(x_probabilities)
print("M = ", m, 'D = ', d)
