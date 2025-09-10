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



class Parent1:
    def home(self):
        print("from parent1")

class Parent2:
    def home(self):
        print("from parent2") 
        
class Child(Parent1,Parent2):
    def home(self):
        print("from child")
        super().home()
obj = Child()
obj.home()
               

                           
  

   
    
 


