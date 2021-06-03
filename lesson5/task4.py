
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math


# Количество перестановок
i = 0
for p in itertools.permutations('012356789', 2):
#    print(''.join(str(x) for x in p))
    i +=1
print("permutations('012356789', 2):", i)

i = 0
for p in itertools.permutations('0123456789', 10):
#    print(''.join(str(x) for x in p))
    i +=1
print("permutations('012356789', 10):", i)

i = 0
# Количество сочетаний
for p in itertools.combinations('0123456789', 2):
#    print(''.join(str(x) for x in p))
    i +=1
print("combinations('0123456789', 2)", i)

i = 0
# Количество сочетаний
for p in itertools.combinations('0123456789', 10):
#    print(''.join(str(x) for x in p))
    i +=1
print("combinations('0123456789', 10)", i)