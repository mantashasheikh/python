#syntax to print output
print("hello world")

#this is a comment

#variables
x = 5
y = "john"
print(x)
print(y)

#casting
a = str(3)
b = int(3)
c = float(3)
print(a)
print(b)
print(c)

#get the type
print(type(x))
print(type(y))

#tells the memory address
d = 2.34
print(id(d))

#python operators
#practice questions
#area of rectangle
length = 6
width = 3
area = length * width
print(area)

#area of triangle
base = 3
height = 6
areaOfTriangle = 0.5*base*height
print(areaOfTriangle)

#area of circle
radius = 2
areaOfCircle = 3.14*radius*radius
print(areaOfCircle)

#celcius to fahrenheit
celcius = 45
fahrenheit = (celcius*9/5)+32
print(fahrenheit)



#string
print("hello world")
print('hello world')

str = "hello, world!"
print(str[1])

for x in "banana":
    print(x)
    
string = "mantasha sheikh"
print(len(string))

txt = "I am a teacher of class 10th"
print("class" in txt)
print("she" in txt)

text = "my name is mantasha sheikh"
if "mantasha" in text:
    print("true")
else:
    print("false")
    
print("mantasha" not in text)
print("rimsha" not in text)

word = " hello world! "
print(word[2:5])
print(word[:5])
print(word[2:])
print(word[-5:-2])

print(word.upper())
print(word.lower())
print(word.strip())
print(word.replace("h", "J"))    
print(word.split(","))

str1 = "max"
str2 = "well"
str3 = str1+str2
print(str3)    

str4 = str1+" "+str2
print(str4)  

age = 36
print( f"my name is john, I am {age}")

price = 59
print(f"the price is {price:.2f} dollar")

print(f"The price is {20*59} dollars")

t = "tony stark is a super hero . he is so powerful"
print(t.capitalize())
print(t.center(100))
print(t.count("is"))
print(t.endswith("powerful"))
print(t.find("hero"))
print(t.startswith("tony"))


#python booleans
print(10>2)
print(10==9)
print(10<9)


print(bool("hello"))
print(bool(15))
print(bool(["apple","mango","banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(()))
print(bool(""))
print(bool([]))
print(bool({}))


#python list[]
thislist = ["apple","mango","banana","apple"]
print(thislist)
print(len(thislist))
print(type(thislist))

print(thislist[1])
print(thislist[-1])
print(thislist[1:4])
print(thislist[-4:-1])

if "apple" in thislist:
    print("yes, apple is present in thislist")

thislist[1] = "blackcurrent"
print(thislist)   

thislist[1:3] = ["blackcurrent","watermelon"]
print(thislist) 

thislist.insert(2,"watermelon")
print(thislist)

list = ["tomato","potato","brinjal","ladyfinger"]
print(len(list))
list.append("pumpkin")
print(list)
print(len(list))

list.insert(1,"onion")
print(list)
print(len(list))

thislist = ["apple","mango","banana"]
tropical = ["cherry","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)

thistuple = ("kiwi","orange")
thislist.extend(thistuple)
print(thislist)

list.remove("brinjal")
print(list)

list.pop(1)
print(list)

del list[0]
print(list)

del list
print(list)

name = ["mantasha","rimsha","umra","iqra","bushra"]
name.clear()
print(name)

name = ["mantasha","rimsha","umra","iqra","bushra"]
name.sort()
print(name)

name.sort(reverse=True)
print(name)

city = ["Bhopal","delhi","Mumbai","Kolkata"]
city.sort()
print(city)

city.reverse()
print(city)

mylist = city.copy()
print(mylist)

mylist = list(name)
print(mylist)

list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1 +list2
print(list3)

list4 = [7,8,9]
for x in list4:
    list1.append(x)
print(list1)

list5 = [12,23,34]
list1.extend(list2)
print(list1)  

my_list1 = []
my_list2 = list()
print(my_list1)
print(my_list2)
my_list = list()
my_list.append(10)
print(my_list)
my_list.extend([2,4,6])
print(my_list)
my_list.insert(1,"python")
print(my_list)
my_list[0] = 20
print(my_list)
my_list.pop(0)
print(my_list)
my_list.remove("python")
print(my_list)


#python tuples
# python inbuilt function
my_tuple = (2,4,6,8,"python","java")
print(len(my_tuple))
print(id(my_tuple))
print(type(my_tuple))
print(tuple())

# print(min(my_tuple))
# print(max(my_tuple))
# print(sum(my_tuple))

my_tuple1 = (2,4,3.5,8,6.98,6.5)
print(min(my_tuple1))
print(max(my_tuple1))
print(sum(my_tuple1))

# tuple inbuilt method
t = (2,4,6,8,2,4,6)
print(t.index(8))

print(t.count(8))





# python dictionary
my_dict = {'name':'Neeraj', 'age':37, 'qulification':'M.tech'}

print(my_dict)
print(type(my_dict))
print(id(my_dict))
print(len(my_dict))
print(max(my_dict))
print(min(my_dict))
# print(sum(my_dict))
print(dict())


dict2 = {1:'neeraj', 2:37, 3:'mtech'}
print(sum(dict2))

# dict3 = {1:'neeraj', 2:37, '3':'mtech'}
# print(min(dict3))
# print(max(dict3))
# print(sum(dict3))

x = {}
print(type(x))

d = {'name':'neeraj', 'age':34, 'qualification':'Mtech'}
print(d.keys())
print(d.values())
print(d.items())
print(d)
print(d.get('name'))

d1 = {1:'python',2:'php'}
d.update(d1)
print(d)

d.setdefault('name','rahul')
print(d)

d.setdefault('name1','rahul')
print(d)

l = ['name','age','city','contact']
d = d.fromkeys(l)
print(d)

d['name'] = 'Neeraj'
print(d)

d.pop('age')
print(d)

d.popitem()
print(d)

d.copy()
print(d)



# python set
# python inbuile=t function

my_set = {2,4,"python","java","php",2,4,9}
print(my_set)
print(type(my_set))
print(id(my_set))
print(len(my_set))
# print(min(my_set))
# print(max(my_set))
# print(sum(my_set))

my_set2 = {"python","java","php"}
print(max(my_set2))
print(min(my_set2))

my_set3 = {2,2.6,3,4.9}
print(sum(my_set3))


# mathematical operation on set
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

# s1.intersection_update(s2)
# print(s1)
# s1.difference_update(s2)
# print(s1)
# s1.symmetric_difference_update(s2)
# print(s1)

s3 = {1,2,3,4,5,6,7,8,9,10,11,12}
s4 = {2,6,9,11}

print(s3.isdisjoint(s4))
print(s3.issubset(s4))
print(s3.issuperset(s4))

s = set()
s.add("python")
print(s)

# s.update("python")
# print(s)

# s.update(10,20,30,40)
# print(s)
# s.update("java","php")
# print(s)
# s.update("p","y","t","h","o","n")
# print(s)
s.update(["java","php"])
print(s)
print(s.pop())
print(s)
# s.remove("python")
# print(s)
# s.remove("neeraj")
# print(s)
s.discard("neeraj")
print(s)

s5 = s.copy()
print(s5,s)
print(id(s5),id(s))

s.clear()
print(s)


# frozen set

fs = frozenset()
l = [2,4,8,10]
fs = frozenset(l)
print(fs)

# typecasting
x = 10
y = str(x)
print(y)
print(type(y))






















  