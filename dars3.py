# 1m
# a=int(input("a="))
# if a>0:
#     a=a+1
# print("a=",a)
#
# 3m
# a=int(input("a="))
# if a>0:
#     a=a-1
#     print("a = " , a)
# elif a<0:
#     a=a-2
#     print("a = ", a)
# elif a==0:
#     a=10
#     print("a = ", a)
#
# 4m
#
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# r=1
# if a>0:
#     r=1
# if b>0:
#     r=r+1
# if c>0:
#     r=r+1
# print("r=",r)
#
# 5m
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# musbat=0
# manfiy=0
# if a>0:
#     musbat=1
# if b>0:
#     musbat=musbat+1
# if c>0:
#     musbat=musbat+1
# print("Musbat sonlar",musbat, "ta")
#
# if a<0:
#     manfiy=1
# if b<0:
#     manfiy=manfiy+1
# if c<0:
#     manfiy=manfiy+1
# print("Manfiy sonlar",manfiy, "ta")
# 6m

# a=int(input("a="))
# b=int(input("b="))
#
# if a<b:
#     print("ikkinchi son:",a)
# if a>b:
#     print("ikkinchi son:",b)
#
# 8m
# a=2
# b=10
# # c-a
# # a=b
# # b=c
# if b>a:
#    print ("a=", a, "b=" , b)
# else:    a,b=b,a
# print ("a=", a, "b=" , b)
#
# 11m
#
# a=int(input("a="))
# b=int(input("b="))
# if a!=b:
#     if a>b:
#         b=a
#     else:
#         b=a
# else:
#     a=0
#     b=0
# print("a=", a, "b=",b)
#
# 14m
#
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
#
# if a > b:
#     a, b = b, a
# if a > c:
#     a, c = c, a
# if b > c:
#     b, c = c, b
#
# print("Kichkinadan kattaga:", a, b, c)
#
#
# 15m
#
# a = int(input("1-sonni kiriting: "))
# b = int(input("2-sonni kiriting: "))
# c = int(input("3-sonni kiriting: "))
#
# if a <= b and a <= c:
#     print("Sonlar:", b, "va", c)
#     print("Yig‘indi:", b + c)
# elif b <= a and b <= c:
#     print("Sonlar:", a, "va", c)
#     print("Yig‘indi:", a + c)
# else:
#     print("Sonlar:", a, "va", b)
#     print("Yig‘indi:", a + b)
#
# 16m
#
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
#
# if a < b and b < c:
#     a = a * 2
#     b = b * 2
#     c = c * 2
# else:
#     a = -a
#     b = -b
#     c = -c
#
# print("Result:", a, b, c)
#
# 18m
#
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
#
# if a == b and a != c:
#     print("Tartib raqami 3")
# elif a == c and a != b:
#     print("Tartib raqami 2")
# elif b == c and b != a:
#     print("Tartib raqami 1")
# else:
#     print("Ikkita teng son yo'q")
#
# 20m
#
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))
#
# if abs(a - b) < abs(a - c):
#     print("Eng yaqin nuqta b =", b, "Masofa =", abs(a - b))
# elif abs(a - c) < abs(a - b):
#     print("Eng yaqin nuqta c =", c, "Masofa =", abs(a - c))
# else:
#     print("b va c bilan bir xil masofada, Masofa =", abs(a - b))
#
# 22m
#
# x = int(input("x = "))
# y = int(input("y = "))
#
# if x > 0 and y > 0:
#     print("Nuqta I chorakda joylashgan")
# elif x < 0 and y > 0:
#     print("Nuqta II chorakda joylashgan")
# elif x < 0 and y < 0:
#     print("Nuqta III chorakda joylashgan")
# else:
#     print("Nuqta IV chorakda joylashgan")
#
# 24m
#
# x = float(input("x = "))
#
# if x > 0:
#     f = "2 * sin(x)"
# else:
#     f = "x - 6"
#
# print("f(x) =", f)
#
# 26m
#
# x = float(input("x = "))
#
# if x <= 0:
#     f = -x
# elif 0 < x < 2:
#     f = x * x
# else:
#     f = 4
#
# print("f(x) =", f)
#
#
# 27m
#
# x = float(input("x = "))
#
# if x < 0:
#     f = 0
# else:
#     n = int(x)
#
#     if n % 2 == 0:
#         f = 1
#     else:
#         f = -1
#
# print("f(x) =", f)
#
# 28m
#
# yil = int(input("Yilni kiriting: "))
#
# if yil % 400 == 0:
#     a = 366
# elif yil % 100 == 0:
#     a = 365
# elif yil % 4 == 0:
#     a = 366
# else:
#     a = 365
#
# print(yil, "yilida", a, "kun bor")
#
# 29m
#
# a = int(input("Butun sonni kiriting: "))
#
# if a == 0:
#     print("Nolga teng")
# elif a > 0 and a % 2 == 0:
#     print("Musbat juft son")
# elif a > 0 and a % 2 == 1:
#     print("Musbat toq son")
# elif a < 0 and a % 2 == 0:
#     print("Manfiy juft son")
# else:
#     print("Manfiy toq son")
#
# 30m
#
# a = int(input("1 dan 999 gacha son kiriting: "))
#
# if a < 1 or a > 999:
#     print("Son 1-999 oralig'ida emas!")
# else:
#     if a % 2 == 0:
#         tur = "juft"
#     else:
#         tur = "toq"
#
# if a < 10:
#         xona = "bir xonali"
# elif a < 100:
#         xona = "ikki xonali"
# else:
#         xona = "uch xonali"
#
# print(a, "soni", xona, tur, "son")
