# 1bool
# a=int(input("a="))
# s=a>0
# print(s)
#
# 2bool
# a=int(input("a="))
# s=a%2==1
# print(s)
#
# 3bool
#
# a=int(input("a="))
# s=a%2==0
# print(s)
#
# 4bool
# a=int(input("a="))
# b=int(input("b="))
# c= (a>2 and b<=3)
# print(c)
#
# 5bool
#
# a=int(input("a="))
# b=int(input("b="))
# c= a>=0 or b<-2
# print(c)
#
# 6bool
#
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d= a<=b<=c
# print(d)
#
# 7bool
#
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d= (a<b<c) or (c<b<a)
# print(d)
#
# 8bool
#
# a=int(input("a="))
# b=int(input("b="))
# d= a%2==1 and b%2==1
# print(d)
#
# 9bool
#
# a=int(input("a="))
# b=int(input("b="))
# d= a%2==1 or b%2==1
# print(d)
#
# 10bool
#
# a=int(input("a="))
# b=int(input("b="))
# d= (a%2==0 and b%2==1 ) or (a%2==1 and b%2==0)
# print(d)
#
# 11bool
#
# a=int(input("a="))
# b=int(input("b="))
# d= (a%2==1 and b%2==1 )or (a%2==0 and b%2==0)
# print(d)
#
# 12bool
#
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d=a>0 and b>0 and c>0
# print(d)
#
# 13bool
#
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d=a>0 or b>0 or c>0
# print(d)
#
# 14bool
#
# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))
#
# d = (a > 0 and b <= 0 and c <= 0) or (b > 0 and a <= 0 and c <= 0) or (c > 0 and a <= 0 and b <= 0)
#
# print(d)
#
#
# 15bool
#
# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))
# d = (a > 0 and b > 0 and c <= 0) or (a > 0 and c > 0 and b <= 0) or (b > 0 and c > 0 and a <= 0)
# print(d)
#
# 16bool
#
# a=int(input("a="))
# b= a%2==0 and 9<a<100
# print(b)
#
# 17bool
#
# a=int(input("a="))
# b= a%2==1 and 100<=a<1000
# print(b)
#
# 18bool
#
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d= a==b or a==c or b==c
# print(d)
#
# 19bool
#
# a=int(input("a="))
# b=int(input("b="))
# c=int(input("c="))
# d= (a == -b) or (a == -c) or (b == -c)
# print(d)
#
# 20bool
#
# a=int(input("a="))
# a1=a%10
# a2=a//10%10
# a3=a//100%10
#
# b = a1 != a2 and a2 != a3 and a1 != a3
# print(b)
#
# 21bool
#
# a=int(input("a="))
# a1=a%10
# a2=a//10%10
# a3=a//100%10
# b= a1>a2>a3
# print(b)
#
# 22bool
#
# a=int(input("a="))
# a1=a%10
# a2=a//10%10
# a3=a//100%10
# b= a1>a2>a3 or a1<a2<a3
# print(b)
#
# 23bool
#
# a=int(input("a="))
# a1=a%10
# a2=a//10%10
# a3=a//100%10
# b= a1==a3
# print(b)
#
# 24bool
#
# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))
#
# D = b*b - 4*a*c
# d = (D >= 0)
#
# print(d)
#
# 25bool
#
# x = int(input("x="))
# y = int(input("y="))
#
# a = (x < 0) and (y > 0)
#
# print(a)
#
# 26bool
#
# x = int(input("x="))
# y = int(input("y="))
#
# a = (x > 0) and (y < 0)
#
# print(a)
#
#
# 27bool
#
# x = int(input("x="))
# y = int(input("y="))
#
# a = (x < 0)
#
# print(a)
#
#
# 28bool
#
# x = int(input("x="))
# y = int(input("y="))
#
# a = (x > 0 and y > 0) or (x < 0 and y < 0)
#
# print(a)
#
# 29bool
#
# x = int(input("x = "))
# y = int(input("y = "))
# x1 = int(input("x1 = "))
# y1 = int(input("y1 = "))
# x2 = int(input("x2 = "))
# y2 = int(input("y2 = "))
#
# d = (x1 <= x <= x2) and (y2 <= y <= y1)
# print(d)
#
# 30bool
#
# a = float(input("a="))
# b = float(input("b="))
# c = float(input("c="))
#
# d = (a == b == c) and (a > 0)
# print(d)
#
# 31bool

a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
d = ((a == b) or (a == c) or (b == c)) and (a+b > c) and (a+c > b) and (b+c > a) and not (a == b == c)
print(d)
#
# 32bool
#
# a = float(input("a="))
# b = float(input("b="))
# c = float(input("c="))
#
# d = (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a)
#
# print(d)
#
# bool33
#
# a = float(input("a="))
# b = float(input("b="))
# c = float(input("c="))
#
# d = (a+b > c) and (a+c > b) and (b+c > a) and (a > 0) and (b > 0) and (c > 0)
#
# print(d)


