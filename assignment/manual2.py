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
    
    
    
                
       