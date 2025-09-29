# natural number
# n = int(input("enter a number : "))
# for i in range(1,n+1):
#     print(i , end=" ")

# even number
# n = int(input("enter a number : ")) 
# for i in range(n+1):
#     if i%2==0:
#         print(i)
        
        
        
# odd number
# n = int(input("enter a number : "))
# for i in range(n+1):
#     if i%2!=0:
#         print(i) 

        
 
# prime number
# n = int(input("enter a number :")) 
# print(f"Prime numbers up to {n}:")
# for num in range(2, n+1):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:   
#         print(num, end=" ") 




# factor of a given number
# n = int(input("enter a number : "))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i, end=" ")
        



# factorial
# n = int(input("enter a number : "))
# fact = 1
# for i in range(1,n+1):
#     fact*=i
#     print(fact)
    
    
    
# leap year
# year = int(input("enter a number : "))
# if (year%4==0 and year%100!=0)or(year%400==0):
#     print("Leap year")
# else:
#     print("not a leap year")
    




#   armstrong
# n = int(input("enter a number : "))
# temp = n
# ans = 0
# x = len(str(n))
# while n>0:
#     digit = n%10
#     ans+=digit**x
#     n//=10
# if ans==temp:
#     print("armstrong")
# else:
#     print("not an armstrong")
    
    


# palindrome
# n = int(input("enter a number"))
# original = n
# rev = 0
# while n>0:
#     digit = n%10
#     rev+=digit
#     n//=10
# if rev==original:
#     print("palindrome")
# else:
#     print("not a palindrome")
    


# lcm






# fibonacci
# n = int(input("enter a number : "))
# first = 0
# second = 1
# print(first)
# print(second)
# for i in range(2,n+1):
#     next = first + second
#     first = second
#     second = next
#     print(next)




# Harshad  number
# n = int(input("enter a number : "))
# temp = n
# sum = 0
# while n>0:
#     digit = n%10
#     sum+=digit
#     n//=10
# if temp%sum==0:
#     print("harshad")
# else:
#     print("not a harshad") 
    
    
    

# anagram
# s1 = input("enter a string :")
# s2 = input("enter a string : ")
# l1 = sorted(s1)
# l2 = sorted(s2)
# if l1==l2:
#     print("anagram")
# else:
#     print("not a anagram")
    
    
    


# Neon
# n = int(input("enter a number : "))
# temp = n
# mul = n * n
# sum = 0
# while mul>0:
#     digit = mul%10
#     sum+=digit
#     mul//=10
# if sum == temp:
#     print("neon number")
# else:
#     print("not a neon number") 
    
    
    

# peterson
# n = int(input("enter a number : "))
# temp = n
# sum = 0
# while n>0:
#     digit = n%10
#     fact = 1
#     for i in range(1,digit+1):
#        fact*=i
#     sum+=fact
#     n//=10
# if sum==temp:
#     print("peterson") 
# else:
#     print("not a peterson") 



    
    


# spy number
# n = int(input("enter a number : "))
# temp = n
# sum = 0
# mul = 1

# while n>0:
#     digit = n%10
#     sum+=digit
#     mul*=digit
# if sum==mul:
#     print("spy number")
# else:
#     print("not a spy")  





# sunny number 
    
    
    
# l =  [2,4,0,6,0,7,0,2,4] 
# l1 = []
# l2 = []
# for i in l:
#     if i!=0:
#         l1.append(i)
#     else:
#         l2.append(i)
# for j in l2:
#     l1.append(j)              
# print(l1)  




# l = [2,3,4,5,6,7,8,9]
# l1 = []
# l2 = []
# for i in l:
#     if i%2==0:
#         l1.append(i)
#     else:
#         l2.append(i)
# for j in l2:
#     l1.append(j)
# print(l1)



# l = [2,4,5,9,7,8,6]
# max = 0
# for i in l:
#     if i > max:
#         max = i
# print(max)  


 

numbers = [5, 3, 8, 1, 2]

# Bubble sort using swap
for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            # swap
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Ascending order:", numbers)           
            




      
        
        
   
        
          
                         
    
    
    

   
    
    

              
    
 

    
    
    

   
            




 
     




      
        
        
    
 
 
                  

            
        
        
    