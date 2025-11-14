# # a=[2,5,6,8,3,5,9,1]
# # b = []
# # for i in a:
# #     if i>5:
# #         b.append (i/2)
# #         print(b)
# #     else :
# #         b.append (2*i)
# # print(b)
# #
# #
# # array 56
# #
# #
# #
# # a= [0,2,4,5,7,2,6,9,11]
# # b=[]
# # for i in range(0,len(a),3):
# #     b.append(a[i])
# # print(b)
# #
# # array59
# #
# # a= [0,2,4,5,7,2,6,9,11]
# # b=[]
# # k=0
# # for i in range (0,len(a)):
# #     k+=a[i]
# #     b.append(k/(i+1))
# # print(b)
# #
# #
# # array66
# #
# #
# # a= [10,2,4,5,7,2,6,9,11]
# # b=0
# # for i in range (len(a)):
# #     if a[i] >0:
# #         a[i] = b
# #         break
# # for j in range(len(a)):
# #     if a[j]%2==0:
# #         a[j]+
# #         = b
# #
# # print(a)
# #
# # array70
# #
# a = [2, 4, 7, 8, 3, 3, 4, 6]
# for i in range(len(a) // 2):
#     if len(a) % 2 == 0:
#         a[i], a[len(a) // 2 + i] = a[len(a) // 2 + i], a[i]
#     else:
#         a[i], a[len(a) // 2 + 1 + i] = a[len(a) // 2 + 1 + i], a[i]
#
# print(a)
#
# homework
#
# array51
#
# a = [1, 2, 3]
# b = [4, 5, 6]
#
# for i in range(len(a)):
#     a[i], b[i] = b[i], a[i]
#
# print("a =", a)
# print("b =", b)
#
#
# array52
#
#
# a = [2, 8, 5, 10]
# b = []
#
# for i in range(len(a)):
#     if a[i] > 5:
#         b.append(2 * a[i])
#     else:
#         b.append(a[i] / 2)
#
# print(b)
#
#
#
# array53
#
#
# a = [2, 9, 5]
# b = [3, 7, 8]
# c = []
#
# for i in range(len(a)):
#     c.append(max(a[i], b[i]))
#
# print(c)
#
#
# array54
#
#
# a = [3, 6, 9, 10, 12, 5]
# b = []
#
# for i in a:
#     if i % 2 == 0:
#         b.append(i)
#
# print(b)
#
#
# array55
#
#
# a = [10, 20, 30, 40, 50, 60]
# b = []
#
# for i in range(1, len(a), 2):
#     b.append(a[i])
#
# print(b)
#
#
#
# array56
#
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = []
#
# for i in range(0, len(a), 3):
#     b.append(a[i])
#
# print(b)
#
#
#
# array57
#
#
#
# a = [1, 2, 3, 4, 5]
# b = []
#
# for i in range(len(a)-1, -1, -1):
#     b.append(a[i])
#
# print(b)
#
#
#
# array58
#
#
# a = [1, 2, 3, 4]
# b = []
# summa = 0
#
# for i in a:
#     summa += i
#     b.append(summa)
#
# print(b)
#
#
# array59
#
#
# a = [1, 2, 3, 4]
# b = []
# summa = 0
#
# for i in range(len(a)):
#     summa += a[i]
#     b.append(summa / (i + 1))
#
# print(b)
#
#
#
# array60
#
#
# a = [1, 2, 3, 4]
# b = []
#
# for i in range(len(a)):
#     b.append(sum(a[i:]))
#
# print(b)
#
#
#
# array61
#
# a = [1, 2, 3, 4]
# b = []
#
# for i in range(len(a)):
#     b.append(sum(a[i:]))
#
# print(b)
#
#
# array62
#
# a = [-3, 5, 0, 7, -1, 9]
# b = []
#
# for i in a:
#     if i > 0:
#         b.append(i)
#
# print(b)
#
#
# array63
#
#
# a = [5, 2, 8, 1, 4]
# a.sort()
# print(a)
#
#
#
# array64
#
# a = [5, 3, 1]
# b = [9, 7, 6]
# c = [4, 8, 2]
#
# a.sort()
# b.sort()
# c.sort()
#
# print(a)
# print(b)
# print(c)
#
#
# array65
#
#
# a = [1, 2, 3, 4, 5, 6]
# k = 2
#
# for i in range(0, len(a), k):
#     a[i] += 3
#
# print(a)
#
#
# array66
#
# a = [5, 8, 3, 4, 6, 7]
# found = False
#
# for i in range(len(a)):
#     if a[i] % 2 == 0 and not found:
#         found = True
#     elif found and a[i] % 2 == 0:
#         a[i] += 1
#
# print(a)
#
#
# array67
#
#
# a = [2, 5, 8, 10]
# last = a[-1]
#
# for i in range(len(a)):
#     a[i] = last
#
# print(a)
#
#
# array68
#
#
# a = [10, 20, 30, 40]
# a[0], a[1] = a[1], a[0]
# print(a)
#
#
# array69
#
# a = [1, 2, 3, 4, 5, 6]
# n = len(a) // 2
# a = a[n:] + a[:n]
# print(a)
#
#
# array70
#
#
# a = [1, 2, 3, 4, 5]
# a.reverse()
# print(a)
#
#
#
# array71
#
#
# a = [10, 20, 30, 40, 50]
# k = 1
# h = 3
#
# a[k], a[h] = a[h], a[k]
# print(a)
#
#
# array72
#
# a = [1, 2, 3, 4, 5, 6, 7]
# k = 2
# h = 5
#
# a[k:h+1] = reversed(a[k:h+1])
# print(a)
#
#
#
# array73
#
# a = [5, 2, 9, 1, 6]
# min_index = a.index(min(a))
# max_index = a.index(max(a))
#
# a[min_index], a[max_index] = a[max_index], a[min_index]
# print(a)
#
#
# array74
#
# a = [5, 2, 9, 1, 6]
# a.remove(min(a))
# a.remove(max(a))
# print(a)
#
#
# array75
#
#
# a = [4, 1, 6, 3, 8, 2]
# min_index = a.index(min(a))
# max_index = a.index(max(a))
#
# if min_index + 1 < len(a) and max_index + 1 < len(a):
#     a[min_index + 1], a[max_index + 1] = a[max_index + 1], a[min_index + 1]
#
# print(a)
#
#
# array76
#
# a = [9, 1, 5, 3, 8]
# a.sort()
# print(a)
#
#
# array77
#
# a = [4, 9, 1, 7, 2]
# min_index = a.index(min(a))
# max_index = a.index(max(a))
#
# a[min_index], a[max_index] = a[max_index], a[min_index]
# a.sort()
# print(a)
#
#
# array78
#
# a = [2, 4, 6, 8]
# b = []
#
# for i in range(len(a)-1):
#     b.append((a[i] + a[i+1]) / 2)
#
# b.append(a[-1])
# print(b)
#
#
#
# array79
#
#
# a = [1, 2, 3, 4]
# a = [a[-1]] + a[:-1]
# print(a)
#
#
# array80
#
#
# a = [1, 2, 3, 4]
# a = a[1:] + [a[0]]
# print(a)
#
#
#
# array81
#
# a = [1, 2, 3, 4, 5]
# k = 2
# b = [0]*k + a[:-k]
# print(b)
#
#
# array82
#
#
# a = [1, 2, 3, 4, 5]
# k = 2
# b = a[k:] + [0]*k
# print(b)
#
#
# array83
#
# a = [1, 2, 3, 4]
# a = [a[-1]] + a[:-1]
# print(a)
#
#
# array84
#
# a = [1, 2, 3, 4]
# a = a[1:] + [a[0]]
# print(a)
#
#
# array85
#
# a = [1, 2, 3, 4, 5]
# k = 2
# a = a[-k:] + a[:-k]
# print(a)
#
#
#
