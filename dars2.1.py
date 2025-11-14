# array18
#
# a = [5, 8, 3, 9, 2]
# n = len(a)
# c = False
#
# for i in range(n):
#     if a[i] < a[-1]:
#         print(a[i])
#         c = True
#         break
#
# if not c:
#     print(0)
#
#
# array19
#
# a = [5, 8, 3, 9, 2]
# n = len(a)
# index = 0
#
# for i in range(n):
#     if a[0] < a[i] < a[-1]:
#         index = i
#
# print(index)
#
#
# array20
#
# a = [2, 5, 7, 4, 9, 6]
# K = 1
# L = 4
# c = 0
# for i in range(K, L + 1):
#     c += a[i]
#
# print(c)
#
#
# array21
#
# a = [2, 5, 7, 4, 9, 6]
# K = 1
# L = 4
#
# s = 0
# for i in range(K, L + 1):
#     s += a[i]
#
# o = s / (L - K + 1)
# print(o)
#
#
# array22
#
# a = [2, 5, 7, 4, 9, 6]
# K = 1
# L = 4
#
# y = 0
# for i in range(len(a)):
#     if i < K or i > L:
#         y += a[i]
#
# print(y)
#
#
# array23
#
# a = [2, 5, 7, 4, 9, 6]
# K = 1
# L = 4
#
# s = 0
# count = 0
# for i in range(len(a)):
#     if i < K or i > L:
#         s += a[i]
#         count += 1
#
# if count > 0:
#     print(s / count)
# else:
#     print(0)
#
#
# array24
#
# a = [2, 4, 6, 8, 10]
# n = len(a)
# d = a[1] - a[0]
# p = True
#
# for i in range(1, n - 1):
#     if a[i + 1] - a[i] != d:
#         p = False
#         break
#
# if p:
#     print(d)
# else:
#     print(0)
#
