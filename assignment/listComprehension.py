# # list comprehension

n = int(input("enter a number : "))
result = [i for i in range(1,n+1)]
print(result)


l = [1,2,3,4,5]
result = [l[i]**2 for i in range(len(l))]
print(result)


l = [1,2,3,4,5,6,7,8,9,10]
result = [i**2 for i in l]
print(result)


l = [1,2,3,4,5]
x = [i**2 for i in l if i%2==0]
print(x)

l = [1,2,3,4,5]
x = ['even' if i%2==0 else 'odd' for i in l]
print(x)


l = [1,2,3,4,5]
x = tuple('even' if i%2==0 else 'odd' for i in l)
print(x)


# dictionary comprehension

l = {1,2,3,4,5}
x = {i : i%2==0 for i in l}
print(x)

l = {1,2,3,4,5}
x = {i : i%2==0 for i in l if i%2==0   }
print(x)


l = [1,2,3,4,5]
x = {i:i**2 if i%2==0 else i**3 for i in l}
print(x)


# set comprehension
l = [1,2,3,4,5]
x = {i**2 if i%2==0 else i**3 for i in l}
print(x)











