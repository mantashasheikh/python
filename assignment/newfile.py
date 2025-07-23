# string method

s = "this is the python class"
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.index("p"))
print(s.count("s"))
print(s.find("P"))
s1 = "python"
s2 = "language"
s3 = ' '.join([s1,s2])
print(s3)
print(type(s))

s4 = "this is a python class"
res = s.split()
print(res)

res1 = s.split("i",2)
print(res1)

x = "a"
print(ord(x))
y = "A"
print(ord(y))
z = "0"
print(ord((z)))
space = " "
print(ord(space))

print(chr(1))
print(chr(32))
print(chr(48))
print(chr(65))
print(chr(97))

# list pyhton function

l = [1,2,"python","java"]
print(l)
print(len(l))
print(type(l))
print(id(l))
print(list())

li = ["Python","Java","php"]
print(max(li))
print(min(li))
# print(sum(li))

li2 = [10,20,10.5,10+5j]
print(sum(li2))
# print(max(li2))
# print(min(li2))

li3 = [23,20.4,50,6.10]
print(max(li3))
print(min(li3))



# operators
l1 = [1,2,3,4,"python"]
l2 = ["java"]
print(l1+l2)
l1 = [1,2,3,4,"python"]
l2 = ["java"]
# print(l1-l2)
# print(l1*l2)
print(l1*3)
print(4 in l1)
l3 = [1,2,3,4]
l4 = [1,2,3,4]
print(l3 == l4)
print(l3 is l4)


# list methods
l = [2,4,"python","java","php",1,5,10,2,3]
x = l.append(50)
print(x)
# print(l.append(50))
# print(l)
# x = 10
# y = print(x)
# print(y)

# l.extend(2,4,6)
l.extend("python")
print(l)
l.extend([1,2,3,4])
print(l)
l.extend((-1,-2,-3))
print(l)
x = l.copy()
print(x)
print(l)
print(id(x),id(l))
# l.clear()
# print(l)
# del l
# print(l)
print(l.count(2))
print(l.index("python"))
l.insert(0,"neeraj")
print(l)
l.insert(5,"mantasha")
print(l)
print(l.pop())
print(l)
print(l.pop(6))
l.remove("python")
print(l)
l.reverse()
print(l)
# l.sort()
# print(l)
l1 = ["name","age","qualification"]
l1.sort()
l1.reverse()
print(l1)

l2 = [1,4,2,3,5]
l2.sort(reverse=True)
print(l2)












