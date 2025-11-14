# # array24
#
# a = [2, 4, 6, 8, 10]
# n = len(a)
# d = a[1] - a[0]
# ok = True
#
# for i in range(1, n-1):
#     if a[i+1] - a[i] != d:
#         ok = False
#         break
#
# if ok:
#     print(d)
# else:
#     print(0)
#
# # array 25
#
#
# a = [2, 4, 8, 16]
# n = len(a)
# q = a[1] / a[0]
# ok = True
#
# for i in range(1, n-1):
#     if a[i+1] / a[i] != q:
#         ok = False
#         break
#
# if ok:
#     print(q)
# else:
#     print(0)
#
# # array 26
#
# a = [4, 7, 1, 9, 2]
# mn = a[0]
#
# for i in range(1, len(a)):
#     if a[i] < mn:
#         mn = a[i]
#
# print(mn)
#
#
#
# # array27
#
# a = [4, 7, 1, 9, 2]
# mx = a[0]
#
# for i in range(1, len(a)):
#     if a[i] > mx:
#         mx = a[i]
#
# print(mx)
#
#
# # array28
#
# a = [4, 7, 1, 9, 2]
# mn = a[0]
# ind = 0
#
# for i in range(1, len(a)):
#     if a[i] < mn:
#         mn = a[i]
#         ind = i
#
# print(ind)
#
#
# # array29
#
# a = [4, 7, 1, 9, 2]
# mx = a[0]
# ind = 0
#
# for i in range(1, len(a)):
#     if a[i] > mx:
#         mx = a[i]
#         ind = i
#
# print(ind)
#
#
# # array30
#
# a = [4, 7, 1, 9, 2]
# mn = a[0]
# mx = a[0]
# imin = 0
# imax = 0
#
# for i in range(len(a)):
#     if a[i] < mn:
#         mn = a[i]
#         imin = i
#     if a[i] > mx:
#         mx = a[i]
#         imax = i
#
# a[imin], a[imax] = a[imax], a[imin]
# print(a)
#
#
#
# # array31
#
# a = [4, 7, 1, 9, 2]
# mx = a[0]
# ind = 0
#
# for i in range(1, len(a)):
#     if a[i] > mx:
#         mx = a[i]
#         ind = i
#
# if ind < len(a)-1:
#     print(a[ind+1])
# else:
#     print(0)
#
#
#
# # array32
#
# a = [4, 7, 1, 9, 2]
# mn = a[0]
# ind = 0
#
# for i in range(1, len(a)):
#     if a[i] < mn:
#         mn = a[i]
#         ind = i
#
# if ind > 0:
#     print(a[ind-1])
# else:
#     print(0)
#
#
#
# # array33
#
# a = [4, 7, 1, 9, 2]
# mn = a[0]
# ind = 0
#
# for i in range(1, len(a)):
#     if a[i] < mn:
#         mn = a[i]
#         ind = i
#
# s = 0
# for i in range(0, ind):
#     s += a[i]
#
# print(s)
#
#
# # array34
#
# a = [4, 7, 1, 9, 2, 5]
# mx = a[0]
# ind = 0
#
# for i in range(1, len(a)):
#     if a[i] > mx:
#         mx = a[i]
#         ind = i
#
# s = 0
# for i in range(ind + 1, len(a)):
#     s += a[i]
#
# print(s)
#
#
# # array35
#
# a = [4, 7, 1, 9, 2]
# mn = a[0]
# ind = 0
#
# for i in range(1, len(a)):
#     if a[i] < mn:
#         mn = a[i]
#         ind = i
#
# if ind > 0:
#     s = 0
#     for i in range(ind):
#         s += a[i]
#     print(s / ind)
# else:
#     print(0)
#
#
#
# # array36
#
#
# a = [4, 7, 1, 9, 2, 5]
# mx = a[0]
# ind = 0
#
# for i in range(1, len(a)):
#     if a[i] > mx:
#         mx = a[i]
#         ind = i
#
# if ind < len(a)-1:
#     s = 0
#     c = 0
#     for i in range(ind+1, len(a)):
#         s += a[i]
#         c += 1
#     print(s / c)
# else:
#     print(0)
#
#
#
# # array37
#
#
# a = [4, 7, 1, 9, 2, 5]
# mn = a[0]
# mx = a[0]
# imin = 0
# imax = 0
#
# for i in range(len(a)):
#     if a[i] < mn:
#         mn = a[i]
#         imin = i
#     if a[i] > mx:
#         mx = a[i]
#         imax = i
#
# if imin > imax:
#     imin, imax = imax, imin
#
# s = 0
# for i in range(imin+1, imax):
#     s += a[i]
#
# print(s)
#
#
#
# # array38
#
#
# a = [4, 7, 1, 9, 2, 5]
# mn = a[0]
# mx = a[0]
# imin = 0
# imax = 0
#
# for i in range(len(a)):
#     if a[i] < mn:
#         mn = a[i]
#         imin = i
#     if a[i] > mx:
#         mx = a[i]
#         imax = i
#
# if imin > imax:
#     imin, imax = imax, imin
#
# s = 0
# c = 0
# for i in range(imin+1, imax):
#     s += a[i]
#     c += 1
#
# if c > 0:
#     print(s / c)
# else:
#     print(0)
#
#
# # array39
#
#
# a = [4, 7, 1, 9, 2, 5]
# s = 0
#
# for i in range(0, len(a), 2):
#     s += a[i]
#
# print(s)
#
#
#
# # array40
#
# a = [4, 7, 1, 9, 2, 5]
# s = 0
#
# for i in range(1, len(a), 2):
#     s += a[i]
#
# print(s)
#
#
#
# # array41
#
# a = [4, 7, 1, 9, 2, 5]
# s = 0
# c = 0
#
# for i in range(0, len(a), 2):
#     s += a[i]
#     c += 1
#
# print(s / c)
#
#
#
# # array42
#
#
# a = [4, 7, 1, 9, 2, 5]
# s = 0
# c = 0
#
# for i in range(1, len(a), 2):
#     s += a[i]
#     c += 1
#
# print(s / c)
#
#
# # array43
#
#
# a = [4, 7, 1, 9, 2, 5]
# mn = a[0]
# mx = a[0]
# imin = 0
# imax = 0
#
# for i in range(len(a)):
#     if a[i] < mn:
#         mn = a[i]
#         imin = i
#     if a[i] > mx:
#         mx = a[i]
#         imax = i
#
# c = imin + (len(a) - imax - 1)
# print(c)
#
#
#
# # array44
#
# a = [4, 7, 1, 9, 2, 5]
# mn = a[0]
# mx = a[0]
# imin = 0
# imax = 0
#
# for i in range(len(a)):
#     if a[i] < mn:
#         mn = a[i]
#         imin = i
#     if a[i] > mx:
#         mx = a[i]
#         imax = i
#
# if imin > imax:
#     imin, imax = imax, imin
#
# s = 0
# for i in range(imin+1, imax):
#     if a[i] % 2 == 1:
#         s += a[i]
#
# print(s)
#
#
# # array45
#
# a = [4, -7, 1, -9, 2, 5]
# c = 0
#
# for i in range(len(a)):
#     if a[i] > 0:
#         c += 1
#
# print(c)
#
#
# # array46
#
# a = [4, -7, 1, -9, 2, 5]
# c = 0
#
# for i in range(len(a)):
#     if a[i] < 0:
#         c += 1
#
# print(c)
#
#
# # array47
#
# a = [4, -7, 1, -9, 2, 5]
# s = 0
#
# for i in range(len(a)):
#     if a[i] > 0:
#         s += a[i]
#
# print(s)
#
#
#
# # array48
#
#
# a = [4, -7, 1, -9, 2, 5]
# s = 0
#
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
#
# print(s)
#
#
# # array49
#
#
# a = [4, -7, 1, -9, 2, 5]
# cp = 0
# cn = 0
#
# for i in range(len(a)):
#     if a[i] > 0:
#         cp += 1
#     elif a[i] < 0:
#         cn += 1
#
# if cp > cn:
#     print("musbat ko‘p")
# elif cn > cp:
#     print("manfiy ko‘p")
# else:
#     print("teng")
#
#
#
# # array50
#
# a = [4, 7, 1, 9, 2, 5]
# n = len(a)
# dmin = abs(a[1] - a[0])
#
# for i in range(n - 1):
#     d = abs(a[i+1] - a[i])
#     if d < dmin:
#         dmin = d
#
# print(dmin)


