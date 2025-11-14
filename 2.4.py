# array90
#
# a = [1, 2, 3, 4, 5]
# k = 2
# b = a[:k] + a[k+1:]
# print(b)
#
#
# array91
#
# a = [10, 20, 30, 40, 50, 60]
# k = 1
# m = 3
# del a[k:m+1]
# print(a)
#
#
# array92
#
# a = [1, 2, 3, 4, 5, 6]
# b = []
# for x in a:
#     if x % 2 == 0:
#         b.append(x)
# print(b)
#
#
#
# array93
#
# a = [10, 20, 30, 40, 50, 60]
# b = a[1::2]
# print(b)
#
#
# array94
#
# a = [10, 20, 30, 40, 50, 60]
# b = a[::2]
# print(b)
#
#
#
# array95
#
# a = [3, 5, 3, 7, 3]
# b = a[:a.index(3)] + a[a.index(3)+1:]
# print(b)
#
#
# array96
#
# a = [3, 5, 3, 7, 5, 3]
# b = []
# [b.append(x) for x in a if x not in b]
# print(b)
#
#
# array97
#
# a = [3, 5, 3, 7, 5, 3]
# b = []
# [b.insert(0, x) for x in a[::-1] if x not in b]
# b = b[::-1]
# print(b)
#
#
# array98
#
# a = [2, 3, 3, 2, 3, 4, 2, 2]
# b = [x for x in a if a.count(x) >= 3]
# print(b)
#
#
# array99
#
# a = [2, 3, 3, 2, 3, 4, 2, 2]
# b = [x for x in a if a.count(x) <= 2]
# print(b)
#
#
#
# array100
#
# a = [1, 2, 2, 3, 4, 4, 5]
# b = [x for x in a if a.count(x) != 2]
# print(b)
#
#
# array101
#
# a = [5, 7, 9, 11, 13]
# k = 3
# a[k-1:k] = [0]
# print(a)
#
#
# array102
#
# a = [5, 7, 9, 11, 13]
# k = 2
# a[k+1:k+2] = [0]
# print(a)
#
#
# array103
#
# a = [8, 2, 5, 10, 4, 6]
# min_i = a.index(min(a))
# max_i = a.index(max(a))
# a[max(0, min_i-1):min_i] = [0]
# a[max_i+1:max_i+2] = [0]
# print(a)
#
#
#
# array104
#
# a = [8, 3, 10, 5, 2, 7]
# min_i = a.index(min(a))
# max_i = a.index(max(a))
#
# if min_i > 0:
#     a[min_i - 1] = 0
# if max_i > 0:
#     a[max_i - 1] = 0
#
# print(a)
#
#
#
# array105
#
# a = [5, 8, 3, 10, 6, 2]
# min_i = a.index(min(a))
# max_i = a.index(max(a))
#
# if min_i < len(a) - 1:
#     a[min_i + 1] = 0
# if max_i > 0:
#     a[max_i - 1] = 0
#
# print(a)
#
#
# array106
#
# a = [4, 8, 2, 7, 10, 3]
# min_i = a.index(min(a))
# max_i = a.index(max(a))
#
# if min_i < max_i:
#     b = a[:min_i+1] + a[max_i:]
# else:
#     b = a[:max_i+1] + a[min_i:]
# print(b)
#
#
# array107
#
# a = [4, 8, 2, 7, 10, 3]
# min_i = a.index(min(a))
# max_i = a.index(max(a))
#
# start = min(min_i, max_i)
# end = max(min_i, max_i)
# a[start+1:end] = [0] * (end - start - 1)
# print(a)
#
#
# array108
#
# a = [5, 2, 8, 10, 4, 9]
# min_i = a.index(min(a))
# max_i = a.index(max(a))
#
# if min_i < max_i:
#     b = a[:min_i+1] + a[max_i+1:]
# else:
#     b = a[:max_i+1] + a[min_i+1:]
# print(b)
#
#
# array109
#
# a = [5, 10, 3, 8, 2, 7]
# min_i = a.index(min(a))
# max_i = a.index(max(a))
#
# if max_i < min_i:
#     b = a[:max_i+1] + a[min_i+1:]
# else:
#     b = a[:min_i+1] + a[max_i+1:]
# print(b)
#
#
# array110
#
# a = [1, 2, 3, 4, 5]
# b = a[::-1]
# print(b)
#
#
# array111
#
# a = [1, 2, 3, 4, 5, 6]
# for i in range(0, len(a)-1, 2):
#     a[i], a[i+1] = a[i+1], a[i]
# print(a)
#
#
# array116
#
a = [2, 2, 2, 3, 3, 5, 5, 5, 5]
b = []
c = []

i = 0
while i < len(a):
    j = i
    while j < len(a) and a[j] == a[i]:
        j += 1
    b.append(j - i)
    c.append(a[i])
    i = j

print("B:", b)
print("C:", c)
#
#
# array117
#
#
# a = [2, 2, 2, 3, 3, 5, 5, 5]
# b = []
# i = 0
# while i < len(a):
#     b.append(0)
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         b.append(a[i])
#         j += 1
#     i = j
# print(b)
#
#
# array118
#
# a = [2, 2, 3, 3, 3, 5]
# b = []
# i = 0
# while i < len(a):
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         b.append(a[i])
#         j += 1
#     b.append(0)
#     i = j
# print(b)
#
#
# array119
#
# a = [2, 2, 3, 3, 5]
# b = []
# i = 0
# while i < len(a):
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         b.append(a[i])
#         j += 1
#     b.append(9)
#     i = j
# print(b)
#
#
# array120
#
# a = [2, 2, 2, 3, 3, 5, 5]
# b = []
# i = 0
# while i < len(a):
#     b.append(a[i])
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         j += 1
#     i = j
# print(b)
#
#
# array121
#
# a = [2, 2, 3, 3, 5]
# k = 2
# b = []
# i = 0
# count = 0
#
# while i < len(a):
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         j += 1
#     count += 1
#     if count == k:
#         b += [a[i]] * ((j - i) * 2)
#     else:
#         b += a[i:j]
#     i = j
# print(b)
#
#
# array122
#
#
# a = [2, 2, 3, 3, 5]
# k = 2
# b = []
# i = 0
# count = 0
#
# while i < len(a):
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         j += 1
#     count += 1
#     if count != k:
#         b += a[i:j]
#     i = j
# print(b)
#
#
# array123
#
# a = [2, 2, 3, 3, 5, 5]
# k = 2
# series = []
#
# i = 0
# while i < len(a):
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         j += 1
#     series.append(a[i:j])
#     i = j
#
# if k <= len(series):
#     series[0], series[k-1] = series[k-1], series[0]
# b = sum(series, [])
# print(b)
#
#
# array124
#
#
# a = [2, 2, 3, 3, 5, 5]
# k = 2
# series = []
#
# i = 0
# while i < len(a):
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         j += 1
#     series.append(a[i:j])
#     i = j
#
# if k <= len(series):
#     series[k-1], series[-1] = series[-1], series[k-1]
# b = sum(series, [])
# print(b)
#
#
# array125
#
# a = [2, 2, 3, 3, 3, 5]
# k = 3
# b = []
# i = 0
# while i < len(a):
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         j += 1
#     if (j - i) < k:
#         b.append(0)
#     else:
#         b += a[i:j]
#     i = j
# print(b)
#
#
# array126
#
# a = [2, 2, 3, 3, 3, 5, 5, 5, 5]
# k = 2
# b = []
# i = 0
# while i < len(a):
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         j += 1
#     if (j - i) == k:
#         b.append(0)
#     else:
#         b += a[i:j]
#     i = j
# print(b)
#
#
# aray127
#
# a = [2, 2, 2, 3, 3, 5]
# k = 2
# b = []
# i = 0
# while i < len(a):
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         j += 1
#     if (j - i) > k:
#         b.append(0)
#     else:
#         b += a[i:j]
#     i = j
# print(b)
#
# array128
#
# a = [2, 2, 2, 3, 3, 5, 5]
# series = []
# i = 0
# while i < len(a):
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         j += 1
#     series.append(a[i:j])
#     i = j
#
# max_len = max(len(s) for s in series)
# for s in series:
#     if len(s) == max_len:
#         s.append(9)
#         break
# b = sum(series, [])
# print(b)
#
#
#
# array129
#
# a = [2, 2, 2, 3, 3, 5, 5, 5]
# series = []
# i = 0
# while i < len(a):
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         j += 1
#     series.append(a[i:j])
#     i = j
#
# max_len = max(len(s) for s in series)
# for s in reversed(series):
#     if len(s) == max_len:
#         s.append(9)
#         break
# b = sum(series, [])
# print(b)
#
#
# array130
#
# a = [2, 2, 3, 3, 5]
# b = []
# i = 0
# while i < len(a):
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         j += 1
#     b += a[i:j] + [9]
#     i = j
# print(b)
#
#
#
#
#
