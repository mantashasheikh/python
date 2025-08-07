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




# list


# find the length of the list
# l = [1, 2.5, 'mantasha', 4.5+3j, 'rimsha'] 
# count = 0
# for i in l:
#     count+=1
# print(count) 



# find the sum of each element of the list
# l = [1, 3, 5, 2.6, 7.8]
# sum = 0
# for i in l:
#     sum+=i
# print(sum)




# find the maximum element element from the list
# l = [2, 5, 6.8, 7.5, 7, 2.5, 55, 154235]
# max = 0
# for i in range(0,len(l)) :
#     if l[i]>max:
#         max = l[i]
# print("the maximum number in the list : ",max)




# find the minimum number from the list
# l = [2, 5, 6.8, 7.5, 7, 2.5,1.5,]
# min = 9
# for i in range(0,len(l)) :
#     if l[i]<min:
#         min = l[i]
# print("the minimum number in the list : ",min)




# count  how many times the particular element occur in the list
# l =  ['a','b','a', 2 , 4 , 2 , 2 ,'a']
# count = 0
# char = 'a'
# for i in range(0,len(l)):
#     if l[i]==char:
#         count+=1
# print(count) 



# reverse a list
# l =  [1,2,3,4,5]
# print(l[::-1])

# l = [1,2,3,4,5]            
# rev = []
# for i in range(len(l)-1,-1,-1):
#     x = l[i]
#     rev.append(x)
# print(rev)



# check the given list is palindrome or not
# l =  [1,0,1]
# rev = (l[::-1])
# if l==rev:
#     print("palindrome")
# else:
#     print("not a palindrome") 




# remove duplicate value from the list
# l = ['a','b','a',2,5,2,6,'a']
# unique = []
# count = 0 
# for i in range(0,len(l)):
#     if l[i] not in unique:
#         unique.append(l[i])
#         count+=1
# print(unique)
# print(count, " character are unique")
   


# sort the list
# l = [2,1,5,4,7,6,3] 
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i] > l[j]:
#             l[i],l[j] = l[j],l[i]
# print(l)  



# merge two list
# l1 = ['mantasha','kumkum']
# l2 = [1,2,3] 
# for i in range(0,len(l2)):
#     l1.append(l2[i])
# print(l1)    
    
# l1.append(l2)
# print(l1)



# find the second maximum element from the list
# l = [1,4,3,7,2,5]
# max = l[0]
# for i in l:
#     if i>max:
#         max = i
        
# l = [2,1,5,4,7,6,3] 
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i] > l[j]:
#             l[i],l[j] = l[j],l[i]
# sec_max = 0
# for m in range(len(l)-1):
#     sec_max = l[m]
# print(sec_max) 



# find the common element from the lists
# l1 = [1,2,3,4,5]
# l2 = [7,6,5,4,3]
# common =  []
# for i in l1:
#     for j in l2:
#         if i==j:
#             common.append(i)
# print(common, " these are the common elements of both list") 




# split even and odd element from the list
# l = [1,2,3,4,5,6,7]
# even = []
# odd = []
# for i in l:
#      if i % 2 == 0:
#          even.append(i)
#      else:
#          odd.append(i)
# print("list of even element : ",even)
# print("list of odd element : ",odd) 




# convert the list into string
# l = ['1','2','3','4','5','6']
# s = ""
# for i in range(len(l)):
#    s = "".join((s,l[i]))
# print(s)  




# convert the string into list
# s =  "12345"
# l = []
# for i in range(len(s)):
#     l.append(s[i])
# print(l)   




# alternate case convert upperCase into lowerCase and lowerCase into upperCase
# s = "My Name Is Mantasha Sheikh. I Live In Bhopal MP . I Am 21 Years Old"
# result = ""
# for ch in range(len(s)):
#     if 'a'<= s[ch] <='z':
#         result += chr(ord(s[ch])-32)
#     elif 'A'<= s[ch] <='Z':
#         result += chr(ord(s[ch])+32) 
#     else:
#         result += s[ch]     
# print(result) 




# reverse each word of the string







# tuples

# print  length of tuple
# t = (2,4,5,7,"a","b","c")
# count = 0
# for i in range(len(t)):
#     count+=1
# print(count)



# find  the occurrence of the particular element 
# t = (2,4,2,5,2,"a","b","c","a")
# target = 2
# count = 0
# for i in t:
#     if target == i:
#         count+=1
# print(count)



# find the maximum element from tuple
# t = ( 2, 5, 6.8, 7.5, 7, 2.5, 55, 15)
# max = 0
# for i in range(0,len(t)) :
#     if t[i]>max:
#         max = t[i]
# print("the maximum number in the tuple : ",max)




# find the minimum element from the tuple
# t = ( 2, 5, 6.8, 7.5, 7, 2.5, 55, 15)
# min = 9
# for i in range(0,len(t)) :
#     if t[i]<min:
#         min = t[i]
# print("the minimum number in the tuple : ",min)



# sum of tuple elements 
# t = (2,4.5,7,8.8,5)
# sum = 0
# for i in t:
#     sum+=i
# print(sum)




# index of element
# t = (2,4,6,"a","b","c")
# value = input("enter a value : ")      #error
# index = 0
# for item in t:
#     if item == value:
#         print(index)
#     index+=1  




    






        
        
        
    

            
        
    




  
    
            
 
     



           
            
            







        
       
        








  












    

        
    
    
   




    
    
    


 


  







 
    
    
        
        
   













