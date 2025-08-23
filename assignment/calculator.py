# static calculator
# while True:
#     print("1 '+' \n2 '-' \n3 '*' \n4 '/' \n5 'off' ")
#     n = int(input("enter your choice :"))
#     x = (1,2,3,4,5)
#     if n in x:
#         y = [1,2,3,4]
#         if n in y:
#             p = float(input("enter a first number : "))
#             q = float(input("enter a second number : "))
#             if n==1:
#                 print(f"Addition of {p} and {q} is : {p+q}")
#             elif n==2:
#                 print(f"subtraction of {p} and {q} is : {p-q}")
#             elif n==3:
#                 print(f"multiplication of {p} and {q} is : {p*q}")
#             elif n==4:
#                 print(f"division of {p} and {q} is : {p/q}")
#         else:
#             break
#     else:
#         print("please enter a  valid option") 
        
        




# Dynamic Calculator for Multiple Numbers & Operations

# def calculator():
#     print("Dynamic Calculator")
#     print("You can enter full expressions like: 10 + 20 * 3 - 5 / 2")
#     print("Type 'exit' to quit.\n")

#     while True:
#         expression = input("Enter expression: ")

#         if expression.lower() == "exit":
#             print("Exiting Calculator. Goodbye!")
#             break

#         try:
#             # Evaluate the expression safely
#             result = eval(expression, {"__builtins__": None}, {})
#             print(f"Result: {result}\n")
#         except ZeroDivisionError:
#             print("Error! Division by zero.\n")
#         except Exception:
#             print("Invalid expression! Please try again.\n")


# # Run calculator
# calculator()


a=10

def add():
    print(4+2)
def sub():
    print(4-2)
def multi():
    print(4*2)
def div():
    print(4/2)
                
