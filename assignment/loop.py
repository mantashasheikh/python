# #print first 10 natural numbers using a loop
# i = 1
# while i<=10:
#     print(i)
#     i+=1
    
# #write a program to calculate the factorial of a number using a for loop
# n = 5
# ans = 1
# for i in range(1,n+1):
#     ans = ans*i
#     print(ans)
    
# #implement a program to find the sum of first N natural numbers using a while loop
# N = 1
# sum = 0
# while N<=5:
#     sum= sum+N
#     N+=1
# print(sum)
    
# #implement a program to find the all number divisile by 3 and 5 within a range
# n = 50
# for i in range(1,n+1):
#     if i%3==0 and i%5==0:
#         print(i, ":is divisible by 3 and 5")

# #write a program to calculate the sum of squares of the N natural number
# N = 5
# sum = 0
# for n in range (1,N+1):
#     sum += n*n
# print(sum)

# #print the multiplication table  of a number
# N = 7
# for i in range(1,10+1):
#     mul = i*N
#     print(mul)
    
# #write a program to check if a number is a prime number
# N = 14
# count = 0
# for i in range(1,N+1):
#   if(N%i==0):
#       count+=1
# if(count==2):
#     print(N,":is prime number")
# else:
#     print(N, ":is not a prime number")
    
# #implement a program to reverse a number
# N = 12345 
# rev = 0
# while N>0:
#     mod = N%10
#     rev = rev*10+mod
#     N = N//10
# print(rev)

# #generate a fibonacci series up to a given term using loop
# N = 4
# first = 0
# second = 1
# next = 0
# print(first) 
# print(second)
# for i in range(1,n+1):
#     next = first + second
#     first = second
#     second = next
#     print(next)
    
# #implement a program to count the number of digits in a number
# N = 2345
# count = 0
# while N>0:
#     mod = N%10
#     count+=1
#     N = N//10
# print("count:",count)   

# #write a program to calculate the sum of digit of a number
# N = 123
# sum = 0
# while N>0:
#     mod = N%10
#     sum = sum+mod
#     N =N//10
# print(sum) 

# #check if a number is a palindrome  using loop
# N = 1221
# ans = N
# rev = 0
# while N>0:
#     mod = N%10
#     rev = rev*10+mod
#     N =N//10
# if rev==ans:
#     print("it is a palindrome")
# else:
#     print("It is not a palindrome") 
    
# #print  all prime number within a range
num = int(input("enter a number:"))
for num in range(1,num+1):
    if num>1:
        for j in range(2,num):
            if num%j==0:
                break
            else:
                print(num) 
            

# #write a program to print LCM of two number
# a = int(input("enter a number:"))
# b = int(input("enter a number:"))
# max = 0
# if(a>b):
#     max = a
# else:
#     max = b
# c = max    
# while True:
#     if(max%a==0 and max%b==0):
#         break
#     max += c
# print(max)       
        
# #write a program to print HCF of two numbers
# # n1 = int(input("enter a number:"))
# # n2 = int(input("enter a number:"))
# # for i in range(1,n1+1):
# #     for j in range(1,n2+1):
# #         if(n1%i==0 and n2%i==0):
# #             hcf=i
# #             break
# # print(hcf)

# #create a program to calculate the power of a number using loop
# # base = int(input("enter a number:"))
# # power = int(input("enter a number"))
# # for i in range(1, base+1):
# #     ans=base**power
# # print(ans)

# #print all armstrong number within a range
# num = int(input("enter a number:"))
# sum = 0
# ans = num
# for i in range(1,num+1):
#     digit = num%10
#     sum = sum+digit*digit*digit
#     num = num//10
# if(ans==sum):
#     print("armstrong")
# else:
#     print("not an armstrong") 
    
# another way to print armstrong number





#write  a pogram to find the sum of even and odd number separately in a range
# num = int(input("enter a number:"))
# sum1 = 0
# sum2 = 0
# for i in range(0,num+1):
#     if(i%2==0):
#         sum1 = sum1+i
#     else:
#         sum2 = sum2+i    
# print("sum of even number is:",sum1)
# print("sum of odd number is:",sum2)

#half pyramid  of
# for r in range(1,6):
#     for c in range(1,6):
#         if(c<=r):
            
        
        

    

        
        
    
        
        

        
    
    
    
    
    
       