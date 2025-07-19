# reverse a string
string = "mantasha"
string2 = ""
for char in range(len(string)-1,-1,-1):
     print(string[char],char)
    
s = "hello"
reversed_s = ""
for char in s:
   reversed_s = char + reversed_s
print(reversed_s)


s = "azeem"
rev = "".join(reversed(s))
print(rev)


# check the string is palindrome or not
# text = input("enter a text:")
# text2 = text[::-1]
# if(text == text2):
#     print("it is a palindrome")
# else:
#     print("it is not a palindrome") 

    
# count vowel in a string
text3 = "esha barkhane"
count = 0
for char in range(0,len(text3),1):
    if (text3[char]) in "aeiou":
        count+=1
print(count)   

# remove all spaces from a string
text4 = "i am a girl"
no_space = text4.replace(" ","")
print(no_space)


# s = "H e l l o   W o r l d"
# no_spaces = ''.join(s.split())
# print(no_spaces)


# convert the string to uppercase and lowercase
text5 = "Bhopal"
print(text5.upper())
print(text5.lower())


# find the length of the string without using len() function
# text6 = "I live in bhopal"
# count = 0
# for i in text6:
#   count+=1
# print("the length of the string is:",count)

# replace all occurence of the substring
text7 = "mat cat"
x = text7.replace("t","p")
print(x)

# remove duplicate characters in the string


    
    
 
    
    
    

    
           


