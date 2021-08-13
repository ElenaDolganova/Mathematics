import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# Задача 1
# Даны значения зарплат из выборки выпускников:
# 100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150.
# Без использования статистических функций вроде mean, std, var, посчитать среднее арифметическое,
# среднее квадратичное отклонение, смещенную и несмещенную оценки дисперсий для данной выборки.
# Можно затем посчитать те же значения с использованием статистических функций, чтобы проверить себя

salary_list = np.array([100, 80, 75, 77, 89, 33, 45, 25, 65, 17, 30, 24, 57, 55, 70, 75, 65, 84, 90, 150])

mean_height = salary_list.sum() / len(salary_list)
print('mean_height', mean_height)
print('salary_list.mean()', salary_list.mean())

salary_std = np.sqrt(((salary_list - mean_height) ** 2).sum() / len(salary_list))

print("std", salary_std)
print("salary_list.std", salary_list.std(ddof=0))

salary_var_0 = ((salary_list - mean_height) ** 2).sum() / len(salary_list)
salary_var_1 = ((salary_list - mean_height) ** 2).sum() / (len(salary_list) - 1)

print('salary_var_0', salary_var_0)
print('salary_list.var(ddof=0)', salary_list.var(ddof=0))

print('salary_var_1', salary_var_1)
print('salary_list.var(ddof=1)', salary_list.var(ddof=1))

# Задача 2
# Для выборки из задачи 1 найти первый и третий квартили, интерквартильное расстояние. Найти выборсы в выборке,
# используя для этого "усы" из boxplot. В этой задаче можно использовать статистические функции.

q_025 = np.quantile(salary_list, 0.25)
q_075 = np.quantile(salary_list, 0.75)
inter_qu = q_075 - q_025
print('q_025 =', q_025, 'q_075 =', q_075)
print('inter_quantile', inter_qu)

sl_ds_min = mean_height - inter_qu
sl_ds_max = mean_height + inter_qu
print('ds_min', sl_ds_min, 'ds_max', sl_ds_max)

sns.boxplot(y=salary_list)
plt.show()


boxplot_range = (q_025 - 1.5 * inter_qu, q_075 + 1.5 * inter_qu)
print('boxplot_range =', boxplot_range)
print("ОТРИЦАТЕЛЬНАЯ ЗАРПЛАТА!!!????")

# for i in range(len(salary_list)):
#     if salary_list[i] < boxplot_range[0]:
#         outliers = salary_list[i]

for i in range(len(salary_list)):
    if salary_list[i] > boxplot_range[1]:
        outliers1 = salary_list[i]

print('outliers', outliers1)


# Задача 3
# В университет на факультеты A и B поступило равное количество студентов, а на факультет C студентов поступило столько
# же, сколько на A и B вместе. Вероятность того, что студент факультета A сдаст первую сессию, равна 0.8.
# Для студента факультета B эта вероятность равна 0.7, а для студента факультета C - 0.9. Студент сдал первую сессию.
# Какова вероятность, что он учится: a) на факультете A? б) на факультете B? в) на факультете C?


# P(pass_exam|A) = 0.8
# P(pass_exam|B) = 0.7
# P(pass_exam|C) = 0.9
#
# P(A) = 1/4
# P(B) = 1/4
# P(C) = 1/2
#
# P(pass_exam) = P(pass_exam|A)*P(A) + P(pass_exam|B)*P(B) P(pass_exam|C)*P(C = 0.8 * 1/4 + 0.7 * 1/4 + 0.9 * 1/2 = 0.825
#
# P(A|pass_exam) = P(pass_exam|A) * P(A) / P(pass_exam) = 0.8 * 0.25 /0.825 = 0.242
# P(B|pass_exam) = P(pass_exam|B) * P(B) / P(pass_exam) = 0.7 * 0.25 /0.825 = 0.212
# P(C|pass_exam) = P(pass_exam|C) * P(C) / P(pass_exam) = 0.9 * 0.25 /0.825 = 0.272

