# def add(x,y):
#     print(x+y)
# p = int(input("enter first number : "))
# q = int(input("enter second number : "))
# result = add(p,q) 
# if result%2==0:
#     print(result , " :is even")
# else:
#     print(result ," :is odd")




# def add(x,y):
#     return(x+y)
# p = int(input("enter first number : "))
# q = int(input("enter secon    d number : "))
# result = add(p,q) 

# if result%2==0:
#     print(f'given num {result} is even')
# else:
#     print(f'given num {result} is odd')


# positional argument
# def sum(x,y,z):
#     return x+y+z
# result = sum(10,20,30,40)
# print(result)



# default argument
# def sum(x=0,y=0,z=0):
#     return x+y+z
# result = sum()
# print(result)
# result = sum(10)
# print(result)
# result = sum(10,20)
# print(result)


# variable length positional argument
# def add(*x):
#     print(x)
#     print(type(x))
# result = add(10,20,30,5,4,6) 

# def sum(*args):
#     sum = 0
#     for i in args:
#         sum = sum+i
#     return sum
# result = sum(10,20,4,5,30) 
# print(result) 


# keyword positional argument
def value(x,y,z):
    print(f"value of x = {x}") 
    print(f"value of x = {y}") 
    print(f"value of x = {z}") 
result = value(z=10,y=20,x=30)


def add(x,y,z):
   return x+y+z 
result = add(z=10,y=20,x=30)
print(result)



# default keyword argument
def sum(x=0,y=0,z=0):
    return x+y+z
result = sum(z=10,y=20,x=30)
print(result)
result = sum(z=10,y=20)
print(result)



# variable length keyword argument




    


 

   



