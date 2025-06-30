# 1. write a program to find maximum between two number 
# li = [25,23]
# max = li[0]
# for i in range(len(li)):
#     if(max<li[i]):
#         max = li[i]
# print(max) 


# 2. write a program to print a maximum of three numbers
# li = [25,53,23]
# max = li[0]
# for i in range(len(li)):
#     if(max<li[i]):
#         max = li[i]
# print(max)
 

# 3.  write a program to check the given number is positive, negative ,or zero
# num = int(input("enter a number:"))
# if(num<0):
#     print(num, " :is negative")
# elif(num>0):
#     print(num, " :is positive")
# else:
#     print(num, " :is zero")

 

# 4. write a program to check whether the number is divisible by 5 and 11 or not
# num = int(input("enter a number:"))
# if(num%5==0 and num%11==0):
#     print(num, " :is divisible by 5 and 11")
# else:
#     print(num, ":is not divisible by 5 and 11")



# 5.  write a program to check whether a number is even or not
# num = int(input("enter a number:"))
# if(num%2==0):
#     print(num, ":is even")
# else:
#     print(num, ":is odd")


    
# 6.  write a program to check whether a year is leap year or not
# year = int(input("enter a year:"))
# if(year%4==0 and year%400):
#     print(year ,":is leap year")
# else:
#     print(year,":is not a leap year")

 

# 7.  write a program to check whether a character is alphabet or not
# char = input("enter a chracter:")
# if(char>='a' and char<='z')or(char>='A' and char<='Z'):
#     print(char , ":is Alphabet")
# else:
#     print(char, ":is not a alphabet")

 

# 8.  write a program to input any alphabet and check whether it is vowel or consonant
# alpha = input("enter a alphabet:")
# if(alpha=='a'or alpha=='e' or alpha=='i'or alpha=='o'or alpha=='u'or alpha=='A'or alpha=='E'or alpha=='I'or alpha=='O'or alpha=='U'):
#     print(alpha, " : is a vowel")
# else:
#     print(alpha, " : is a consonant")


    
# 9.  write a program to input any character and check whether it is alphabet, digit, or special character 
# any = input("enter anything:")
# if(any>="a" and any<="z")or(any>="A" and any<="Z"):
#     print(any , ": is a alphabet")
# elif(any>="0" and any<="9"):
#     print(any , " :is a digit")
# else:
#     print(any, " :is a special character")
    
     
    
# 10. write a program to check whether a character is uppercase and lowercase alphabet
# alpha = input("enter a alphabet:")
# if(alpha>="A" and alpha<="Z"):
#     print(alpha, ": this alphabet is in Uppercase")
# elif(alpha>="a" and alpha<="z"):
#     print(alpha, ": this alphabet is in lowercase ") 
# else:
#     print("invalid character")


    
# 11. write a program to input week number and print week days
# week = int(input("enter a  week number"))
# if(week==1):
#     print("monday")
# elif(week==2):
#     print("tuesday")
# elif(week==3):
#     print("wednesday")
# elif(week==4):
#     print("thursday")
# elif(week==5):
#     print("friday")
# elif(week==6):
#     print("saturday")
# elif(week==7):
#     print("sunday") 
# else:
#     print("nothing") 


# 12. write a program to input month number and print number of days in that month
# month = int(input("enter a month number:")) 
# if(month==1):
#     print("january = 31 days ")
# elif(month==2):
#     print("february = 28 or 29 days")
# elif(month==3):
#     print("march = 31 days")
# elif(month==4):
#     print("april = 30 days")
# elif(month==5):
#     print("may = 31 days")
# elif(month==6):
#     print("june = 30 days")
# elif(month==7):
#     print("july = 31 days")
# elif(month==8):
#     print("august = 30 days")
# elif(month==9):
#     print("september = 31 days")
# elif(month==10):
#     print("october = 31 days")
# elif(month==11):
#     print("november = 30 days")
# elif(month==12):
#     print("december = 31 days")
# else:
#     print("invalid number there are only 12 months")
 
    
    
# 13. write a program to count the total number of notes in the given amount
# amount = int(input("Enter the amount: Rs"))

# print(f"Calculating notes for amount: Rs {amount}")
# total_notes = 0

# if amount >= 500:
#     n500 = amount // 500
#     print("Rs500 notes:", n500)
#     total_notes += n500
#     amount = amount % 500

# if amount >= 200:
#     n200 = amount // 200
#     print("Rs200 notes:", n200)
#     total_notes += n200
#     amount = amount % 200

# if amount >= 100:
#     n100 = amount // 100
#     print("Rs100 notes:", n100)
#     total_notes += n100
#     amount = amount % 100

# if amount >= 50:
#     n50 = amount // 50
#     print("Rs50 notes:", n50)
#     total_notes += n50
#     amount = amount % 50

# if amount >= 20:
#     n20 = amount // 20
#     print("₹20 notes:", n20)
#     total_notes += n20
#     amount = amount % 20

# if amount >= 10:
#     n10 = amount // 10
#     print("Rs10 notes:", n10)
#     total_notes += n10
#     amount = amount % 10

# if amount >= 5:
#     n5 = amount // 5
#     print("Rs5 notes:", n5)
#     total_notes += n5
#     amount = amount % 5

# if amount >= 2:
#     n2 = amount // 2
#     print("Rs2 notes:", n2)
#     total_notes += n2
#     amount = amount % 2

# if amount >= 1:
#     n1 = amount
#     print("Rs1 notes:", n1)
#     total_notes += n1

# print("Total number of notes:", total_notes)




# 14. write a program to input angles of a triangle and check whether triangle is valid or not
# angle1 = float(input("enter angle1 :"))
# angle2 = float(input("enter angle2 :"))
# angle3 = float(input("enter angle3 :"))
# sum_of_angles = angle1 + angle2 + angle3
# if(angle1>0 and angle2>0 and angle3>0):
#     if(sum_of_angles==180):
#         print("this triangle is valid : ",sum_of_angles)
#     else:
#         print("this triangle is not valid")    
# else:
#     print("invalid angles") 
    


# 15. write a program to input all sides of a triangle and check whether th e triangle is valid or not
# a = float(input("Enter first side: "))
# b = float(input("Enter second side: "))
# c = float(input("Enter third side: "))
# if a > 0 and b > 0 and c > 0:
#     if (a + b > c) and (a + c > b) and (b + c > a):
#         print("The triangle is valid.")
#     else:
#         print("The triangle is not valid ")
# else:
#     print("The triangle is not valid ")
    
    


# 16. write a program to check whether the triangle is equilateral, isosceles, and scalene
# a = float(input("Enter side a: "))
# b = float(input("Enter side b: "))
# c = float(input("Enter side c: "))

# if a <= 0 or b <= 0 or c <= 0:
#     print("Invalid triangle: sides must be greater than zero.")
# else:
#     if (a + b > c) and (a + c > b) and (b + c > a):
#         if a == b == c:
#             print("The triangle is equilateral.")
#         elif a == b or b == c or a == c:
#             print("The triangle is isosceles.")
#         else:
#             print("The triangle is scalene.")
#     else:
#         print("Invalid triangle: violates the triangle inequality.") 
        
        

# 17. write a program to calculate profit or loss
# cost_price = float(input("Enter the Cost Price (CP): "))
# selling_price = float(input("Enter the Selling Price (SP): "))

# if selling_price > cost_price:
#     profit = selling_price - cost_price
#     print(f"Profit = ₹{profit:.2f}")
# elif cost_price > selling_price:
#     loss = cost_price - selling_price
#     print(f"Loss = ₹{loss:.2f}")
# else:
#     print("No Profit No Loss.")
    


# 18. Write a  program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
# physics = float(input("Enter marks in Physics: "))
# chemistry = float(input("Enter marks in Chemistry: "))
# biology = float(input("Enter marks in Biology: "))
# mathematics = float(input("Enter marks in Mathematics: "))
# computer = float(input("Enter marks in Computer: "))

# total_marks = physics + chemistry + biology + mathematics + computer
# percentage = (total_marks / 500) * 100

# print(f"Total Marks: {total_marks}/500")
# print(f"Percentage: {percentage:.2f}%")

# if percentage >= 90:
#     grade = "A"
# elif percentage >= 80:
#     grade = "B"
# elif percentage >= 70:
#     grade = "C"
# elif percentage >= 60:
#     grade = "D"
# elif percentage >= 40:
#     grade = "E"
# else:
#     grade = "F"

# print(f"Grade: {grade}")



# 20. Write a  program to input electricity unit charges and calculate total electricity bill according to the given condition:
# unit = int(input("enter a unit:"))
# if(unit>0 and unit<=50):
#     print("rupees per unit:", unit*0.50)
# elif(unit>50 and unit<=100):
#     print("rupees per unit:", unit*0.75-25)
# elif(unit>100 and unit<=150):
#     print("rupees per unit:", unit*1.20-75-250)
# elif(unit>150):
#     print("rupees per unit:", unit*1.50-180-1000-250)
# else:
#     print("invalid unit")



# no return without arument
#
        
        
# no return with argument  
# def perfect_number(a):
#     ans = 0
#     for i in range(1,int(num**0)+1):
#         if num%i==0:
#             ans+=i
#     if ans==num:
#         print("perfect number")
#     else:
#         print("no a perfect number")
        
# num = int(input("enter a number:"))        
# perfect_number(num) 


# positional argument

# def student_data(name,rollno):
#     print(f"The student name is {name} and the roll number is {rollno}")

# student_data("jatin",101)


# keword argument
# def student_data(name,rollno):
#     print(f"The student name is {name} and the roll number is {rollno}")

# student_data(rollno = 101,name="jatin")

#implement a grading systembased on user input marks
marks = int(input("enter a marks: "))
if(marks>=80 and marks<=100):
    print("A")
elif(marks>=60 and marks<80):
    print("B") 
elif(marks>=40 and marks<60):
    print("C")
elif(marks>=0 and marks<40):
    print("D")
else:
    print("E")
    
# check if a number is even or odd usingan if-else statement
num = int(input("enter a number:"))
if(num%2==0):
    print(num, ": is even")
else:
    print(num , ": is odd")  
    
#write a program to find the largest of three numbers
num1 = 34
num2 = 45
num3 = 24
if (num1>num2 and num2>num3):
    print(num1, ": is largest")
elif(num2>num3 and num2>num1):
    print(num2 , ":is largest")
else:
    print(num3, ":is largest") 

#implement  a program to check if a year is a leap year
year = int(input("enter a year"))
if(year%400==0) or (year%4==0 and year%100!=0):
    print(year, ":is a leap year")
else:
    print(year, ":is not a leap year") 
    
#write a program to  determine the eligibility to vote based on age
age = int(input("enter a age:"))
if(age>=18):
    print("eligible for vote")
else:
    print("not eligible for vote")

# create a program to check if a character is vowel or consonent
char = input("enter a character")
if char in "aeiouAEIOU": 
    print(char , ":is vowel") 
else:
    print(char , ":is consonent")                   
    
              
s="suraj"
print("z" in s)
                   
 
                
        
         

 
                       
       
    

    
               
        
          