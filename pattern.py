row = 5
for r in range(1,row+1):
    for c in range(1,row+1):
        if(c>=r):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()   