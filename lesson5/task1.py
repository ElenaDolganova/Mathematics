# 1.1 Напишите код, моделирующий выпадение поля в рулетке (с учетом поля зеро).
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab


#Запускаем рулетку 100 раз
xx = []
b, r, s, o = 0, 0, 0, 0
n = 100
for i in range(0, n):
    x = np.random.randint(0, 37)
    xx.append(x)
    if x == 0:
#        print("zero")
        o += 1
    elif x % 2 == 0:
#        print("red", x)
        r += 1
    else:
#        print("black", x)
        b = b + 1
    s += 1

print("black", b, " red", r, ' zero', o, " всего: ", s)


# 1.2 сколько раз в 1 серии из 100 повторений выпадет значение от 0 до 36
num_bins = 100
n, bins, patches = plt.hist(xx, num_bins)
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Histogram')
plt.show()
