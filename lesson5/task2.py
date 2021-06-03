# 2.1
# Напишите код, проверяющий любую из теорем сложения или умножения вероятности на примере рулетки или
# подбрасывания монетки.

import numpy as np
import matplotlib.pyplot as plt


b, r, s, o = 0, 0, 0, 0
p_o, p_b, p_r = 0, 0, 0
n = 1
for i in range(0, n):
    x = np.random.randint(0, 36)
    if x == 0:
#        print("zero")
        o += 1
        p_o = o / 37
    elif x % 2 == 0:
#       print("red", x)
        r += 1
        p_r = 18 * r / 37
    else:
#        print("black", x)
        b = b + 1
        p_b = 18 * b / 37

p_sum = p_o + p_b + p_r

print("P(A + B + C) = ", p_sum, 'P(A) =', p_o, 'P(B) =', p_b, 'P(C) =', p_r)
print("black", b, " red", r, ' zero', o, " всего: ", n)

# 2.2 Сгенерируйте десять выборок случайных чисел х0, …, х9.
# и постройте гистограмму распределения случайной суммы  +х1+ …+ х9.

x_sum = []
n = 10
for i in range(n):
    x = np.random.rand(10)
    x_sum.append(sum(x))
    i += 1

num_bins = 10
n, bins, patches = plt.hist(x_sum, num_bins)
plt.xlabel('summa')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()

