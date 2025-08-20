while True:
    print("1 '+' \n2 '-' \n3 '*' \n4 '/' \n5 'off' ")
    n = int(input("enter your choice :"))
    x = (1,2,3,4,5)
    if n in x:
        y = [1,2,3,4]
        if n in y:
            p = float(input("enter a first number : "))
            q = float(input("enter a second number : "))
            if n==1:
                print(f"Addition of {p} and {q} is : {p+q}")
            elif n==2:
                print(f"subtraction of {p} and {q} is : {p-q}")
            elif n==3:
                print(f"multiplication of {p} and {q} is : {p*q}")
            elif n==4:
                print(f"division of {p} and {q} is : {p/q}")
        else:
            break
    else:
        print("please enter a  valid option")    