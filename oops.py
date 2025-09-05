# internal constructor

# class New:
#     x = 10
#     y = 20
# obj = New
# print(id(New))
# print(id(obj)) 


# class new:
#     pass
# obj = new
# print(id(new))
# print(id(obj)) 


# class new:
#     "for demo purpose"
# obj = new
# print(id(new))
# print(id(obj))



# class New:
#     "for demo purpose"
# obj = New
# print(dir(New))
# print(New.__doc__)


# class New:
#     "for demo purpose"
# obj = New
# obj1 = New
# obj2 = New
# print(id(New))
# print(id(obj),id(obj1),id(obj2))



# external  constructor

# class Student:
#     def __init__(self):
#         print("external constructor called")
# x = Student
# print(id(x),id(Student))    #same address
# y = Student()
# print(id(y),id(Student))    #different address


# class Student:
#     def __init__(self):
#         print("external constructor called")
#         print(id(self))
# x = Student()
# print(id(x),id(Student))


# class Student:
#     def __init__(self,name,grade):
#         self.n = name
#         self.g = grade
#         print("obj self id : ", id(self))
        
#     def account(self):
#         print(self.n)
#         print(self.g)    
# obj =  Student("Neeraj","10th")
# obj.account()


# 4-9-2025

# class Student:
#     def __init__(self):
#         print("external")
# obj = Student()
# obj.__init__()  


# class Student:
#     def __init__(self):
#         print("external")
#     def __init__(self):
#         print("2")
#     def __init__(self):
#         print("3")        
# obj = Student()
# obj.__init__() 



# 5-9-2025


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
       






               


     



        
        








   