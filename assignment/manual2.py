# find the factor of any number
# n=int(input("enter a number : "))
# factor = []
# for i in range(1,n+1):
#     if n%i==0:
#         factor.append(i)
# print(factor)  



# wap to arrange all items from list in assending order.
# l = eval(input("enter a list : "))
# for i in range(0,len(l)):
#     for j in range(0,len(l)):
#         if l[j]>l[i]:
#             l[i],l[j]=l[j],l[i]
# print(l)            
       


#  WAP to arrenge all items from list in desending order. 
# l = eval(input("enter a list : "))
# for i in range(0,len(l)):
#     for j in range(0,len(l)):
#         if l[j]<l[i]:
#             l[i],l[j]=l[j],l[i]
# print(l) 



 
# WAP to find maximum digit in given list.
# l = eval(input("enter a list : "))
# max = 0
# for i in l:
#     if i>max:
#         max=i
# print(max)  



# WAP to find maximum digit in given list.
# l = eval(input("enter a list : "))
# min = 9
# for i in l:
#     if i<min:
#         min=i
# print(min) 



# check the number is perfect or not
# n = int(input("enter a number : ")) 
# sum = 0 
# for i in range(1,n): 
#     if n%i==0: 
#         sum=sum+i 
# if n==sum: 
#     print(f'given number {n} is perfect number') 
# else: 
#     print(f'given number {n} is not a perfect number') 
    
    

   
# WAP to arrenge all even and odd no at a place. 
# l = [2,1,3,8,4,8,5]  
# l1=[] 
# for i in l: 
#     if i %2==0: 
#         l1.append(i) 
# for i in l: 
#     if i%2 !=0: 
#         l1.append(i) 
# print(l1)  



 
# WAP to arrenge all zeroes at the end. 
# l = [2,0,3,0,1,0,5]  
# l1=[] 
# for i in l: 
#     if i !=0: 
#         l1.append(i) 
# n = len(l)-len(l1)  
# for i in range(n): 
#     l1.append(0) 
# print(l1)



# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5
# n = int(input("Enter any no :")) 
# for i in range(1,n+1): 
#     for j in range(1,n+1): 
#         print(j,end=' ') 
#     print()

    
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5 
# n= int(input("Enter any no :")) 
# for i in range(1,n+1): 
#     for j in range(1,i+1): 
#         print(j,end=' ')
#     print()  
    
    
    
# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E 
# n= int(input("Enter any no :")) 
# for i in range(1,n+1): 
#     ch='A' 
#     for j in range(1,n+1): 
#         print(ch,end=' ') 
#         ch=chr(ord(ch)+1) 
#     print()
    
      
    
   
# A
# A B
# A B C
# A B C D
# A B C D E 
# n= int(input("Enter any no :")) 
# for i in range(1,n+1): 
#     ch = 'A' 
#     for j in range(1,i+1): 
#         print(ch,end=' ') 
#         ch=chr(ord(ch)+1) 
#     print()                 
   
   
   
   
#  
# 2  
# 2 4 
# 2 4 6 
# 2 4 6 8 
# 2 4 6 8 10 
# n = int(input("Enter any no :")) 
# for i in range(1,n+1):  
#     for j in range(1,i+1):  
#         print(2*j,end=" ") 
#     print()    
    
    
    
# 1 
# 1 3 
# 1 3 5 
# 1 3 5 7 
# 1 3 5 7 9 
# n = int(input("Enter any no :")) 
# for i in range(1,n+1):  
#     for j in range(1,i+1):  
#         print(2*j-1,end=" ") 
#     print() 
    
    
    
# 10  
# 10 8 
# 10 8 6 
# 10 8 6 4 
# 10 8 6 4 2 
# code for above output 
# k=[] 
# for i in range(10,1,-2): 
#     k.append(i) 
#     for j in k: 
#         print(j,end=" ") 
#     print() 
    
    
    
# * 
# ** 
# *** 
# **** 
# ***** 
# n=int(input("Enter the number of rows: "))  
# for i in range(1,n+1):  
#     print("*"*i)  
    
    
    
# *  
# * * 
# * * * 
# * * * * 
# * * * * * 
# n=int(input("Enter the number of rows: "))  
# for i in range(1,n+1):  
#     print("* "*i)
    
    

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# n=int(input("Enter the number of rows: "))  
# for i in range(1,n+1):  
#     print(" "*(n-i),"*"*i) 
    
  
  
#      * 
#     *** 
#    ***** 
#   ******* 
#  ********* 
# n=int(input("Enter the number of rows: ")) 
# for i in range(1,n+1): 
#     print(" "*(n-i),"*"*(2*i-1))  


#       * 
#      * * 
#     * * * 
#    * * * * 
#   * * * * * 
# n=int(input("Enter the number of rows: "))  
# for i in range(1,n+1):  
#     print(" "*(n-i)," *"*i)  
    
    
    

#  ***** 
#   **** 
#    *** 
#     ** 
#      * 
# n=int(input("Enter the number of rows: "))  
# for i in range(n,0,-1):  
#     print(" "*(n-i),"*"*i)
    
    
    
# *****  
# **** 
# *** 
# ** 
# * 
# n=int(input("Enter the number of rows: "))  
# for i in range(n,0,-1):  
#     print("*"*i) 
    
    
    
    
#   * * * * * 
#    * * * * 
#     * * * 
#      * * 
#       * 
# n=int(input("Enter the number of rows: "))  
# for i in range(n,0,-1):  
#     print(" "*(n-i)," *"*i)                
    
    
    

#       * 
#      * * 
#     * * * 
#    * * * * 
#   * * * * * 
#    * * * * 
#     * * * 
#      * * 
#       * 
# n=int(input("Enter the number of rows: ")) 
# for i in range(1,n+1):  
#     print(" "*(n-i),"* "*i)  
# m=n-1 
# for i in range(m,0,-1):  
#     print(" "*(m-i)," *"*i) 


    
    
#      *
#     ** 
#    *** 
#   ****
#  ***** 
# ***** 
# **** 
# *** 
# ** 
# * 
# n=int(input("Enter the number of rows: "))  
# for i in range(0,n+1):  
#     print(" "*(n-i),"*"*i) 
# for i in range(n,0,-1):  
#     print("*"*i," "*(n-i))
    
    
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
# n=int(input("Enter the number of rows: "))  
# for i in range(0,n+1):  
#     print("* "*i) 
# m=n-1 
# for i in range(m,0,-1):  
#     print("* "*i) 




# write a program to check given number is positive
# n=int(input("enter a number : "))
# if(n>0):
#     print(f"{n} :this number is positive")
    
    
    
# write a program to check the given number is positive or negative
# n=int(input("enter a number : "))
# if(n>0):
#     print(f"{n} :is positive")
# else:
#     print(f"{n} :is negative") 
    
    

# write a program to check the given number is positive , negative or zero
# n=int(input("enter a number : "))
# if(n>0):
#     print(f"{n} :is positive")
# elif(n<0):
#     print(f"{n} :is negative")
# else:
#     print(f"{n} : is zero")   
    
    

# write a program to swap two variable without using third variable
# a = 4
# b = 6
# a,b = b,a 
# print("a : ",a)
# print("b : ",b)


# write a prohram to swap two variables using third variable
# a = 8
# b = 9
# c = 0
# c = b
# b = a
# a = c
# print("a : ",a)
# print("b : ",b)



# write a program to swap two variable s using addition and subtraction



    
# Write a program to find largest no among the three inputs numbers. 
# n1 = int(input("enter first number : "))
# n2 = int(input("enter second number :"))
# n3 = int(input("enter third number :"))
# if n1>n2 and n1>n3:
#     print(n1, " : is greater")
# elif n2>n1 and n2>n3:
#     print(n2, " : is greater")
# else:
#     print(n3, " : is greater")
    
    
    
# Write a program to find area of  triangle. (1/2* hight*base)
# height = int(input("enter a height : "))
# base = int(input("enter a base : "))
# area = 1/2*(height*base)
# print(area)



# Write a program to find area of square. 
# side =  int(input("enter a number : "))
# area = side*side
# print(area) 




# Write a program to find given year is leep year or not. 
# year = int(input("enter a number :"))
# if year%4==0 or year%400==0:
#     print(year , " : is a leap year")
# else:
#     print(year , " : is not a leap year")
    
    
    
# Write a program to display n natural numbers. 
# n = int(input("enter a number : "))
# i=1
# while i<=n:
#     print(i,end=" ")
#     i+=1 

    
    
# Write a program to calculate the sum of numbers. 
# l = [2,3,4,5,6]
# i = 0
# sum = 0
# while i in range(len(l)):
#     sum+=l[i]
#     i+=1
# print(sum)
    
    

# Write a program to find even no. (2,4,6,8,….) 
# n = int(input("enter a number : "))
# i = 1
# while i<=n:
#     if i%2==0:
#         print(i)
#     i+=1
    

# Write a program find odd no.(1,3,5,7,9,……)     
# n = int(input("enter a number : "))
# i = 1
# while i<=n:
#     if i%2!=0:
#         print(i)
#     i+=1  
    
    

# Write a program to find factorial of given no. 
# n = int(input("enter a number : "))
# i = 1
# fact = 1
# while i<=n:
#     fact*=i
#     i+=1
# print(fact)



# Write a program to print your names ten times.  
# n = int(input("enter a number : "))
# i = 1
# while i<=n:
#     print("mantasha")
#     i+=1  



#  Write a program to find how many vowels and consonants are present in string
# name = input("enter a string : ")
# vowel = 0
# consonent = 0
# i = 0
# while i in range(len(name)):
#     if name[i] in "aeiouAEIOU":
#         vowel+=1
#     else:
#         consonent+=1
#     i+=1  
# print(vowel)
# print(consonent)



# Write a program to add 5 in each elements in given list.
# l = [10,20,30,40,50]
# i = 0
# while i in range(len(l)):
#     l[i]+=5
#     i+=1
# print(l) 



# Write a program to add 5 in each elements in given tuple.
# t = (10,20,30,40,50)
# i=0
# while i in range(len(t)): #error
#     t[i]+=5
#     i+=1
# print(t)




#  Write a program to create a list from given string. 
s = input("enter a string : ")
l = []
i=0
while i in range(len(s)) :
    l.append(s[i])
    i+=1
print(l)
    



                 
    
              
    
   
             
    
    
    
                           
    
    
    
                
       