# if -else

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
    
              
