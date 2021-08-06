import numpy as np


def poisson_proba(k, lambda_):
    return (lambda_ ** k) * (np.exp(-lambda_)) / np.math.factorial(k)

# Задача 2
# Вероятность попадания в цель при одном выстреле равна 0.01. Какова вероятность того, что число попаданий
# при 200 выстрелах будет не менее 5 и не более 10?

a = 200 * 0.01
k5 = 5
k10 = 10

# probability_k5 = (a ** k5) * (np.exp(-a)) / np.math.factorial(k5)
# probability_k10 = (a ** k10) * (np.exp(-a)) / np.math.factorial(k10)

probability_5_10 = sum(poisson_proba(k=i, lambda_=a) for i in range(5, 11))
print(probability_5_10)
# print('k5', probability_k5)
# print('k10', probability_k10)

