# # s = 'dono     qiz    bola    bor    ekan'
# # sozlar = s.split()
# # sozlar = sozlar[::-1]
# # natija = " ".join(sozlar)
# # print(natija)
# #
# # s = 'dono     qiz    bola    bor    ekan'
# #
# # a = ""
# # r = []
# #
# # for b in s:
# #     if b != " ":
# #         a += b
# #     elif a != "":
# #         r.append(a)
# #         soz = ""
# # if a != "":
# #     r.append(a)
# #
# # for i in range(len(r)-1, -1, -1):
# #     print(r[i], end=" ")
# #
# #
# # s = 'sdfg, wefgf . wertre , werfgv!? wdefgv , qwe. edgfd!'
# #
# # tinish_belgilar = ['.', ',', ';', ':', '?', '!', '…', '-', '—', '(', ')', '[', ']', '{', '}', '«', '»', '"', "'", '/', '\\']
# #
# # count = 0
# #
# # for i in s:
# #     if i in tinish_belgilar:
# #         count += 1
# #
# # print(count)
# #
# # a = 'okefjn lkwmdfc lkwmfce wojmwe 3edjn uj wedf ujm wdf 3eds qwer'
# #
# # file5
# #
# #
# # a = open("butunson.txt", 'r')
# # s1 = a.read()
# # print(len(a.read()))
# # a.close()
# # a1=open("file38", 'w')
# # a1.write(s1[::-1])
# # a1.close()
# #
# file10
#
# a = open("file10.txt", 'r')
# s = a.read().split()
# a.close()
#
# a1 = open("file10yangi.txt", 'w')
# a1.write(" ".join(s[::-1]))
# a1.close()
#
#
# file11
#
# a = open("file11.txt", 'r')
# s = a.read().split()
# a.close()
#
# a1 = open("file11_1.txt", 'w')
# a2 = open("file11_2.txt", 'w')
#
# for i in range(len(s)):
#     if i % 2 == 0:
#         a1.write(s[i] + " ")
#     else:
#         a2.write(s[i] + " ")
#
# a1.close()
# a2.close()
#
# file12
#
# a = open("file12.txt", 'r')
# s = a.read().split()
# a.close()
#
# a1 = open("file12_juft.txt", 'w')
# a2 = open("file12_toq.txt", 'w')
#
# juft_bor = False
# toq_bor = False
#
# for x in s:
#     if int(x) % 2 == 0:
#         a1.write(x + " ")
#         juft_bor = True
#     else:
#         a2.write(x + " ")
#         toq_bor = True
#
# if not juft_bor:
#     a1.truncate(0)
# if not toq_bor:
#     a2.truncate(0)
#
# a1.close()
# a2.close()
#
#
# file13
#
# a = open("file13.txt", 'r')
# s = a.read().split()
# a.close()
#
# a1 = open("file13_musbat.txt", 'w')
# a2 = open("file13_manfiy.txt", 'w')
#
# musbat = []
# manfiy = []
#
# for x in s:
#     x = int(x)
#     if x > 0:
#         musbat.append(str(x))
#     elif x < 0:
#         manfiy.append(str(x))
#
# if musbat:
#     a1.write(" ".join(musbat[::-1]))
# if manfiy:
#     a2.write(" ".join(manfiy[::-1]))
#
# a1.close()
# a2.close()
#
#
# file14
#
# a = open("file14.txt", 'r')
# s = a.read().split()
# a.close()
#
# s = list(map(float, s))
# yig = sum(s)
# n = len(s)
# orta = yig / n
#
# print(orta)
#
#
#
# file15
#
# a = open("file15.txt", 'r')
# s = a.read().split()
# a.close()
#
# s = list(map(float, s))
# yig = 0
# for i in range(1, len(s), 2):
#     yig += s[i]
#
# print(yig)
#
#
# file16
#
# a = open("file16.txt", 'r')
# s = a.read().split()
# a.close()
#
# s = list(map(int, s))
# count = 1
#
# for i in range(1, len(s)):
#     if s[i] != s[i - 1]:
#         count += 1
#
# print(count)
#
#
#
#
# file17
#
# a = open("file17.txt", 'r')
# s = a.read().split()
# a.close()
#
# s = list(map(int, s))
# yangi = []
# c = 1
#
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         c += 1
#     else:
#         yangi.append(str(c))
#         c = 1
# yangi.append(str(c))
#
# a1 = open("file17_yangi.txt", 'w')
# a1.write(" ".join(yangi))
# a1.close()
#
#
#
# file18
#
# a = open("file18.txt", 'r')
# s = a.read().split()
# a.close()
#
# s = list(map(float, s))
# for i in range(1, len(s) - 1):
#     if s[i] < s[i - 1] and s[i] < s[i + 1]:
#         print(s[i])
#         break
#
#
#
# file19
#
#
# a = open("file19.txt", 'r')
# s = a.read().split()
# a.close()
#
# s = list(map(float, s))
# for i in range(1, len(s) - 1):
#     if s[i] > s[i - 1] and s[i] > s[i + 1]:
#         print(s[i])
#         break
#
#
#
# file20
#
# a = open("file20.txt", 'r')
# s = a.read().split()
# a.close()
#
# s = list(map(float, s))
# min_son = 0
# max_son = 0
#
# for i in range(1, len(s) - 1):
#     if s[i] < s[i - 1] and s[i] < s[i + 1]:
#         min_son += 1
#     if s[i] > s[i - 1] and s[i] > s[i + 1]:
#         max_son += 1
#
# print("Lokal minimumlar soni:", min_son)
# print("Lokal maksimumlar soni:", max_son)
#
#
# file21
#
#
# a = open("file21.txt", 'r')
# s = a.read().split()
# a.close()
#
# s = list(map(float, s))
# indexlar = []
#
# for i in range(1, len(s) - 1):
#     if s[i] > s[i - 1] and s[i] > s[i + 1]:
#         indexlar.append(str(i + 1))  # 1 dan boshlab sanaymiz
#
# a1 = open("file21_yangi.txt", 'w')
# a1.write(" ".join(indexlar))
# a1.close()
#
#
#
#
# file22
#
# a = open("file22.txt", 'r')
# s = a.read().split()
# a.close()
#
# s = list(map(float, s))
# indexlar = []
#
# for i in range(1, len(s) - 1):
#     if (s[i] < s[i - 1] and s[i] < s[i + 1]) or (s[i] > s[i - 1] and s[i] > s[i + 1]):
#         indexlar.append(i + 1)
#
# indexlar.sort(reverse=True)
#
# a1 = open("file22_yangi.txt", 'w')
# a1.write(" ".join(map(str, indexlar)))
# a1.close()
#
#
# file23
#
# a = open("file23.txt", 'r')
# s = a.read().split()
# a.close()
#
# s = list(map(float, s))
# uzunliklar = []
# uzun = 1
#
# for i in range(1, len(s)):
#     if s[i] < s[i - 1]:
#         uzun += 1
#     else:
#         if uzun > 1:
#             uzunliklar.append(str(uzun))
#         uzun = 1
# if uzun > 1:
#     uzunliklar.append(str(uzun))
#
# a1 = open("file23_yangi.txt", 'w')
# a1.write(" ".join(uzunliklar))
# a1.close()
#
#
# file24
#
#
# a = open("file24.txt", 'r')
# s = a.read().split()
# a.close()
#
# s = list(map(float, s))
# uzunliklar = []
# uzun = 1
#
# for i in range(1, len(s)):
#     if (s[i] > s[i - 1]) or (s[i] < s[i - 1]):
#         uzun += 1
#     else:
#         if uzun > 1:
#             uzunliklar.append(str(uzun))
#         uzun = 1
# if uzun > 1:
#     uzunliklar.append(str(uzun))
#
# a1 = open("file24_yangi.txt", 'w')
# a1.write(" ".join(uzunliklar))
# a1.close()
#
#
#
# file25
#
#
# a = open("file25.txt", 'r')
# s = a.read().split()
# a.close()
#
# s = [str(float(x)**2) for x in s]
#
# a1 = open("file25_yangi.txt", 'w')
# a1.write(" ".join(s))
# a1.close()
#
#
# file26
#
# a = open("file26.txt", 'r')
# s = list(map(float, a.read().split()))
# a.close()
#
# mx = max(s)
# mn = min(s)
# imax = s.index(mx)
# imin = s.index(mn)
#
# s[imax], s[imin] = s[imin], s[imax]
#
# a1 = open("file26_yangi.txt", 'w')
# a1.write(" ".join(map(str, s)))
# a1.close()
#
#
#
# file27
#
# a = open("file27.txt", 'r')
# s = a.read().split()
# a.close()
#
# yangi = []
# i = 0
# j = len(s) - 1
#
# while i <= j:
#     yangi.append(s[i])
#     if i != j:
#         yangi.append(s[j])
#     i += 1
#     j -= 1
#
# a1 = open("file27_yangi.txt", 'w')
# a1.write(" ".join(yangi))
# a1.close()
#
#
# file28
#
# a = open("file28.txt", 'r')
# s = list(map(float, a.read().split()))
# a.close()
#
# yangi = [s[0]]
# for i in range(1, len(s) - 1):
#     o = (s[i - 1] + s[i + 1]) / 2
#     yangi.append(o)
# yangi.append(s[-1])
#
# a1 = open("file28_yangi.txt", 'w')
# a1.write(" ".join(map(str, yangi)))
# a1.close()
#
#
#
# file29
#
#
# a = open("file29.txt", 'r')
# s = a.read().split()
# a.close()
#
# if len(s) > 10:
#     s = s[-10:]
#
# a1 = open("file29_yangi.txt", 'w')
# a1.write(" ".join(s))
# a1.close()
#
#
# file30
#
#
# a = open("file30.txt", 'r')
# s = a.read().split()
# a.close()
#
# if len(s) % 2 == 0:
#     s = s[:len(s)//2]
#
# a1 = open("file30_yangi.txt", 'w')
# a1.write(" ".join(s))
# a1.close()
#
#
#
# file31
#
# a = open("file31.txt", 'r')
# s = a.read().split()
# a.close()
#
# if len(s) > 10:
#     s = s[:10]
#
# a1 = open("file31_yangi.txt", 'w')
# a1.write(" ".join(s))
# a1.close()
#
#
# file32
#
# a = open("file32.txt", 'r')
# s = a.read().split()
# a.close()
#
# if len(s) % 2 == 0:
#     s = s[len(s)//2:]
#
# a1 = open("file32_yangi.txt", 'w')
# a1.write(" ".join(s))
# a1.close()
#
#
# file33
#
# a = open("file33.txt", 'r')
# s = a.read().split()
# a.close()
#
# yangi = []
# for i in range(len(s)):
#     if i % 2 != 0:
#         yangi.append(s[i])
#
# a1 = open("file33_yangi.txt", 'w')
# a1.write(" ".join(yangi))
# a1.close()
#
#
# file34
#
# a = open("file34.txt", 'r')
# s = list(map(float, a.read().split()))
# a.close()
#
# yangi = [str(x) for x in s if x >= 0]
#
# a1 = open("file34_yangi.txt", 'w')
# a1.write(" ".join(yangi))
# a1.close()
#
#
# file35
#
#
# a = open("file35.txt", 'r')
# s = a.read().split()
# a.close()
#
# while len(s) < 10:
#     s.insert(0, '0')
#
# a1 = open("file35_yangi.txt", 'w')
# a1.write(" ".join(s))
# a1.close()
#
