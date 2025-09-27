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
n = int(input("enter a number : "))
temp = n
ans = 0
x = len(str(n))
while n>0:
    digit = n%10
    ans+=digit**x
    n//=10
if ans==temp:
    print("armstrong")
else:
    print("not an armstrong")
    
    


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
num1 = int(input("enter a number : "))
num2 = int(input("enter a number : "))
lcm = 0
max = 0
if num1>num2:
    max = num1
else:
    max = num2
if max%num1==0 and max%num2==0:
    lcm = max
    print(lcm)    
            
    
 
     




      
        
        
    
 
 
                  

            
        
        
    