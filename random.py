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



# num = int(input("enter a number : "))
# rev = 0
# while num>0:
#     digit = num%10
#     rev = rev*10+digit
#     num = num/10
# print(rev)    
    

# string = input("enter a string : ")
# rev = string[::-1]
# if string==rev:
#     print("palindrome")
# else:
#     print("not a palindrome") 

# num = int(input("enter a number : "))

# if num%2==0:
#     print(num+num)
    
    
# name = input("enter a string :")
# print(name)   



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
    
    
    
    
# s = "this is the python class"
# print(s.lower())
# print(s.upper())
# print(s.capitalize())
# print(s.title())
# print(s.index("p"))
# print(s.count("s"))
# print(s.find("P"))


# l = ['1','2','3','4','5','6']
# s = ""
# for i in range(len(l)):
#    s = "".join((s,l[i]))
# print(s) 



# l = [1,7,6,5,4,2,3]
# for i in range(len(l)):
#     if i>5:
#         print(i)
         
# l = [1,7,6,5,4,2,3]
# print(max(l))


# name = "mantasha"
# print(name)

# age = int(input("enter your age : "))
# print(age)
# print(age/2)

# s1 = input("enter a string 1 : ")
# s2 = input("enter a string 2 : ")
# print(s1 + s2)
  
Class = "3rd"

print(Class)

t = (2,3,4,59,7,6)
print(max(t))

p = "this is para"
print(p)


N = 2345
count = 0
while N>0:
    mod = N%10
    count+=1
    N = N//10
print("count:",count)


N = 123
sum = 0
while N>0:
    mod = N%10
    sum = sum+mod
    N =N//10
print(sum) 

N = 1221
ans = N
rev = 0
while N>0:
    mod = N%10
    rev = rev*10+mod
    N =N//10
if rev==ans:
    print("it is a palindrome")
else:
    print("It is not a palindrome")
    
    
    
num = int(input("enter a number:"))
for num in range(1,num+1):
    if num>1:
        for j in range(2,num):
            if num%j==0:
                break
            else:
                print(num)     


a = int(input("enter a number:"))
b = int(input("enter a number:"))
max = 0
if(a>b):
    max = a
else:
    max = b
c = max    
while True:
    if(max%a==0 and max%b==0):
        break
    max += c
print(max) 


n1 = int(input("enter a number:"))
n2 = int(input("enter a number:"))
for i in range(1,n1+1):
    for j in range(1,n2+1):
        if(n1%i==0 and n2%i==0):
            hcf=i
            break
print(hcf)


base = int(input("enter a number:"))
power = int(input("enter a number"))
for i in range(1, base+1):
    ans=base**power
print(ans)                

s =  "12345"
l = []
for i in range(len(s)):
    l.append(s[i])
print(l)                

s = "My Name Is Mantasha Sheikh. I Live In Bhopal MP . I Am 21 Years Old"
result = ""
for ch in range(len(s)):
    if 'a'<= s[ch] <='z':
        result += chr(ord(s[ch])-32)
    elif 'A'<= s[ch] <='Z':
        result += chr(ord(s[ch])+32) 
    else:
        result += s[ch]     
print(result) 


n = int(input("enter a number:"))
i = 1
while i<=n:
    print("*"*n)
    i = i+1
    
class Student:
    school_code  = 101
    def __init__(self,name):
        self.n = name
        
    @classmethod
    def update_code(cls,new_code):
        cls.school_code = new_code
        cls.city = "bhopal"
obj = Student("neeraj")
print(obj.school_code)    
obj.update_code(102)
print(obj.school_code)
obj2 = Student("Rahul")
print(obj2.school_code)
print(obj.city)
print(obj2.city)



t = (2,4,5,7,"a","b","c")
count = 0
for i in range(len(t)):
    count+=1
print(count)
class Parent:
    def home(self):
        print("home from parent class")
    
    def car(self):
        print("car from parent class") 
        
class Child(Parent):
    pass
obj = Child()
obj.home()
obj.car()


t = (2,4,2,5,2,"a","b","c","a")
target = 2
count = 0
for i in t:
    if target == i:
        count+=1
print(count)

t = ( 2, 5, 6.8, 7.5, 7, 2.5, 55, 15)
max = 0
for i in range(0,len(t)) :
    if t[i]>max:
        max = t[i]
print("the maximum number in the tuple : ",max)

t = ( 2, 5, 6.8, 7.5, 7, 2.5, 55, 15)
min = 9
for i in range(0,len(t)) :
    if t[i]<min:
        min = t[i]
print("the minimum number in the tuple : ",min)