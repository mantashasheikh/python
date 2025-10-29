# string


# # count the number of character in the string/length of string
# s = input("enter a string : ")
# count = 0
# for _ in s:
#     count = count+1
# print(count) 



#length of integer
# num = int(input("enter a number : "))
# count = 0 
# while num>0:
#     last_digit = num%10
#     count+=1
#     num//=10
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
# s = input("enter a string :")
# print(s[::-1])

# s = "neeraj"
# reverse_s = ""
# for i in range(len(s)-1,-1,-1):
#     reverse_s = reverse_s+s[i]
# print(reverse_s)

# s = "This is python class"
# s1=''
# for i in range(len(s)-1,-1,-1):
#     s1 = ''.join((s1,s[i]))
# print(s1)




# reverse a number /integer
# num = int(input("enter a number : "))
# rev = 0
# while num>0:
#     last_digit = num%10
#     rev = rev*10+last_digit
#     num//=10
# print(rev) 


   


# # check the given string is palindrome or not
# s = input("enter a string : ")
# if(s==s[::-1]):
#     print("palindrome")
# else:
#     print("not a palindrome")    

# s1 = input("enter a string : ")
# reverse = ""
# for i in range(len(s1)-1,-1,-1):
#     reverse = reverse + s1[i]
# if(s1 == reverse):
#     print("palindrome")
# else:
#     print("not a palindrome")




# convert the string into lower case
# s = input("enter a string : ")
# result = ''
# for ch in s:
#     if 'A' <= ch <= 'Z':
#         result += chr(ord(ch) + 32)
#     else:
#         result += ch
# print(result)  



# convert the string into upper case
# s = input("enter a string : ")
# result = ''
# for ch in s:
#     if 'a' <= ch <= 'z':
#         result += chr(ord(ch) - 32)
#     else:
#         result += ch
# print(result)



# remove spaces from the string
# s = input("enter a string : ")
# result = ''
# for ch in s:
#     if ch != ' ':
#         result += ch
# print(result)



# count the word from the given string
# s = "This is python class."
# count = 0
# in_word = False
# for ch in s:
#     if ch != ' ' and not in_word:
#         count += 1
#         in_word = True
#     elif ch == ' ':
#          in_word = False
# print(count)      





# replace character from the string
# s = input("enter a string : ")
# old_chr = 'a'
# new_chr = "x"
# result = ''
# for ch in s:
#     if ch == old_chr :
#         result += new_chr
#     else:
#         result += ch
# print(result)




# find substring from the given string
# s = "neeraj sir"
# s1 = "raj"
# if s1 in s:
#    print(s1, " is the substring of the given string")
# else:
#     print(s1, " is not a substring of the given string")   



# remove vowel from the String
# s = input("enter a string : ")
# result = ''
# vowel ="aeiouAEIOU"
# for ch  in s:
#     if ch not in vowel:
#         result+=ch
# print(result)



# count the unique character in string
# s = input("enter a string : ")
# unique = " "
# count = 0 
# for i in range(0,len(s)):
#     if s[i] not in unique:
#         unique+=s[i]
#         count+=1
# print(unique)
# print(count, " character are unique") 

# s = input("enter a string:")
# result = ''
# for ch in s:
#     exists = False
#     for r in result:
#         if ch == r:
#             exists = True
#             break
#         if not exists:
#             result += ch
# print(result)    
       
    

# find out the frequency of each character in string
# s =  input("enter a string : ")
# freq = {}
# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# print(freq) 



# capitalized the first letter of the string
# s = input("enter a string : ")
# first_ch = s[0]
# ascii_val = ord(first_ch)
# if(ascii_val >= 97 and ascii_val<=122):
#     capital_ch = chr(ascii_val-32)
# else:
#     capital_ch = first_ch
# capitalized = capital_ch
# i=1
# while i<len(s):
#     capitalized+=s[i]
#     i+=1
# print(capitalized)  


        