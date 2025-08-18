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
# q = int(input("enter second number : "))
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
# def value(x,y,z):
#     print(f"value of x = {x}") 
#     print(f"value of x = {y}") 
#     print(f"value of x = {z}") 
# result = value(z=10,y=20,x=30)


# def add(x,y,z):
#    return x+y+z 
# result = add(z=10,y=20,x=30)
# print(result)



# default keyword argument
# def sum(x=0,y=0,z=0):
#     return x+y+z
# result = sum(z=10,y=20,x=30)
# print(result)
# result = sum(z=10,y=20)
# print(result)



# variable length keyword argument
# def show(**x):
#     print(x)
#     print(type(x))
# result = show(x=10,y=20,z=30,p=40,q=50,r=60)    




# eval
# x = input("enter a number : ")
# print(x)
# print(type(x))

# print(tuple(x))

# y = (10,20,30)
# print(str(y))


# x = eval(input("enter a number : "))
# print(x)
# print(type(x))

# y=eval('2+5-1*5')
# print(y)


# x = ((1,2,3,4,5),)
# sum = 0
# for i in x:
#     print(i)
#     for j in i:
#         sum+=j
# print(sum)  


# x = eval(input("enter a number : "))
# print(x)
# print(type(x))   


# def add(*n):
#     sum = 0
#     for i in n:
#        print(i)
#     for j in i:
#         sum+=j
#     return sum
# ans = add((2,3,4,5),)
# print(ans)



# def display(**n):
#     # for i in n:
#     for k,v in n.items():
#         print(f'key is {k} and value is {v}')
# x = eval(input("enter a tuple : "))
# result = display(**x)
# print(result)            
       
       
       
# def show(**n):
#     print(n)
#     print(type(n))
# d=eval(input("enter a dict :"))
# show(**d) 


# def display(**n):
#     for k,v in n.items():
#         print(f'key is {k} and value is {v}')
# d=eval(input("enter a dict :"))
# display(**d)   


# def show(x,y,z=0,*n,p,q=0,**m):
#     print(x) 
#     print(y) 
#     print(z) 
#     print(n) 
#     print(p) 
#     print(q) 
#     print(m) 
# show(1,2,10,2,4,6,p=20,q=30,r=10,s=20,t=20) 



# x= [10,20,30,40]
# p,q,r,s=[10,20,30,40]
# print(p)
# print(q)
# print(r)
# print(s) 


# x = [10,20,30,40]
# print(*x) 


# x = 'python'
# print(*x)   



# def add(*n):
#     sum = 0
#     for i in n:
#         sum = sum+i
#     return sum
# x = eval(input("enter any collection : "))
# result = add(*x)   
# print(result)  


# w = 10
# x = 10,
# print(type(w))
# print(type(x))
# y = (10)
# z = (10,)
# print(type(y))
# print(type(z))
# p = ("mantasha")
# print(type(p))
# q = ((1,2,3,4))
# print(type(q))



# n=int(input("Enter any no:")) 
# factors = [] 
# for i in range(1,n+1): 
#     if n%i==0: 
#         factors.append(i) 
 
# print("Factors are :",factors) 



# map()

l = [1,2,3,4,5]
def squar(n):
    return n**2
result = map(squar,l)
print(result)
print(tuple(result))
print(list(result))      #interview question



l1 = [6,7,8,9,10]
l2 = [1,2,3,4,5]
l3 = [1,2,3,4]
l4 = [1,2,3]
def add(x,y,z,p):
    return x+y+z+p
result = map(add,l1,l2,l3,l4)     #interview question
print(list(result))





l1 = [6,7,8,9,10]
l2 = [1,2,3,4,5]
l3 = [1,2,3,4,5]
def add(x,y,z):
    return x+y+z
result = map(add,l1,l2,l3)     #interview question
print(list(result))



# filter()

# l = [1,2,3,4,5]
# def even_no(n):
#     if n%2==0:
#         return n
# result = list(filter(even_no,l))
# print(result)  



# l = [1,2,3,4,5]
# def odd_no(n):
#     if n%2!=0:
#         return n
# result = list(filter(odd_no,l))
# print(result)



# l = [1,2,3,4,5]
# def odd_no(n):
#     if n%2!=0:
#         return 'even'
#     else:
#         return 'odd'
# result = list(map(odd_no,l))
# print(result)












  










  
       

       

       





    


 

   



