# masala
#
# a=50
# b=10
# c=0
#
# while a>10:
#         a-=1
#         if a%3==0:
#             print(a)
#
# w1
#
# a=int(input("a="))
# b=int(input("b="))
#
# while a>b:
#     a-=b
# print(a)
#
# w2
#
# a=int(input("a="))
# b=int(input("b="))
# c = 0
# while a >= b:
#     a -= b
#     c += 1
# print(c)
#
#
# w3
#
# n=int(input("n="))
# k=int(input("k="))
# i=0
# while n>k:
#     i+=1
#     n-=k
# print(i, "butun" , n , " qoldiq")
#
# w4
#
#
# n = int(input("n="))
# i=0
# while n>3**i:
#     i+=1
# if n == 1:
#     print("3 ning darajasi")
# else:
#     print("3 ning darajasi emas")
#
#
# w5
#
# n=int(input("n="))
# K = 0
# c = 1
#
# while c < n:
#     c = c * 2
#     K = K + 1
#
# k = c - n
#
# print("K =", K)
# print("k =", k)
# print("Tek: 2^K - k =", c - k)
#
# w6
# n = int(input("n= "))
# result = 1
# i = n
#
# while i > 0:
#     result = result * i
#     i = i - 2
#
# print("n!! =", result)
#
# w7
#
# n=int(input("n="))
# k=1
# while k*k <= n:
#     k+=1
#     print(k)
# print(k)
#
# w8
#
# n=int(input("n="))
# k=1
#
# while (n>=k**2):
#     k+=1
# print(k)
#
#
# w9
#
# n=int(input("n="))
# k=0
# c=1
# while c<=n:
#     k+=1
#     c = c * 3
# print( "k=" ,  k , "daraja = " , c)
#
# w10
#
# n = int(input("n="))
# k = 0
# c = 1
#
# while c*3<= n:
#     c*=3
#     k+=1
#
# print("k =", k, "daraja =", c)
#
# w11
#
# n = int(input("n="))
# k=1
# s=0
# while n>=s:
#     k+=1
#     s+=k
#     print("k=", k-1)
# print("k=", k-1)
#
# w12
# n = int(input("n="))
# k =0
# b =0
# while b +(k+1)<=n:
#     k+=1
#     b+=k
# print("Eng katta k =", k)
# print("1 dan", k, "gacha bo‘lgan sonlar yig‘indisi =", b)
#
#
# w13
#
# a=int(input("a="))
# k=1
# s=0
# while a>=s:
#     k+=1
#     s+=1/k
#     print("k=",k-1)
# print("k=",k-1)
#
# w14
# a=float(input("a="))
# k=0
# s=0
# while s + 1/(k+1) <= a:
#     k+=1
#     s+=1/k
#     print("k=" , k , "s=" ,s)
#
# w15
#
# b=float(input("summa="))
# p=float(input("foiz="))
# o=2
# c=0
# h=b
# while h < b * o:
#     c += 1
#     h = h * (1 + p / 100)
#     print("Oy:", c, " | Joriy summa:", h)
# print("Necha oyda:", c, "oyda 2 baravar bo‘ladi")
#
#
#
# w16
#
# a=10
# p=int(input("p="))
# k=1
# while a<200:
#     k+=1
#     a=a+a*p/100
# print ( k, a)
#
# w17
#
# n=int(input("n="))
# m=int(input("m="))
# i=0
# while n>m:
#     i+=1
#     n-=m
# print(i, "butun" , n , " qoldiq")
#
# w18
#
# n = int(input("n="))
# while n>0:
#     a=n%10
#     n=n//10
#     print(a, end="")
#
# w19
#
# n = int(input("n="))
# i = 0
# s = 0
#
# while n > 0:
#     i += 1
#     a = n % 10
#     s += a
#     n = n // 10
#
# print("Raqamlar soni:", i)
# print("Raqamlar yig‘indisi:", s)
#
# w20
#
# n = int(input("n="))
#
# while n > 0:
#     c = n % 10
#     if c == 2:
#         print("Berilgan son ichida 2 raqami bor.")
#         break
#     n = n // 10
# else:
#     print("Berilgan son ichida 2 raqami yo'q.")
#
# w21
#
# n = int(input("n="))
#
# while n > 0:
#     c = n % 10
#     if c % 2 != 0:
#         print("Berilgan son ichida toq raqam bor.")
#         break
#     n = n // 10
# else:
#     print("Berilgan son ichida toq raqam yo'q.")
#
#
# w22
#
# n = int(input("n="))
#
# if n <= 1:
#     print("n 1 dan katta bo'lishi kerak!")
# else:
#     k = 2
#     while k < n:
#         if n % k == 0:
#             print("Tub emas.")
#             break
#         k += 1
#     else:
#         print("Tub son.")
#
# w23
#
# a = int(input("a="))
# b = int(input("b="))
#
# while a != b:
#     if a > b:
#         a = a - b
#     else:
#         b = b - a
#
# print("EKUB =", a)
#
# w24
#
# n = int(input("n="))
# a = 1
# b = 1
# while b < n:
#     a, b = b, a + b
# if b == n:
#     print("Bu son Fibonachchi soni.")
# else:
#     print("Bu son Fibonachchi soni emas.")
#
#
# w25
#
# n = int(input("n = "))
# a = 1
# b = 1
# while b <= n:
#     a, b = b, a + b
# print("n dan katta birinchi Fibonachchi son:", b)
#
# w30

