# def outerfunc(funcname):
#     def innerfunc():
#         print("from inner function")
#         x = funcname()
#     return innerfunc
# def new():
#     print("from new function")
# res = outerfunc(new)
# res()
       


# decorator to print only the original string
def show_original(func):
    def wrapper(s):
        print("Original String:", s)   # print original string
        func(s)                        # call reverse function (but ignore result)
    return wrapper

# function to reverse string
@show_original
def reverse_string(s):
    return s[::-1]   # reversal still happens, but not shown

# test
reverse_string("Mantasha")

       
       