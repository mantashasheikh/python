# def add(x,y):
#     print(x+y)
# p = int(input("enter first number : "))
# q = int(input("enter second number : "))
# result = add(p,q) 
# if result%2==0:
#     print(result , " :is even")
# else:
#     print(result ," :is odd")




def add(x,y):
    return(x+y)
p = int(input("enter first number : "))
q = int(input("enter second number : "))
result = add(p,q) 

if result%2==0:
    print(f'given num {result} is even')
else:
    print(f'given num {result} is odd')    




