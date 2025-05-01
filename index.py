# area of square
# side = int(input("enter a side:"))
# print(side*side)

# Area of a circle
# radius = int(input("enter a radius:"))
# pie = 3.14
# Area1 = pie*radius*radius
# print(Area1) 

# Area of a triangle
# num = 0.5
# base = int(input("enter a base:"))
# height = int(input("enter a height:"))
# Area2 = num*base*height
# print(Area2)


# convert the celcius into farenheit
# celcius = int(input("enter a celcius"))
# farenheit = (celcius*9)/5+32
# print(farenheit)


# list methods

# fruits = ["apple","mango","banana","grapes"]
# fruits.insert(0,"watermelon")
# print(fruits)

# vegetables = ['ladyfinger','tomato','potato']
# vegetables.append("onion")  
# print(vegetables)   
             
# indoorGames = ["carrom","chess","ludo"]
# indoorGames.extend("table tennis")
# print(indoorGames)

# outdoorGames = ["badminton","cricket","football"]
# outdoorGames.pop(1)
# print(outdoorGames)

# flowersName = ["rose","lily","lotus","jasmine","marrygold","sunflower"]
# flowersName.remove("jasmine")
# print(flowersName)

# alpha = ['c','f','a','d','b','e']
# alpha.sort()
# print(alpha)

# alpha.reverse()
# print(alpha)

# l1 = ["cat", "dog", "rabbit"]
# l2 = ["lion","tiger","leopard"]
# print(l1,l2)
# del l1

# print(l2.count("leopard"))



# another question

# question = []
# question.append("Q1: Python was developed in:")
# question.append("Q2: c++ was developed in:")
# question.append("Q3: HTML was developed in:")
# question.append("Q4: when one is not a valid keyword in python:")
# question.append("Q5: full form of CSS:")
# question.pop()

# options =[
#     ("A: 1990", "B: 1991", "c: 1999", "D: 2000")
#     ("A: 1990", "B: 1990", "C: 1970", "C:2000")
#     ("A: 1991", "B: 1980", "C: 1999", "D: 2000")
#     ("A: true", "B:True", "C:False", "D: None")
#     ("A: cascarding style sheet", "B: cascading sheet", "C:cascading card", "D:cascading style sheet")
# ]

# answers =["B","C","A","A","D"]

# ans = []

# print(question[0])
# print(options[0])
# ans.append(input("select the correct option:").upper())
# points = points+1

# print(question[1])
# print(options[1])
# ans.append(input("select the correct option:").upper())

# print(question[2])
# print(options[2])
# ans.append(input("select the correct option:").upper())

# print(question[3])
# print(options[3])
# ans.append(input("select the correct option:").upper())

# print(question[4])
# print(options[4])
# ans.append(input("select the correct option:").upper())


# tuple methods

thisTuple=("apple", "banana", "cherry")
print(thisTuple)
print(type(thisTuple))
print(len(thisTuple))
print(thisTuple[1])
for x in thisTuple:
    print(x)

for i in range(len(thisTuple)):
    print(thisTuple[i])
    
tuple1=("a","b","c")
tuple2=(1,2,3)
tuple3=tuple1 + tuple2
print(tuple3) 

myTuple=thisTuple*3
print(myTuple)   



number = (1,3,4,6,7,3,5,3,7)
print(number.count(3))
print(number.count(7))
print(number.index(4))



# dictionary methods

studentData = {"name":"mantahsa sheikh","class":"twelth","subject":"maths","age":21}
print(studentData)

print(len(studentData))

print(type(studentData))

print(studentData["class"])

del studentData["class"]
print(studentData)

print(studentData.get("name"))


# key is mandatary
print(studentData.pop("subject")) 


# key is not mandatary it removes the items from the last
print(studentData.popitem())

for i in studentData.items():
    print(i)
    
for j in studentData.keys():
    print(j)
    
for k in studentData.values():
    print(k)
    
studentData.setdefault("grade","A")            

foodItems={"fruits":"mango","vegetable":"ladyfinger"}
foodItems.clear()
print(foodItems)








