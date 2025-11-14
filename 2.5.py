# a = [2, 2, 2, 3, 3, 5, 5, 5, 5]
# b = []
# c = []
#
# i = 0
# while i < len(a):
#     j = i
#     while j < len(a) and a[j] == a[i]:
#         j += 1
#     b.append(j - i)
#     c.append(a[i])
#     i = j
#
# print("B:", b)
# print("C:", c)
#
# b = [3, 2, 4]
# c = [2, 3, 5]
# a = []
# for i in range (len(c)):
#     for j in range (c[i]):
#         a.append(b[i])
# print("A" , a)
#
# array118
#
# a = [2, 2, 2, 3, 3, 5, 5, 5, 5]
# for i in range (1,len(a)):
#     for j in range (a[i]):
#         a.append(a[i])
#     a.append(a[0])
# print(b)
#
#
#
#
# array123
#
# a = [2, 2, 3, 3, 5, 5]
# k = 2
# b = []
# e = 0
# for i in range(1, len(a) + 1):
#     if i == len(a) or a[i] != a[i - 1]:
#         b.append(a[e:i])
#         e = i
# if k <= len(b):
#     b[0], b[k - 1] = b[k - 1], b[0]
# b = [x for s in b for x in s]
# print(b)
#
# def add_number (a:int,b:int, c:int, d:int):
#     if type(a)==int and type(b)==int and type(c)==int and type(d)==int:
#         return a+b+c+d
#     else:
#         return "Invalid input"
# a1=(add_number(34,56 , 45, 12))
# b1=(add_number(23,2 , 34, 56))
# c1=(add_number(11,32,67,89))
# d1=(add_number(12,22,12,56))
# print(a1)
# print(b1)
# print(c1)
# print(d1)
#
#
#
# def list_max_min(a:list):
#     index_max = a.index(max(a))
#     index_min = a.index(min(a))
#     return f"max index = {a[index_max]}, min index = {a[index_min]}"
#
# a = [45,23,56,78,101]
# print(list_max_min(a))

# strings
#
# for x in "banana":
#   print(x)
#
# a = "Hello, World!"
# print(len(a))
#
# txt = "The best things in life are free!"
# print("free" in txt)
#
# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")
#
# txt = "The best things in life are free!"
# print("expensive" not in txt)
#
# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")
#
# Slicing
#
# b = "Hello, World!"
# print(b[2:5])
#
# b = "Hello, World!"
# print(b[:5])
#
# b = "Hello, World!"
# print(b[2:])
#
# b = "Hello, World!"
# print(b[-5:-2])
#
# Modify
#
# a = "Hello, World!"
# print(a.upper())
#
# a = "Hello, World!"
# print(a.lower())
#
# a = " Hello, World! "
# print(a.strip())
#
#
# a = "Hello, World!"
# print(a.replace("H", "J"))
#
# a = "Hello, World!"
# print(a.split(","))
#
# Concatenation
#
# a = "Hello"
# b = "World"
# c = a + b
# print(c)
#
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)
#
# 2-topshiriq
#
#
s = "ewer ewrreqwr eqwfrgewrtg qeeer qwerer qwe qeq eq qwert qwerty asd asdfg qqqqqq"
w = s.split()
q = ["zzz","zzz","zzz"]
r = ""
for x in w:
    for i in range(3):
        if len(x) < len(q[i]):
            q[i] = x
            break
for x in w:
    if len(x)==6:
        r += x+" "
        if r.count(" ")==3:
            break
for x in q:
    r = x+" "+r
while len(r)<100:
    r += "x"
print(r[:100])
print(len(r[:100]))


