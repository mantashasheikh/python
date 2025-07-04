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


#python list
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














  