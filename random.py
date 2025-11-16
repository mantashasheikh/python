# n = int(input("enter a number : "))
# if(n%2==0):
#     print("even")
# else:
#     print("odd")    
    
# num1 = 2
# num2 = 3
# print(num1 + num2) 

# n1 = int(input("enter a number1 : "))
# n2 = int(input("enter a number2 : "))
# print(n1 - n2)
# print(n1 * n2)   
# print(n1 / n2)
# print(n1 % n2)

# s = input("enter a string : ")
# print(s[::-1])



num = int(input("enter a number : "))
rev = 0
while num>0:
    digit = num%10
    rev = rev*10+digit
    num = num/10
print(rev)    
    

string = input("enter a string : ")
rev = string[::-1]
if string==rev:
    print("palindrome")
else:
    print("not a palindrome") 

num = int(input("enter a number : "))

if num%2==0:
    print(num+num)
    
    
name = input("enter a string :")
print(name)   



N = 4
first = 0
second = 1
next = 0
print(first) 
print(second)
for i in range(1,n+1):
    next = first + second
    first = second
    second = next
    print(next)        