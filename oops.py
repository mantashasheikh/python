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


class Student:
    def __init__(self):
        print("external constructor called")
x = Student
print(id(x),id(Student))    #same address
y = Student()
print(id(y),id(Student))    #different address











   