# # count the number of character in the string
# s = "neeraj"
# count = 0
# for _ in s:
#     count = count+1
# print(count)  

# # count the particular character in the string(let count 'e' from the string)
# s = "neeraj"
# count = 0
# target = 'e'
# for _ in s:
#     if _==target:
#         count=count+1
# print(count) 

# # reverse a string
# s = "neeraj"
# reverse_s = " "
# for i in range(len(s)-1,-1,-1):
#     reverse_s = reverse_s+s[i]
# print(reverse_s) 


# # check the given string is palindrome or not
# s1 = "pop"
# reverse = " "
# for i in range(len(s1)-1,-1,-1):
#     reverse = reverse + s1[i]
# if(s1 == reverse):
#     print("palindrome")
# else:
#     print("not a palindrome")
    
    
# num = int(input("enter a number:"))
# count = 0
# while num>0:
#     last_digit = num%10
#     count+=1
#     num//=10 
# print(count)  

num = 1234
rev = 0
while num>0:
    last_digit = num%10
    rev = rev*10+last_digit
    num//=10
print(rev)         
        
   













