def outerfunc(funcname):
    def innerfunc():
        print("from inner function")
        x = funcname()
    return innerfunc
def new():
    print("from new function")
res = outerfunc(new)
res()
       