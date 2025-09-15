# def Factors(n):
#     factors = [] 
#     for i in range(1,n+1): 
#         if n%i==0: 
#             factors.append(i) 
#     return factors
# num = int(input("enter a number : "))
# ans = Factors(num)
# print(ans)



# def Sort(l):
#     for i in range(len(l)-1): 
#         for j in range(len(l)-i-1): 
#             if l[j] > l[j+1]: 
#                 l[j], l[j+1] = l[j+1], l[j] 
#     return l            
# list = [64, 34, 25, 12, 22, 11, 90, 5] 
# sort = Sort(list)            
# print(sort)




 
# def Descending(l):
#     n = len(l) 
#     for i in range(n-1): 
#         for j in range(n-i-1): 
#             if l[j] < l[j+1]: 
#                 l[j], l[j+1] = l[j+1], l[j]
#     return l             
# list = [64, 34, 25, 12, 22, 11, 90, 5] 
# sort = Descending(list)            
# print(sort)  



# def Max(l):
#     max = l[0] 
#     for i in range(len(l)-1): 
#         if l[i]>l[i+1]: 
#             max = l[i] 
#             l[i],l[i+1]=l[i+1],l[i]   
#         else: 
#             max=l[i+1] 
#     return max        
# list = [2,4,9,3,5]
# ans = Max(list)         
# print(ans) 





# def Min(l):
#     min = l[0] 
#     for i in range(len(l)-1): 
#         if l[i]<l[i+1]: 
#             min = l[i] 
#             l[i],l[i+1]=l[i+1],l[i]   
#         else: 
#             min=l[i+1] 
#     return min        
# list = [2,4,9,3,5]  
# ans = Min(list)      
# print(ans) 




# prime number
# def Prime(n):
#     count = 0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     return count    
   
# num = int(input("enter a number")) 
# ans = Prime(num) 
# if ans==2:
#     print("Prime number")
# else:
#     print("not a prime number")


# hcf
# num1 = int(input("enter a number : "))
# num2 = int(input("enter a number : "))
# if num1>num2:
#     max = num1
# else:
#     max = num2
# while(1):
#     if(max%num1==0 and max%num2==0):
#         break
#     max+=1

# print(max)     


# lcm
# num1 = int(input("enter a number : "))
# num2 = int(input("enter a number : "))
# if num1<num2:
#     min = num1
# else:
#     min= num2
# for i in range(1,min+1):
#     if(min%i==0 and min%i==0):
#         break


# print(min)  


# anagram
# s1 = "mantasha"
# s2 = "kumkum"
# for ch in s1:
#     pass
# if ch in s2:
#     print("anagram")
# else:
#     print("not anagram") 
    
    
# prime
# n = int(input("enter a number"))     
# count = 0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
       
# if count==2:
#     print("Prime number")
# else:
#     print("not a prime number")  


# factorial
n = int(input("enter a number : "))
fact = 1
for i in range(1,n+1):
    fact*=i
print(fa         
    
    
    
       
    
    
               
    
    
    
    
              
        




            









 

            
        
          
         
    

    
    
    