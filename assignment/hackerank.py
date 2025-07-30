# test case 0
print("hello, world!")


# test case 1
n = int(input("enter a number"))
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")
    
    
    
year = int(input("enter a year:"))    
def is_leap(year):
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap(year)) 



num = int(input("enter a number:"))
for i in range(1, num + 1):
    print(i, end='')
    
    
    
    
    
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"
import re
print(str(bool(re.match(regex_pattern, input("enter a number:")))))


# import re
# n = int(input())
# for _ in range(n):
#     number = input().strip()
#     if re.match(r'^[789]\d{9}$', number):
#         print("YES")
#     else:
#         print("NO")    
       
