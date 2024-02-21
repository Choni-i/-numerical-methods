# -*- coding: utf-8 -*-
"""all_code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CddfqN5F7Nfya2Bm8RyRcDMmLwoXFUFb
"""

import numpy as np
import matplotlib.pyplot as plt

N= 23
n = 5
C= np.zeros((n, n), dtype=float)
b = np.full(n, 23, dtype=float)

for i in range(n):
    for j in range(n):
        C[i, j] = 0.1 * N * (i + 1) * (j + 1)

A = 11.7 /(1+C)**7
x = np.linalg.solve(A, b)
cond_A = np.linalg.cond(np.abs(A), p=np.inf)

delta = 0.1 #произвольная
x_new = np.empty((n, n))

for i in range(n):
    b_new = b.copy()
    b_new[i] += delta
    x_new[i] = np.linalg.solve(A, b_new)

d = np.array([np.linalg.norm(x - x_i, ord=np.inf) / np.linalg.norm(x, ord=np.inf)
              for x_i in x_new])

plt.figure(figsize=(6, 5))
plt.bar(['1', '2', '3','4','5'], d)
plt.xlabel('m')
plt.savefig('cond_precision.png', dpi=300)

d_argmax = np.argmax(d)
b_new = b.copy()
b_new[d_argmax] += delta


rel_delta = (np.linalg.norm(b_new - b, ord=np.inf)
              / np.linalg.norm(b, ord=np.inf))
print(f'm = {d_argmax + 1}')
print(f'd = {d}\n')
print(f'delta(x^m) = {d[d_argmax]}')
print(f'delta(b^m) = {rel_delta}')
print(f'cond(A) = {cond_A}\n')
print(f'{d[d_argmax]} <= {rel_delta * cond_A}')
print(f'delta(x^m) <= cond(A) * delta(b^m)')

import numpy as np

A = np.array([[611, 196, -192, 407],
             [196, 899, 113, -192],
             [-192, 113, 899, 196],
             [407, -192, 196, 611]], dtype=float)

b = np.full((4,4), 0, dtype=float)
m = -np.Inf

for i in range(4):
  b[i, i] = 1
  x_i = np.linalg.solve(A, b[i])
  nor_i = np.linalg.norm(x_i)/np.linalg.norm(b[i])
  m = max(nor_i, m)

print(A)
norm_A = np.linalg.norm(A)
print(f'Экспериментальное число обусловенности матрицы:               {m*norm_A}')
print(f'Число обусловенности матрицы, полученное встроенной функцией: {np.linalg.cond(A)}')

import numpy as np
import math
import matplotlib.pyplot as plt

M = 5
n = 100
q = 1.001 - 2*M*10**(-3)
def search_b(x):
  b = np.zeros(n, dtype=float)
  for i in range(n):
    b[i] = abs(x-(n/10))*i*math.sin(x)
  return b

A = np.zeros((n,n), dtype=float)
for i in range(n):
  for j in range(n):
    if (i==j):
      A[i][j] = (q-1)**(i+j)
    else:
      A[i][j] = (q)**(i+j) + 0.1*(j-i)

def gauss_method(A, b):
    A = A.copy()
    b = b.copy()
    n = A.shape[0]
    b_tmp = []
    for i in range(n):
        max_val = abs(A[i, 0])
        max_i = i
        max_j = 0
        for j in range(i, n):
            for k in range(0, n):
                if abs(A[j, k])> max_val:
                    max_val = abs(A[j, k])
                    max_i = j
                    max_j = k
        b_tmp.append(max_j)
        if max_i!=i:
            tmp = A[i].copy()
            A[i] = A[max_i]
            A[max_i] = tmp
            tmp = b[i]
            b[i] = b[max_i]
            b[max_i] = tmp
        for k in range(i + 1, n):
            b[k] -= b[i] * A[k,max_j]/A[i,max_j]
            A[k] -= A[i] * A[k,max_j]/A[i,max_j]
    result = b.copy()
    for i in range(n-1, -1, -1):
        j = b_tmp[i]
        b[i]/=A[i,j]
        result[j] = b[i]
        for k in range(0, i):
            b[k] -= b[i] * A[k,j]
    return result

num = 50
point = np.linspace(-5.0, 5.0, num)
y = []
orig = []
for x in point:
  y.append(np.sum(gauss_method(A, search_b(x))))
  orig.append(np.sum(np.linalg.solve(A, search_b(x))))


plt.figure(figsize=(6, 5))
plt.plot(point, y)
plt.title("Реализованный метод Гаусса - схема полного выбора")
plt.xlabel('x')
plt.ylabel('y(x)')
plt.show()
plt.savefig('graphic.png', dpi=300)

plt.figure(figsize=(6, 5))
plt.plot(point, orig)
plt.title("Встроенный метод Гаусса")
plt.xlabel('x')
plt.ylabel('orig(x)')
plt.show()
plt.savefig('orig_graphic.png', dpi=300)