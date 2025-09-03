# def string_length(s):
#     count=0
#     for _ in s:
#         count = count+1
#     return count
# n = input("enter a string:")
# result = string_length(n)  
# print(result) 


# def reverse(s):
#     return s[::-1]
# n = input("enter a string: ")
# result = reverse(n)
# print(result)


# def palindrome(s):
#     a = s
#     s[::-1]
#     if a==s:
#         return palindrome
#     else:
#         return palindrome



# def lowerCase(s):
#     result = ""
#     for ch in s:
#         if 'A'<= ch <='Z':
#             result += chr(ord(ch) + 32)
#         else:
#             result += ch  
#     return result
# n = input("enter a string : ")
# ans = lowerCase(n)
# print(ans)




def upperCase(s):
    result =""
    for ch in s:
        if 'a'<=ch <='z':
            result += chr(ord(ch)-32)
        else:
            result += ch
    return result
n = input("enter a string : ")
ans = upperCase(n)
print(ans)
            
        
          
         
    

    
    
    