# 9-9-2025

# single level inheritance

# class Parent:
#     def home(self):
#         print("home from parent class")
    
#     def car(self):
#         print("car from parent class") 
        
# class Child(Parent):
#     pass
# obj = Child()
# obj.home()
# obj.car()



# multi level inheritance 

# class GrandParent:
#     def name(self):
#         print("name from grandparent")

# class Parent(GrandParent):
#     def car(self):
#         print("car from parent")

# class Child(Parent):
#     pass

# obj = Child()
# obj.name()
# obj.car() 


# multiple inheritance  

# class Parent1:
#     def home(self):
#         print("from parent1")

# class Parent2:
#     def home(self):
#         print("from parent2") 
        
# class Child(Parent1,Parent2):
#     pass

# obj = Child()
# obj.home()


# method overriding

# class Parent:
#     def home(self):
#         print("from parent")

# class Child(Parent):
#     def home(self):
#         print("from child")
#         super().home()

# obj = Child()
# obj.home() 



# class Parent1:
#     def home(self):
#         print("from parent1")

# class Parent2:
#     def home(self):
#         print("from parent2") 
        
# class Child(Parent1,Parent2):
#     def home(self):
#         print("from child")
#         super().home()
# obj = Child()
# obj.home()



#heirarchical inheritence

# class Parent:
#     def home(self):
#         print("home from parent")
#     def car(self):
#         print("car from parent")
# class Child(Parent):
#     pass 
# class Child2(Parent):
#     pass

# obj = Child()
# obj.home()
# obj.car()
# obj2 = Child2()
# obj2.home()
# obj2.car() 




#
#hybrid inheritance

# class Parent:
#     def home(self):
#         print("home from parent")
#     def car(self):
#         print("car from parent")
# class Child1(Parent):
#     pass 
# class Child2(Parent):
#     pass
# class Child(Child1,Child2):
#     pass
# obj = Child()
# obj.home()
# obj.car()




# Abstraction

# from abc import ABC, abstractmethod    #error
# class first(ABC):
#     @abstractmethod   
#     def new(self):
#         pass
# class Child(first):
#     pass
# obj = Child() 



# from abc import ABC, abstractmethod   #error
# class Senior(ABC):
#     def add(self):
#         x = 2
#         y = 3
#         print(x+y)
    
#     def sub(self):
#         x = 3
#         y = 1
#         print(x-y)
#     @abstractmethod
#     def div(self):
#         pass

# class Junior(Senior):
#     def mult(self):
#         x = 8
#         y = 4
#         print(x*2)
    
#     def division(self):
#         x = 6
#         y = 3
#         print(x/y)
# obj = Junior() 





# from abc import ABC, abstractmethod 
# class Senior(ABC):
#     def add(self):
#         x = 2
#         y = 3
#         print(x+y)
    
#     def sub(self):
#         x = 3
#         y = 1
#         print(x-y)
#     @abstractmethod
#     def div(self):
#         pass

# class Junior(Senior):
#     def mult(self):
#         x = 8
#         y = 4
#         print(x*2)
    
#     def div(self):
#         x = 6
#         y = 3
#         print(x/y)
# obj = Junior() 
# obj.add()
# obj.div()   





# encapsulation


#public variable
# class Parent:
#     principal = "python" 
#     def new(self):
#         print("Hello")

# class Child(Parent):
#     def child(self):
#         print("parent principle")
#         Parent.new(self)

# obj = Child()
# obj.child()
# print((Parent.principal)) 



#protected variable

# class Parent:
#     _principal = "python" 
#     def _new(self):
#         print("Hello")

# class Child(Parent):
#     def child(self):
#         print(Parent._principal)
#         Parent._new(self)

# obj = Child()
# obj.child()
# print((Parent._principal))

  


#private variable

# class Parent:
#     __principal = "python" 
#     def __new(self):
#         print("Hello")

# class Child(Parent):
#     def child(self):
#         print(Parent.__principal)
#         Parent.__new_new(self)

# obj = Child()
# # obj.child()
# # print((Parent.__principal)) 





# class Parent:
#     __principal = "python" 
#     def __new(self):
#         print("Hello")

# class Child(Parent):
#     def child(self):
#         print(Parent.__principal)
#         Parent.__new(self)

# obj = Child()
# # obj.child()
# print(Parent._Parent__principal)
# # print(Parent.__new)
# # print(dir(Parent))





# x = 10
# print(x)
# print(y:=10)



# polymorphism

class Calculator:
    
              


 








 


         
               

                           
  

   
    
 


