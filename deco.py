# def outerfunc(funcname):
#     def innerfunc():
#         print("from inner function")
#         x = funcname()
#     return innerfunc
# def new():
#     print("from new function")
# res = outerfunc(new)
# # res()


# # H.W.


# a = "mantasha"
# a1 = ""
# for i in a:
#     s1 = ord(i)
#     if s1%2==0:
#         # print(s1)
#         a1 = a1+chr(ord(i))
# print(a1)    
    
       


# # decorator to print only the original string
# def show_original(func):
#     def wrapper(s):
#         print("Original String:", s)   # print original string
#         func(s)                        # call reverse function (but ignore result)
#     return wrapper

# # function to reverse string
# @show_original
# def reverse_string(s):
#     return s[::-1]   # reversal still happens, but not shown

# # test
# reverse_string("Mantasha")


def natural(n):
    for i in range(1,n+1):
        return i
x = int(input("enter a number:"))
res = natural(x)
print(res)  



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

       
       