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
 
    
    
# write a program to count the total number of notes in the given amount
# Input the amount
amount = int(input("Enter the amount: Rs"))

print("Calculating notes for amount: Rs",amount)
total_notes = 0

if amount >= 500:
    n500 = amount // 500
    print("Rs500 notes:", n500)
    total_notes += n500
    amount = amount % 500

if amount >= 200:
    n200 = amount // 200
    print("Rs200 notes:", n200)
    total_notes += n200
    amount = amount % 200

if amount >= 100:
    n100 = amount // 100
    print("Rs100 notes:", n100)
    total_notes += n100
    amount = amount % 100

if amount >= 50:
    n50 = amount // 50
    print("Rs50 notes:", n50)
    total_notes += n50
    amount = amount % 50

if amount >= 20:
    n20 = amount // 20
    print("₹20 notes:", n20)
    total_notes += n20
    amount = amount % 20

if amount >= 10:
    n10 = amount // 10
    print("Rs10 notes:", n10)
    total_notes += n10
    amount = amount % 10

if amount >= 5:
    n5 = amount // 5
    print("Rs5 notes:", n5)
    total_notes += n5
    amount = amount % 5

if amount >= 2:
    n2 = amount // 2
    print("Rs2 notes:", n2)
    total_notes += n2
    amount = amount % 2

if amount >= 1:
    n1 = amount
    print("Rs1 notes:", n1)
    total_notes += n1

print("Total number of notes:", total_notes)

 
                       
       
    

    
               
        
          