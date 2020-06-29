import numpy as np

N = 10000 # 欲得到10000个真实前沿点
x1 = np.linspace(0, 5, N)
# print(x1)
# print("/n")
x2 = x1.copy()
# print(x2)
# print("/n")
x2[x1 >= 3] = 3
# print(x2)
m = np.vstack((4 * x1 ** 2 + 4 * x2 ** 2, (x1 - 5) ** 2 + (x2 - 5) ** 2)).T
print(x1.shape)
print(x2.shape)
print(m.shape)

