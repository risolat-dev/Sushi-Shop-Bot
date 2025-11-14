# # file38
# #
# # f=open("file38.txt","r")
# # s=f.read().split()
# # a=list(map(int,s))
# # print(a)
# # f.close()
# # f=open("file38.txt","w")
# # for i in range(len(a)):
# #     if i%2==1:
# #         a[i]=2*a[i]
# #         f.write(str(a[i])+' ')
# # f.close()
# #
# #
# # a = list(range(10))
# # print(a)
# # b = [i for  i in a if i%5==0 and i%2==1]
# # print(b)
# #
# #
# # a = list(range(10))
# # print(a)
# # b = [i*5 for  i in a ]
# # print(b)
# #
# #
# # a = '''asdfg qwertghasdf asfg asdfg werty asdfg 34rty'''
# # c = a.split()
# # print(a)
# # b =' '.join([a for  i in c if len(i)>4])
# # print(b)
# #
# # a = lambda e,r,t,y: e+r+t+y
# # print(a(1,2,3,4))
# #
# # a = list(range(10))
# # print(a)
# # b= list(map(lambda x: x**2, a))
# # print(b)
#
# a = list(range(10))
# print(a)
# b= list(map(lambda x:2%x ,list(filter(lambda x: x**2, a))))
# print(b)
#
#
# # Text5
# S = input("Qo‘shiladigan satrni kiriting: ")
#
# with open("matn.txt", "a", encoding="utf-8") as f:
#     f.write("\n" + S)
#
# print("S satr fayl oxiriga qo‘shiladi.")
#
#
# # Text6
# with open("fayl1.txt", "r", encoding="utf-8") as f1:
#     matn1 = f1.read()
#
# with open("fayl2.txt", "r", encoding="utf-8") as f2:
#     matn2 = f2.read()
#
# with open("fayl1.txt", "w", encoding="utf-8") as f1:
#     f1.write(matn1 + "\n" + matn2)
#
# print("Ikkinchi fayl birinchi fayl oxiriga qo‘shildi.")
#
#
# # Text7
# S = input("Boshiga qo‘shiladigan satrni kiriting: ")
#
# with open("matn.txt", "r", encoding="utf-8") as f:
#     eski = f.read()
#
# with open("matn.txt", "w", encoding="utf-8") as f:
#     f.write(S + "\n" + eski)
#
# print("S satr fayl boshiga qo‘shildi.")
#
# # Text8
# with open("fayl1.txt", "r", encoding="utf-8") as f1:
#     matn1 = f1.read()
#
# with open("fayl2.txt", "r", encoding="utf-8") as f2:
#     matn2 = f2.read()
#
# with open("fayl1.txt", "w", encoding="utf-8") as f1:
#     f1.write(matn2 + "\n" + matn1)
#
# print("Ikkinchi fayl birinchi fayl boshiga qo‘shildi.")
#
# # Text9
# K = int(input("K ni kiriting: "))
#
# with open("matn.txt", "r", encoding="utf-8") as f:
#     a = f.read().split("\n")
#
# if 1 <= K <= len(a):
#     a.insert(K - 1, "")
#
# with open("natija.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(a))
#
# # Text10
# K = int(input("K ni kiriting: "))
#
# with open("matn.txt", "r", encoding="utf-8") as f:
#     a = f.read().split("\n")
#
# if 1 <= K <= len(a):
#     a.insert(K, "")
#
# with open("natija.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(a))
#
#
# # Text11
# with open("matn.txt", "r", encoding="utf-8") as f:
#     a = f.read().split("\n")
#
# natija = []
# for s in a:
#     natija.append(s)
#     if s.strip() == "":
#         natija.append("")
#
# with open("natija.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(natija))
#
# # Text12
# S = input("Bo‘sh satr o‘rniga yoziladigan S satrni kiriting: ")
#
# with open("matn.txt", "r", encoding="utf-8") as f:
#     a = f.read().split("\n")
#
# for i in range(len(a)):
#     if a[i].strip() == "":
#         a[i] = S
#
# with open("natija.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(a))
#
# # Text13
# with open("matn.txt", "r", encoding="utf-8") as f:
#     a = f.read().split("\n")
#
# if len(a) > 0:
#     a.pop(0)
#
# with open("natija.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(a))
#
# # Text14
# with open("matn.txt", "r", encoding="utf-8") as f:
#     a = f.read().split("\n")
#
# if len(a) > 0:
#     a.pop()
#
# with open("natija.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(a))
#
#
# # Text15
# K = int(input("K ni kiriting: "))
#
# with open("matn.txt", "r", encoding="utf-8") as f:
#     a = f.read().split("\n")
#
# if 1 <= K <= len(a):
#     a.pop(K-1)
#
# with open("natija.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(a))
#
#
#
# # Text16
# with open("matn.txt", "r", encoding="utf-8") as f:
#     a = f.read().split("\n")
#
# yangi = [s for s in a if s.strip() != ""]
#
# with open("natija.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(yangi))
#
# # Text17
# with open("fayl1.txt", "r", encoding="utf-8") as f1:
#     a1 = f1.read().split("\n")
#
# with open("fayl2.txt", "r", encoding="utf-8") as f2:
#     a2 = f2.read().split("\n")
#
# natija = []
# for i in range(min(len(a1), len(a2))):
#     natija.append(a1[i] + a2[i])
#
# if len(a1) > len(a2):
#     natija += a1[len(a2):]
#
# with open("natija.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(natija))
#
#
# # Text18
# K = int(input("K ni kiriting: "))
#
# with open("matn.txt", "r", encoding="utf-8") as f:
#     a = f.read().split("\n")
#
# natija = []
# for s in a:
#     if len(s) > K:
#         natija.append(s[K:])
#     else:
#         natija.append("")
#
# with open("natija.txt", "w", encoding="utf-8") as f:
#     f.write("\n".join(natija))
#
# # Text19
# with open("matn.txt", "r", encoding="utf-8") as f:
#     matn = f.read()
#
# matn = matn.swapcase()
#
# with open("natija.txt", "w", encoding="utf-8") as f:
#     f.write(matn)
#
# # Text20
# with open("matn.txt", "r", encoding="utf-8") as f:
#     matn = f.read()
#
# while "  " in matn:
#     matn = matn.replace("  ", " ")
#
# with open("natija.txt", "w", encoding="utf-8") as f:
#     f.write(matn)
#
#
#
# # Text21
# with open("matn.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#
# for line in lines[-3:]:
#     print(line.strip())
#
# # Text22
# K = int(input("K ni kiriting: "))
#
# with open("matn.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#
# for line in lines[-K:]:
#     print(line.strip())
#
# # Text23
# K = int(input("K ni kiriting: "))
#
# with open("matn.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#
# with open("yangi_fayl.txt", "w", encoding="utf-8") as f:
#     f.writelines(lines[:K])
#
# print("Yangi fayl yaratildi.")
#
# # Text24
# with open("matn.txt", "r", encoding="utf-8") as f:
#     text = f.read()
#
# p = [p for p in text.split("\n\n") if p.strip() != ""]
# print("Abzaslar soni:", len(p))
#
# # Text25
# K = int(input("O‘chiriladigan abzas raqamini kiriting: "))
#
# with open("matn.txt", "r", encoding="utf-8") as f:
#     text = f.read()
#
# p = [p for p in text.split("\n\n") if p.strip() != ""]
#
# if 1 <= K <= len(p):
#     p.pop(K - 1)
#
# with open("natija.txt", "w", encoding="utf-8") as f:
#     f.write("\n\n".join(p))
#
#
# # Text26
# with open("matn.txt", "r", encoding="utf-8") as f:
#     text = f.read()
#
# p = [p for p in text.split("\n\n") if p.strip() != ""]
# count = 0
# for p in p:
#     first_line = p.split("\n")[0]
#     if not first_line.startswith("     "):
#         count += 1
#
# print("Hisobga olingan abzaslar soni:", count)
#
#
# # Text27
# K = int(input("O‘chiriladigan abzas raqami: "))
#
# with open("matn.txt", "r", encoding="utf-8") as f:
#     text = f.read()
#
# p = [p for p in text.split("\n\n") if not p.startswith("     ")]
#
# if 1 <= K <= len(p):
#     p.pop(K - 1)
#
# with open("natija.txt", "w", encoding="utf-8") as f:
#     f.write("\n\n".join(p))
#
#
# # Text28
# with open("matn.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()
#
# result = []
# for line in lines:
#     result.append(line)
#     if line.startswith("     "):
#         result.append("\n")
#
# with open("natija.txt", "w", encoding="utf-8") as f:
#     f.writelines(result)
#
# # Text29
# with open("matn.txt", "r", encoding="utf-8") as f:
#     text = f.read()
#
# s = text.split()
# l = max(s, key=len)
# print("Eng uzun so‘z:", l)
#
#
# # Text30
# with open("matn.txt", "r", encoding="utf-8") as f:
#     text = f.read()
#
# s = text.split()
# shortest_length = min(len(w) for w in s)
# shortest_words = [w for w in s if len(w) == shortest_length]
#
# print("Eng qisqa oxirgi so‘z:", shortest_words[-1])