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




# def upperCase(s):
#     result =""
#     for ch in s:
#         if 'a'<=ch <='z':
#             result += chr(ord(ch)-32)
#         else:
#             result += ch
#     return result
# n = input("enter a string : ")
# ans = upperCase(n)
# print(ans)


# # declaration of instance variable
# class Student:
#     def __init__(self,name,age ,roll):
#         self.n = name    #inside constructor  
#         self.a = age
#         self.r = roll
#     def addNew(self,contact):
#         self.c = contact    #inside instance method
#     def showDetail(self):
#         print(self.n,self.a,self.r,self.c,self.e)
# obj = Student("mantasha",37,1234)
# obj.addNew(123456789)      
# obj.e = "mantasha@gmail.com"    #outside the class
# obj.showDetail() 


# # calling of instance variable
# class Student:
#     def __init__(self,name,age ):
#         self.n = name
#         self.a = age
#         print(self.a,self.n)    #inside a constructor
       
#     def addNew(self,contact):
#         self.c = contact
#     def showDetail(self):
#         print(self.n,self.a,self.c,self.e)   #inside instance method
# obj = Student("mantasha",37,1234)
# obj.addNew(123456789)
# obj.e = "mantasha@gmail.com"
# obj.showDetail() 
# print(obj.n,obj.a,obj.c,obj.e)      #outside the class




# class Student:
#     def __init__(self,name):
#         self.n = name
        
#     def show(self):
#         print(self.n)    
# obj = Student("mantasha")
# obj.show()
# print(obj.n) 
       

# import keyword
# x = keyword.kwlist
# print(x)
# print(len(x))
# print(type(x))



# import keyword
# x = keyword.softkwlist
# print(x)
# print(len(x))
# print(type(x))


a = None
print(type(a))




               
        
            
        
          
         
    

    
    
    