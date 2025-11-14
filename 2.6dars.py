# string28
#
#
#
# s = 'sfdd sdfg 345t jhg sd ytr'
# s1 = ''
#
# for i in s:
#     if i == 's':
#         s1+="ss"
#     else:
#         s1+=i
# print(s1)
#
# string30
#
#
# s = 'sfdd sdfg 345t jhg sd ytr'
# s1 = ''
#
# for i in s:
#     if i == 's':
#         s1+="1"
#     else:
#         s1+=i
# print(s1)
#
# string34
#
# s= "asdf df wedf wer sd rtdf"
# s2 = 'df'
# s4 = 'wewe'
# s1= s[::-1]
# s3 = s2[::-1]
# # s0=s1.replace(s3,"", 1)
# # print(s0[::-1])
# #
# # index = 0
# # for i in range (len(s1)- len(s3)):
# #     if s1[i:len(s2)+i] == s3:
# #         index = i
# #         break
# # s0=s1[:index] + s1[index+len(s2):]
# # print(s0[::-1])
# #
# # index = 0
# # for i in range (len(s)- len(s2)):
# #     if s[i:len(s2)+i] == s2:
# #         index = i
# # s0 = s[:index]+s[index+len(s2):]
# # print(s0)
# #
#
# s0=s[::-1].replace(s2[::-1],s4[::-1],1)
# print(s0[::-1])
#
#
s = "asfdgb asdfsg asdfgb"
index1 = s.find(" ")
index2 = s.rfind(" ")
if index1 == index2:
    print(" ")
else:
    print(s[index1:index2])
