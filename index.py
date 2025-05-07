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

# thisTuple=("apple", "banana", "cherry")
# print(thisTuple)
# print(type(thisTuple))
# print(len(thisTuple))
# print(thisTuple[1])
# for x in thisTuple:
#     print(x)

# for i in range(len(thisTuple)):
#     print(thisTuple[i])
    
# tuple1=("a","b","c")
# tuple2=(1,2,3)
# tuple3=tuple1 + tuple2
# print(tuple3) 

# myTuple=thisTuple*3
# print(myTuple)   



# number = (1,3,4,6,7,3,5,3,7)
# print(number.count(3))
# print(number.count(7))
# print(number.index(4))



# dictionary methods

# studentData = {"name":"mantahsa sheikh","class":"twelth","subject":"maths","age":21}
# print(studentData)

# print(len(studentData))

# print(type(studentData))

# print(studentData["class"])

# del studentData["class"]
# print(studentData)

# print(studentData.get("name"))


# key is mandatary
# print(studentData.pop("subject")) 


# key is not mandatary it removes the items from the last
# print(studentData.popitem())

# for i in studentData.items():
#     print(i)
    
# for j in studentData.keys():
#     print(j)
    
# for k in studentData.values():
#     print(k)
    
# studentData.setdefault("grade","A")            

# foodItems={"fruits":"mango","vegetable":"ladyfinger"}
# foodItems.clear()
# print(foodItems)


# ternary operator

# check the number is even or odd

# number = int(input("enter a number:"))
# print(number,":is even") if(number%2==0) else print(number, ":is odd")

# check the number is multiple of 5 or not

# num = int(input("enter a number:"))
# print(num,": is multiple of 5") if(num%5==0) else print(num,":is not a multiple of 5")

# check the age is eligible for vote or not

# age = int(input("enter a number:"))
# print("person is eligible for vote") if(age>=18) else print("the person is not eligible for vote")

# check the given password is correct or not

# password = int(input("enter a password:"))
# print("password is correct") if(password==1234) else print("password is not correct")

# check the given number in between 1-100 or not

# n = int(input("enter a number:"))
# print(n, ":is between 1-100") if(n>=0 and n<=100) else print(n,":is not between 1-100")

# check the number is positive or negative

# number1 = -2
# print(number1, ":is positive") if(number1>=0) else print(number1, ":is negative")

# range function

# print(range(0,6))
# print(list(range(0,6)))
# print(tuple(range(1,6,2)))
# print(list(range(-1, -11, -2)))


# questin:- (using nested if else)order place in restaurant

menu = {"pizza":150, "Burger":100, "Momos":50, "dry":80}
print(menu)
order = input("enter a order(pizza, Burger, Momos, dry):")


if (order=="pizza"):
    quantity = int(input("enter a quantity:"))
    if (quantity>0):
        print("prize of pizza is:", 150*quantity)
    else:
        print("invalid quatity")
        
elif (order=="Burger"):
    quantity = int(input("enter a quantity:"))
    if (quantity>0):
        print("prize of pizza is:", 100*quantity)
    else:
        print("invalid quatity") 
        
elif (order=="Momos"):
    quantity = int(input("enter a quantity:"))
    if (quantity>0):
        print("prize of pizza is:", 50*quantity)
    else:
        print("invalid quatity") 
        
elif (order=="dry"):
    quantity = int(input("enter a quantity:"))
    if (quantity>0):
        print("prize of pizza is:", 80*quantity)
    else:
        print("invalid quatity")
        
else:
    print("this is not available") 
    
    
#question:-
 
studentMarks = int(input("enter a student marks:"))
if (studentMarks>0 and studentMarks<=30):
    print("student grade is :" , "D")
elif (studentMarks>30 and studentMarks<=50):
    print("student grade is :" , "C" )
elif (studentMarks>50 and studentMarks<=70):
    print("student grade is :" , "B" )
elif (studentMarks>70 and studentMarks<=100):
    print("student grade is :" , "A" )
else:
    print("invalid marks")    
    
    
# question:-

salary = int(input("enter a salary:"))
if (salary>0 and salary<=10000):
    mobileName = input("enter a mobile name (nokia, realme, iphone):") 
    if (mobileName=="nokia"):
        print("prize of nokia:" , 5000)
    
    
    
elif (salary>0 and salary<=10000):
    mobileName = input("enter a mobile name (nokia, realme, iphone):")
    if (mobileName=="realme"):
        print("prize of realme:" , 30000 )
     
    
elif (salary>0 and salary<=10000):
    mobileName = input("enter a mobile name (nokia, realme, iphone):") 
    if (mobileName=="iphone"):
        print("prize of iphone:" , 80000)
    
    
else:
    print("invalid salary")    
            
    
    
         
        
        
       
     
                                   
        
    
    














