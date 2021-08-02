import numpy as np
import math


def arrangements(n, k):
    return np.math.factorial(n) // np.math.factorial(n - k)


def permutations(n):
    return np.math.factorial(n)


def combinations(n, k):
    return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))


# Задача 1
# Группа студентов изучает 10 различных дисциплин. Сколькими способами можно составить расписание на понедельник,
# если в этот день должно быть 4 разных занятия?

Stud_shed = arrangements(10, 4)
print('# Задача 1')
print('Stud_shed', Stud_shed)

# __Задача 2__
# Из колоды в 52 карты вынимают случайным образом 4 карты. Найти число исходов, соответствующих тому, что был вытянут
# хотя бы один туз.

# Хотя бы 1 туз = 1 туз и больше = 1 туз ИЛИ 2 туза ИЛИ 3 туза ИЛИ 4 туза:

ace1 = combinations(4, 1)
any_other_cards3 = combinations(51, 3)
var1 = ace1 * any_other_cards3

ace2 = combinations(4, 2)
any_other_cards2 = combinations(50, 2)
var2 = ace2 * any_other_cards2

ace3 = combinations(4, 3)
any_other_cards3 = combinations(49, 1)
var3 = ace3 * any_other_cards3

ace4 = combinations(4, 4)
any_other_cards4 = combinations(48, 0)
var4 = ace4 * any_other_cards4

take_1_or_2_or_3_or_4_ace = var1 + var2 + var3 + var4
print('\n''__Задача 2__')
print('ace', take_1_or_2_or_3_or_4_ace)

# __Задача 3__
# Семь человек рассаживаются наудачу на скамейке. Какова вероятность того, что два определённых человека будут
# сидеть рядом?

var_2_people = 6 * 2    # варианты рассадить пару на 7-и местах
var_2_people_from_7 = var_2_people * permutations(7 - 2)
var_all = permutations(7)
result = var_2_people_from_7 / var_all
print('\n''__Задача 3__')
print("result", result)

# __Задача 4__
# Из 60 вопросов, входящих в экзаменационные билеты, студент знает 50. Какова вероятность того, что среди трёх наугад
# выбранных вопросов студент знает: а) все? б) два?

print('\n''__Задача 4__')

c_all_questions = combinations(60, 3)
c3_good_questions = combinations(50, 3)
c2_good_questions = combinations(50, 2)
c1_bad_questions = combinations(10, 1)
p2_good = c2_good_questions * c1_bad_questions / c_all_questions
p3_good = c3_good_questions / c_all_questions
print('p_know_3 = ', p3_good,  '  p_know_2 = ',  p2_good)

# __Задача 5__
# Бросается игральная кость. Пусть событие `A` - появление чётного числа, событие `B` - появление числа больше трёх.
# Являются ли эти события независимыми?

print('\n''__Задача 5__')

# События независимы, если P(AB) = P(A)*P(B);
# Может выпасть число 4 или 6, т.е. одновременно и четное число и больше 3
p_ab = 2 / 6     #     выбор 2 из 6
p_a = 1 / 2      # = 1/2 =  1 / 6 + 1 / 6 + 1 / 6    2, 4, 6
p_b = 1 / 2      # = 1/2 =  1 / 6 + 1 / 6 + 1 / 6    4, 5, 6
if p_a * p_b == p_ab:
    print('События независимые', 'p_ab = ', p_ab, 'p_a * p_b = ', p_a * p_b)
else:
    print('События зависимые', 'p_ab = ', p_ab, '   p_a * p_b = ', p_a * p_b)


# __Задача 6__
# Допустим, имеется некоторая очень редкая болезнь (поражает 0.1 % населения). Вы приходите к врачу, вам делают тест на эту болезнь, и тест оказывается положительным. Врач говорит вам, что этот тест верно выявляет 99 % больных этой болезнью и всего лишь в 1 % случаев даёт ложный положительный ответ.
# _Вопрос_: какова вероятность, что вы действительно больны ей?
# _Подсказка_: вновь используйте формулу Байеса с раскрытием знаменателя с помощью формулы полной вероятности.

# P(больной \ положительн) = [Р(положительн \ больной) * Р(больной)] / [Р(положит \ больной) * Р(больной) + Р(положит \ здоровый) * Р(здоровый)]

p_positive_ill = 0.99
p_ill = 0.01
p_positive_healthy = 0.01
p_healthy = 0.9
p_ill_positive = p_positive_ill * p_ill / (p_positive_ill * p_ill + p_positive_healthy * p_healthy)

print('\n''__Задача 6__')
print('вероятность оказаться больным при положительном результате анализа \n', 'p_ill_positive = ', p_ill_positive)
