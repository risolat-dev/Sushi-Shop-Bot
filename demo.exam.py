# # 1m
# #
# # x1 =float(input("x1="))
# # x2 =float(input("x2="))
# # y1 =float(input("y1="))
# # y2 =float(input("y2="))
# #
# # d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
# # print("Masofa =", d)
# #
# #
# # 2m
# # N = int(input("sekund="))
# # h= N//3600
# # m= (N%3600)//60
# # s = N%60
# # print("Soat " , h,"minut " , m, " sekund " , s)
# #
# # 3m
# # a = int(input("a="))
# # b = int(input("b="))
# # c = int(input("c="))
# # d = (a > 0 and b > 0 and c <= 0) or (a > 0 and c > 0 and b <= 0) or (b > 0 and c > 0 and a <= 0)
# # print(d)
# #
# # 4m
# # yil = int(input("Yilni kiriting: "))
# #
# # if yil % 400 == 0:
# #     a = 366
# # elif yil % 100 == 0:
# #     a = 365
# # elif yil % 4 == 0:
# #     a = 366
# # else:
# #     a = 365
# #
# # print(yil, "yilida", a, "kun bor")
# #
# # 5m
# # n = int(input("n = "))
# #
# # A = 2
# # for i in range(n):
# #     print(f"A{i} = {A}")
# #     A = 2 + 1 / A
# #
# # 6m
# #
# # b=float(input("summa="))
# # p=float(input("foiz="))
# # o=2
# # c=0
# # h=b
# # while h < b * o:
# #     c += 1
# #     h = h * (1 + p / 100)
# #     print("Oy:", c, " | Joriy summa:", h)
# # print("Necha oyda:", c, "oyda 2 baravar bo‘ladi")
# #
# # 7m
# # from random import randint
# # n = randint(5, 20)
# # print("n =", n)
# # a = randint(10, 30)
# # print("1.", a)
# # min_val = a
# # max_val = a
# # extreme_index = 1
# #
# # for i in range(2, n + 1):
# #     a = randint(10, 30)
# #     print(f"{i}. {a}")
# #
# #
# #     if a < min_val:
# #         min_val = a
# #         extreme_index = i
# #
# #     if a > max_val:
# #         max_val = a
# #         extreme_index = i
# #
# # print("Eng kichik element:", min_val)
# # print("Eng katta element:", max_val)
# # print("Birinchi uchragan ekstremal elementning tartib raqami:", extreme_index)
#
#
# # homework
# 19begin
# x1 = int(input("x1 = "))
# y1 = int(input("y1 = "))
# x2 = int(input("x2 = "))
# y2 = int(input("y2 = "))
#
# a = abs(x2 - x1)
# b = abs(y2 - y1)
#
# P = 2 * (a + b)
# S = a * b
#
# print("Perimetri =", P)
# print("Yuzasi =", S)
#
# Begin20
# x1 = int(input("x1 = "))
# y1 = int(input("y1 = "))
# x2 = int(input("x2 = "))
# y2 = int(input("y2 = "))
#
# d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#
# print("Masofa =", d)
#
#
# # # 15int
# # a=int(input("a="))
# # a1= a%10
# # a2= a//10%10
# # a3=a//100%10
# #
# # b=a1+a2*100+a3*10
# # print(b)
#
# 22int
#
#
# N = int(input("N sekundni kiriting: "))
# N = N % 86400
#
# s = N // 3600
# q = N % 3600
# m = q // 60
# sek = q % 60
#
# print(s, "soat", m, "minut", sek, "sekund o'tdi")
#
#
# 20bool
#
# # a=int(input("a="))
# # a1=a%10
# # a2=a//10%10
# # a3=a//100%10
# #
# # b = a1 != a2 and a2 != a3 and a1 != a3
# # print(b)
#
# 13bool
#
# # a=int(input("a="))
# # b=int(input("b="))
# # c=int(input("c="))
# # d=a>0 or b>0 or c>0
# # print(d)
#
# 29if
#
# # a = int(input("Butun sonni kiriting: "))
# #
# # if a == 0:
# #     print("Nolga teng")
# # elif a > 0 and a % 2 == 0:
# #     print("Musbat juft son")
# # elif a > 0 and a % 2 == 1:
# #     print("Musbat toq son")
# # elif a < 0 and a % 2 == 0:
# #     print("Manfiy juft son")
# # else:
# #     print("Manfiy toq son")
# #
#
# 30if
#
# # a = int(input("1 dan 999 gacha son kiriting: "))
# #
# # if a < 1 or a > 999:
# #     print("Son 1-999 oralig'ida emas!")
# # else:
# #     if a % 2 == 0:
# #         tur = "juft"
# #     else:
# #         tur = "toq"
# #
# # if a < 10:
# #         xona = "bir xonali"
# # elif a < 100:
# #         xona = "ikki xonali"
# # else:
# #         xona = "uch xonali"
# #
# # print(a, "soni", xona, tur, "son")
#
# 13for
#
# # n = int(input("n = "))
# # s = 0
# # c = 1
# # for i in range(1, n + 1):
# #     x = 1 + i / 10
# #     s += c * x
# #     c = -c
# #     print(s)
# #
# # print("Yig‘indi:", s)
# #
#
# 35for
#
# # n = int(input("n = "))
# #
# # A1 = 1
# # A2 = 2
# # A3 = 3
# #
# # print(f"A1 = {A1}")
# # print(f"A2 = {A2}")
# # print(f"A3 = {A3}")
# #
# # for k in range(4, n + 1):
# #     A = A3 + A2 - 2 * A1
# #     print(f"A{k} = {A}")
# #     A1 = A2
# #     A2 = A3
# #     A3 = A
#
# 12while
#
# # n = int(input("n="))
# # k =0
# # b =0
# # while b +(k+1)<=n:
# #     k+=1
# #     b+=k
# # print("Eng katta k =", k)
# # print("1 dan", k, "gacha bo‘lgan sonlar yig‘indisi =", b)
#
# 14while
#
# # a=float(input("a="))
# # k=0
# # s=0
# # while s + 1/(k+1) <= a:
# #     k+=1
# #     s+=1/k
# #     print("k=" , k , "s=" ,s)
#
