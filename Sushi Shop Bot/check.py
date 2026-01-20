# r="R\tisolat is good person , and she is good at python."
#
#
# x=r.expandtabs()
#
#
# print(x)
#
#
# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# txt3 = "My name is {}, I'm {}".format("John",36)
#
# print(txt1)
# print(txt2)
# print(txt3)
#
# a= "My name is {name}, I'm {age}".format(name = "Risolat" , age = 19)
# print(a)
#
# name="risolat"
# city = "Tashkent"
# x = "My name is %s i live in %s." % (name, city)
# print(x)
#
# fruits = "apple, banana, cherry"
# vegetables = "potato , tomato, carrots"
# x= "i love %s and %s. " % (fruits, vegetables)
# print(x)
#
# name = "Risolat"
# city = "Tashkent"
# r = "My name is {} and I live in {}. ".format(name,city)
# print(r)
#
# name = "Risolat"
# city = "Tashkent"
# r="My name is {0} and I live in {1} ." .format(name, city)
# print(r)
#
# n="Risolat"
# c="Tashkent"
# e= "My name is {name} and I live in {city} ." .format(name =n, city= c)
# print(e)
#
# thelist = ["risolat" , "cool" , "cool", "risolat"]
# thelist[3] = "cool"
# list1 = ["cool", "volfram","text","davlatovna"]
# list1[2]="banana"
# # thelist.append(list1)
# thelist.extend(list1)
# thelist.insert(2,"orange")
# thelist.remove("orange")
# thelist.pop(2)
# thelist.pop() #lastitem
# del thelist[3]
# thelist.clear()
# for r in thelist:
#     print(r)
# for index in range(len(thelist)):
#     print(thelist[index])
# [print(thelist) for index in range(len(thelist))]
# [print(thelist[i]) for i in range(len(thelist)) if "a" in thelist[i]]
# thelist.sort()
# print(thelist)
# thelist.sort(reverse=True)
# print(thelist)
# thelist.sort(key=str.lower)
# print(thelist)
# newlist= thelist.copy()
# print(newlist)
# newlist = list(thelist)
# print(newlist)
# newlist = thelist[:]
# print(newlist)
# newlist.extend(list1)
# list3 = newlist + thelist
# print(list3)
# for x in newlist:
#     list3.append(x)
# print(list3)
# list1.extend(newlist)
# list1.remove("cool")
# list1.remove("risolat")
# print(thelist)
# print(list1)
# list1.count()
# print(list1)
#
# r = ("cool" , "omina" , "risolat" , "temur" , "gozal")
# print(len(tuple))
# tuple = ("cool",)
# string = ("cool")
# print(type(tuple))
# print(type(string))
# tuple = tuple(("cool"))
# print(type(tuple))
# print(tuple[2:4])
# if "cool" in tuple:
#     print('Yes "cool" is in the tuple')
# y = list(r)
# y[0] = "Omina"
# r= tuple(y)
# print(r) #now tuple is also changeable
# o = ("Risolat",)
# r+=o
# print(r)
# del r
# (mood, first, second,third, fourth) = r #unpacking tuple
# print(mood)
# print(first)
# print(second)
# print(third)
# print(fourth)
#
# (mood, *people) = r
# print(mood)
# print(people)

# theset = {"risolat" , "omina" }
# print(theset)
# print(type(theset))
# print(len(theset))
# theset= set(("risolat" , "omina"))
# print(theset)
# for x in theset:
#     print(x)
# print("risolat" in theset)
# print("omina" not in theset)
# theset.add("davlat")
# print(theset)
# thisset = {"temur" , "gozal"}
# theset.update(thisset)
# print(theset)
# theset.discard("gozal")
# theset.remove("gozal")
# x=theset.pop()
# print(x)
# print(theset)
# theset.clear()
# print(theset)
# del theset
# print(theset)
# set1 = theset.union(thisset)
# print(set1)
# set1 =  thisset | theset
# print(set1)
# set1 = theset.union(r)
# print(set1)
# set1 = theset.intersection(thisset)
# print(set1)
# set1 = theset & thisset
# print(set1)
# theset.intersection_update(thisset)
# print(theset)
# theset.difference(thisset)
# print(theset)
# set1 = theset - thisset
# print(set1)
# theset.difference_update(thisset)
# print(theset)
# theset.symmetric_difference(thisset)
# print(theset)
# thisset.symmetric_difference_update(theset)
# print(thisset)
# set1 = theset ^ thisset
# print(set1)
# x = frozenset({"risolat" , "omina"})
# print(x)
# print(type(x))
# y=x.copy()
# print(y)
# print(x.difference(y))
# print(x.intersection(y))
# print(x&y)
# print(x.isdisjoint(y))
# print(x.issubset(y))
# print(x>y)
# print(x>=y)
# print(x.symmetric_difference(y))
# print(x^y)
# print(x.union(y))
# print(x|y)
#
thedict = {
    "Name" : "Risolat",
    "Last name" : "Jo'raboyeva" ,
    "Age" : 19,
}
print(thedict)
print(len(thedict))
thedict = dict(name = "Risolat" , Lastname = "Jo'raboyeva" , Age = 19)
print(thedict)
x= thedict.keys()
print(x)
y = thedict.values()
print(y)
z = thedict.items()
print(z)
a = thedict["Lastname"]
print(a)





