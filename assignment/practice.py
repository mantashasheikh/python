def string_length(s):
    count=0
    for _ in s:
        count = count+1
    return count
n = input("enter a string:")
result = string_length(n)  
print(result) 


def reverse(s):
    return s[::-1]
n = input("enter a string: ")
result = reverse(n)
print(result)
    