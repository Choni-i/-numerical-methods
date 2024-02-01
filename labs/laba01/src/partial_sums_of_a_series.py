# -*- coding: utf-8 -*-
"""partial sums of a series.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SJ0n0Mh6wBP7DNpXf_rvBxG0BjaFPOnf
"""

import matplotlib.pyplot as plt
from collections import defaultdict

def Summa(n):
    return 96/(n ** 2 + 9 * n + 20)

N_values = [10, 100, 10**3, 10**4, 10**5, 10**6]
sums = {}
errors = {}
right_figure = defaultdict(int) #??
for N in N_values:
    s = 0.
    true_s = 24.
    for i in range(N):
        s += Summa(i)
    sums[N] = s
    errors[N] = abs(s - true_s)

    i = 1
    while i < 30:
        if errors[N] <= 10 ** (i):
            right_figure[N] += 1
            i -= 1
        else:
            break

    print(f'For N = {N}: \nsum = {sums[N]} \nabs error = {errors[N]} \nnumders of right figure = {right_figure[N]}\n')

keys = list(map(str, sums.keys()))
bars = plt.barh(keys, list(right_figure.values()))
plt.bar_label(bars, padding=1, fontsize=10)
plt.xlim(0, 6)
plt.xlabel("Кол-во значимых цифр")
plt.ylabel("Кол-во чисел ряда")
plt.legend()
plt.savefig('right_figure.png', dpi=300)