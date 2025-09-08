# string method

s = "this is the python class .this class is very good"
# print(s.lower())
# print(s.upper())
# print(s.capitalize())
# print(s.title())
# print(s.index("p"))
# print(s.count("class"))
# print(s.find("P"))
# s1 = "python"
# s2 = "language"
# s3 = ' '.join([s1,s2])
# print(s3)
# print(type(s))

# s4 = "this is a python class"
# res = s.split()
# print(res)

# res1 = s.split("i",2)
# print(res1)

# x = "a"
# print(ord(x))
# y = "A"
# print(ord(y))
# z = "0"
# print(ord((z)))
# space = " "
# print(ord(space))

# print(chr(1))
# print(chr(32))
# print(chr(48))
# print(chr(65))
# print(chr(97))

# list pyhton function

# l = [1,2,"python","java"]
# print(l)
# print(len(l))
# print(type(l))
# print(id(l))
# print(list())

# li = ["Python","Java","php"]
# print(max(li))
# print(min(li))
# print(sum(li))

# li2 = [10,20,10.5,10+5j]
# print(sum(li2))
# # print(max(li2))
# # print(min(li2))

# li3 = [23,20.4,50,6.10]
# print(max(li3))
# print(min(li3))



# # operators
# l1 = [1,2,3,4,"python"]
# l2 = ["java"]
# print(l1+l2) #concatination
# l1 = [1,2,3,4,"python"]
# l2 = ["java"]
# # print(l1-l2)
# # print(l1*l2)
# print(l1*3) #repeatation
# print(4 in l1)
# l3 = [1,2,3,4]
# l4 = [1,2,3,4]
# print(l3 == l4)
# print(l3 is l4)


# list methods
# l = [2,4,"python","java","php",1,5,10,2,3]
# x = l.append(50)
# print(x)
# print(l.append(50))
# print(l)
# x = 10
# y = print(x)
# print(y)

# l.extend(2,4,6)
# l.extend("python")
# print(l)
# l.extend([1,2,3,4])
# print(l)
# l.extend((-1,-2,-3))
# print(l)
# x = l.copy()
# print(x)
# print(l)
# print(id(x),id(l))
# l.clear()
# print(l)
# del l
# print(l)
# print(l.count(2))
# print(l.index("python"))
# l.insert(0,"neeraj")
# print(l)
# l.insert(5,"mantasha")
# print(l)
# print(l.pop())
# print(l)
# print(l.pop(6))
# l.remove("python")
# print(l)
# l.reverse()
# print(l)
# l.sort()
# print(l)
# l1 = ["name","age","qualification"]
# l1.sort()
# l1.reverse()
# print(l1)

# l2 = [1,4,2,3,5]
# l2.sort(reverse=True)
# print(l2)


# #python tuples
# # python inbuilt function
# my_tuple = (2,4,6,8,"python","java")
# print(len(my_tuple))
# print(id(my_tuple))
# print(type(my_tuple))
# print(tuple())

# print(min(my_tuple))
# print(max(my_tuple))
# print(sum(my_tuple))

# my_tuple1 = (2,4,3.5,8,6.98,6.5)
# print(min(my_tuple1))
# print(max(my_tuple1))
# print(sum(my_tuple1))


# # tuple inbuilt method
# t = (2,4,6,8,2,4,6)
# print(t.index(8))

# print(t.count(8))





# # python dictionary
# my_dict = {'name':'Neeraj', 'age':37, 'qulification':'M.tech'}

# print(my_dict)
# print(type(my_dict))
# print(id(my_dict))
# print(len(my_dict))
# print(max(my_dict))
# print(min(my_dict))
# # print(sum(my_dict))
# print(dict())


# dict2 = {1:'neeraj', 2:37, 3:'mtech'}
# print(sum(dict2))

# # dict3 = {1:'neeraj', 2:37, '3':'mtech'}
# # print(min(dict3))
# # print(max(dict3))
# # print(sum(dict3))

# x = {}
# print(type(x))

# d = {'name':'neeraj', 'age':34, 'qualification':'Mtech'}
# print(d.keys())
# print(d.values())
# print(d.items())
# print(d)
# print(d.get('name'))

# d1 = {1:'python',2:'php'}
# d.update(d1)
# print(d)

# d.setdefault('name','rahul')
# print(d)

# d.setdefault('name1','rahul')
# print(d)

# l = ['name','age','city','contact']
# d = d.fromkeys(l)
# print(d)

# d = d.keys()
# print(d)

# d['name'] = 'Neeraj'
# print(d)

# d.pop('age')
# print(d)

# d.popitem()
# print(d)

# d.copy()
# print(d)



# # python set
# # python inbuile=t function
# my_set = {2,4,"python","java","php",2,4,9}
# print(my_set)
# print(type(my_set))
# print(id(my_set))
# print(len(my_set))
# print(min(my_set))
# print(max(my_set))
# print(sum(my_set))

# my_set2 = {"python","java","php"}
# print(max(my_set2))
# print(min(my_set2))

# my_set3 = {2,2.6,3,4.9}
# print(sum(my_set3))


# # mathematical operation on set
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))

# s1.intersection_update(s2)
# print(s1)
# s1.difference_update(s2)
# print(s1)
# s1.symmetric_difference_update(s2)
# print(s1)

# s3 = {1,2,3,4,5,6,7,8,9,10,11,12}
# s4 = {2,6,9,11}


# print(s4.isdisjoint(s3))
# print(s4.issubset(s3))
# print(s3.issuperset(s4))

s = set()
# s.add("python")
# print(s)

# # s.update("python")
# # print(s)

# s.update(10,20,30,40)
# print(s)
# s.update("java","php")
# print(s)
# s.update("p","y","t","h","o","n")
# print(s)
# s.update(["java","php"])
# print(s)
# print(s.pop())
# print(s)
# s.remove("python")
# print(s)
# s.remove("neeraj")
# print(s)
# s.discard("neeraj")
# print(s)

# s5 = s.copy()
# print(s5,s)
# print(id(s5),id(s))

# s.clear()
# print(s)


# # frozen set

# fs = frozenset()
# l = [2,4,8,10]
# fs = frozenset(l)
# print(fs)

# # typecasting
# # x = 10
# # y = str(x)
# # print(y)
# # print(type(y))


# r = (list(range(-1,-11,-1)))
# print(r)
# x = (list(range(-1,-1,-1)))
# print(x)









  












