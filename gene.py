# generator
def natural(n):
    for i in range(1,n+1):
        yield i
x = int(input("enter a number:"))
res = natural(x)
for i in res:
    print(i)
    
    
    
def natural(n):
    for i in range(1,n+1):
        yield i
x = int(input("enter a number:"))
res = natural(x)
print(next(res)) 
print("hello")
print("world")
print(next(res))
print("mantasha")
for i in res:
    print(i)
print(res)