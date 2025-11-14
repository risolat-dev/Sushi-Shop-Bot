# # m1
# #
# from random import randint
# # n=randint(5,15)
# # print("n=" , n)
# # a=randint(10,20)
# # print("1." , a)
# # max=a+b
# # min=a
# # for i in range (2, n+1):
# #     a=randint(10,20)
# #     print(f"{i}.  " , a)
# #     if max <a:
# #         max=a
# #     if min >a:
# #         min=a
# # print("max = " , max)
# # print("min = " , min)
# #
# #
# # m2
# #
# # n = randint(5, 15)
# # print("n =", n)
# #
# # a = randint(10, 20)
# # b = randint(10, 20)
# # print("1.", a, b)
# # min_area = a * b
# # min_a = a
# # min_b = b
# #
# # for i in range(2, n + 1):
# #     a = randint(10, 20)
# #     b = randint(10, 20)
# #     print(f"{i}. " , a, b)
# #     area = a * b
# #     if area < min_area:
# #         min_area = area
# #         min_a = a
# #         min_b = b
# #
# # print("a =", min_a, "b =", min_b, "yuzasi =", min_area)
# #
# #
# #
# # m3
# #
# # n = randint(10, 20)
# # print("n=" , n)
# # a=randint(10,20)
# # b=randint(10,20)
# # print("1." , a,b)
# # max = a+b
# # for i in range (2,n+1):
# #     a = randint(10, 20)
# #     b = randint(10, 20)
# #     print (f"{i}.  ", a,b)
# #     if max < a+b:
# #         max = a+b
# # print("max= ", max)
# #
# # m4
# #
# # n = randint(5, 15)
# # print("n =", n)
# # a = randint(10, 99)
# # print("1.", a)
# # min_val = a
# # min_index = 1
# #
# # for i in range(2, n + 1):
# #     a = randint(10, 99)
# #     print(f"{i}. {a}")
# #     if a < min_val:
# #         min_val = a
# #         min_index = i
# #
# # print("Eng kichik element =", min_val)
# # print("Uning o‘rni =", min_index)
# #
# #
# # m5
# #
# # n = randint(5,15)
# # print("n=" , n)
# # m=randint(10,20)
# # v= randint(10,20)
# # print("1." , m, v)
# # p_max=m/v
# # for i in range ( 2, n+1):
# #     m = randint(10, 20)
# #     v = randint(10, 20)
# #     print(f"{i} .  ", m, v)
# #     if p_max < m/v:
# #         p_max=m/v
# # print("Zichlik = " , p_max)
# #
# #
# # m6
#
# n = randint(5, 15)
# print("n =", n)
#
# a = randint(10, 99)
# print("1.", a)
# min_val = a
# max_val = a
# min_index = 1
# max_index = 1
#
# for i in range(2, n + 1):
#     a = randint(10, 99)
#     print(f"{i}. {a}")
#
#     if a < min_val:
#         min_val = a
#         min_index = i
#
#     if a >= max_val:
#         max_val = a
#         max_index = i
#
# print("Eng kichik element:", min_val, "→ tartib raqami:", min_index)
# print("Eng katta element:", max_val, "→ oxirgi uchragan o‘rni:", max_index)
#
# m7
#
# n = randint(5, 15)
# print("n =", n)
#
# a = randint(10, 99)
# print("1.", a)
# max_val = a
# min_val = a
# max_index = 1
# min_index = 1
#
# for i in range(2, n + 1):
#     a = randint(10, 99)
#     print(f"{i}. {a}")
#
#     if a > max_val:
#         max_val = a
#         max_index = i
#
#     if a <= min_val:
#         min_val = a
#         min_index = i
#
# print("Eng katta element:", max_val, "→ birinchi uchragan o‘rni:", max_index)
# print("Eng kichik element:", min_val, "→ oxirgi uchragan o‘rni:", min_index)
#
# m8
#
#
# n = randint(5, 15)
# print("n =", n)
#
# a = randint(10, 99)
# print("1.", a)
# min_val = a
# first_min_index = 1
# last_min_index = 1
#
# for i in range(2, n + 1):
#     a = randint(10, 99)
#     print(f"{i}. {a}")
#
#     if a < min_val:
#         min_val = a
#         first_min_index = i
#         last_min_index = i
#     elif a == min_val:
#         last_min_index = i
#
# print("Eng kichik element:", min_val)
# print("Birinchi uchragan o‘rni:", first_min_index)
# print("Oxirgi uchragan o‘rni:", last_min_index)
#
#
# # m9
# #
# #
# # n = randint(5, 10)
# # print("n =", n)
# # x = randint(1, 20)
# # print("1. ", x)
# # max = 0
# # first = 0
# # last = 0
# # for i in range(2, n + 1):
# #     x = randint(1, 20)
# #     print(f"{i}. " , x)
# #
# #     if x > max:
# #         max = x
# #         first = i
# #         last = i
# #     if x >= max:
# #         last = i
# # print("Birinchi o‘rni:", first)
# # print("Oxirgi o‘rni:", last)
# #
#
# m10
#
# n = randint(5, 15)
# print("n =", n)
#
# a = randint(10, 99)
# print("1.", a)
# min_val = a
# max_val = a
# extreme_index = 1
#
# for i in range(2, n + 1):
#     a = randint(10, 99)
#     print(f"{i}. {a}")
#
#
#     if a < min_val:
#         min_val = a
#         extreme_index = i
#
#     if a > max_val:
#         max_val = a
#         extreme_index = i
#
# print("Eng kichik element:", min_val)
# print("Eng katta element:", max_val)
# print("Birinchi uchragan ekstremal elementning tartib raqami:", extreme_index)
#
# m11
#
# n = randint(5, 15)
# print("n =", n)
#
# a = randint(10, 99)
# print("1.", a)
# min_val = a
# max_val = a
# extreme_index = 1  # hozircha 1-element
#
# for i in range(2, n + 1):
#     a = randint(10, 99)
#     print(f"{i}. {a}")
#
#     if a < min_val:
#         min_val = a
#         extreme_index = i
#     elif a > max_val:
#         max_val = a
#         extreme_index = i
#     elif a == min_val or a == max_val:
#         extreme_index = i
#
# print("\nEng kichik element:", min_val)
# print("Eng katta element:", max_val)
# print("Oxirgi uchragan ekstremal elementning tartib raqami:", extreme_index)
#
# m12
#
# n = randint(5, 15)
# print("n =", n)
#
# a = randint(-10, 10)
# print("1.", a)
#
# if a > 0:
#     min_pos = a
# else:
#     min_pos = 0
#
# for i in range(2, n + 1):
#     a = randint(-10, 10)
#     print(f"{i}. {a}")
#
#     if a > 0:
#         if min_pos == 0 or a < min_pos:
#             min_pos = a
#
# print("Eng kichik musbat son:", min_pos)
#
#
# # m13
# #
# from random import randint
#
# n = randint(1, 20)
# print("n =", n)
#
# max_odd = 0
# index = 0
#
# for i in range(1, n + 1):
#     a = randint(1, 20)
#     print(f"{i}. {a}")
#
#     if a % 2 == 1:
#         if a > max_odd:
#             max_odd = a
#             index = i
#
# if index == 0:
#     print("0")
# else:
#     print("Birinchi eng katta toq element:", max_odd)
#     print("Tartib raqami:", index)
#
# m14
#
#
# B = randint(5, 20)
# print("B =", B)
#
# n = 10
# min_greater = 0
# index = 0
#
# for i in range(1, n + 1):
#     a = randint(1, 30)
#     print(f"{i}. {a}")
#     if a > B and (min_greater == 0 or a < min_greater):
#         min_greater = a
#         index = i
#
# if index == 0:
#     print("0")
# else:
#     print("Eng kichik B dan katta element:", min_greater)
#     print("Tartib raqami:", index)
#
# m15
#
#
# B = randint(1, 10)
# C = randint(B + 1, 20)
# print("B =", B, " C =", C)
# n = 10
# max_in_range = 0
# index = 0
#
# for i in range(1, n + 1):
#     a = randint(-10, 30)
#     print(f"{i}. {a}")
#
#     if B < a < C:
#         if max_in_range == 0 or a > max_in_range:
#             max_in_range = a
#             index = i
#
# if index == 0:
#     print("0")
# else:
#     print(f"(B, C) = ({B}, {C}) oraliqdagi eng katta element: {max_in_range}")
#     print("Tartib raqami:", index)
#
# m16
#
# n = randint(5, 15)
# print("n =", n)
#
# a = randint(-10, 30)
# print("1.", a)
# min_val = a
# min_index = 1
#
# for i in range(2, n + 1):
#     a = randint(-10, 30)
#     print(f"{i}. {a}")
#     if a < min_val:
#         min_val = a
#         min_index = i
#
# print("Eng kichik element:", min_val)
# print("Uning tartib raqami:", min_index)
# print("Unga qadar bo‘lgan elementlar soni:", min_index - 1)
#
# m17
#
#
# n = randint(5, 15)
# print("n =", n)
# a = randint(-10, 30)
# print("1.", a)
# max_val = a
# max_index = 1
# for i in range(2, n + 1):
#     a = randint(-10, 30)
#     print(f"{i}. {a}")
#     if a >= max_val:
#         max_val = a
#         max_index = i
#
# print("Eng katta element:", max_val)
# print("Uning oxirgi uchragan tartib raqami:", max_index)
# print("Undan keyingi elementlar soni:", n - max_index)
#
    