# homework

# 29m
#
# a=float(input("a="))
# b=float(input("b="))
# n=int(input("n="))
# c = (b - a) / n
#
# for i in range(n + 1):
#     x = a + i * c
#     print(f"x{i} = {x}")
#
# 30m
#
# import math
#
# a = float(input("a = "))
# b = float(input("b = "))
# n = int(input("n = "))
# h = (b - a) / n
#
# for i in range(n + 1):
#     x = a + i * h
#     fx = 1 - math.sin(x)
#     print(f"x = {x:.4f}, f(x) = {fx:.6f}")
#
# 31m
#
# n = int(input("n = "))
#
# A = 2
# for i in range(n):
#     print(f"A{i} = {A}")
#     A = 2 + 1 / A
#
# 32m
#
# n = int(input("n = "))
#
# A = 1
# for k in range(1, n+1):
#     A = (A + 1) / k
#     print(f"A{k} = {A}")
#
#
# 33m
#
#
# n = int(input("n = "))
#
# f1 = 1
# f2 = 1
#
# print(f"F1 = {f1}")
# print(f"F2 = {f2}")
#
# for k in range(3, n + 1):
#     f = f1 + f2
#     print(f"F{k} = {f}")
#     f1 = f2
#     f2 = f
#
# 34m
#
# n = int(input("n = "))
#
# A1 = 1
# A2 = 2
#
# print(f"A1 = {A1}")
# print(f"A2 = {A2}")
#
# for k in range(3, n + 1):
#     A = (A1 + 2 * A2) / 3
#     print(f"A{k} = {A}")
#     A1 = A2
#     A2 = A
#
# 35m
#
# n = int(input("n = "))
#
# A1 = 1
# A2 = 2
# A3 = 3
#
# print(f"A1 = {A1}")
# print(f"A2 = {A2}")
# print(f"A3 = {A3}")
#
# for k in range(4, n + 1):
#     A = A3 + A2 - 2 * A1
#     print(f"A{k} = {A}")
#     A1 = A2
#     A2 = A3
#     A3 = A
#
# 36m
#
# n = int(input("n = "))
# k = int(input("k = "))
#
# s = 0
#
# for i in range(1, n + 1):
#     p = 1
#     for j in range(k):
#         p *= i
#     s += p
#
# print("Yig'indi =",s)
#
# 37m
#
# N = int(input("N = "))
#
# S = 0
#
# for i in range(1, N + 1):
#     S += i
#
# print("Yig'indi =", S)
#
#
# 38m
#
# N = int(input("N = "))
#
# S = 0
#
# for i in range(1, N + 1):
#     p = 1
#     k = N - i + 1
#     for j in range(k):
#         p *= i
#     S += p
#
# print("Yig'indi =", S)
#
# 39m
#
# A = int(input("A = "))
# B = int(input("B = "))
#
# for i in range(A, B + 1):
#     for j in range(i):
#         print(i, end=' ')
#     print()
#
# 40m
#
# A = int(input("A = "))
# B = int(input("B = "))
#
# count = 1
#
# for i in range(A, B + 1):
#     for j in range(count):
#         print(i, end=' ')
#     print()
#     count += 1
