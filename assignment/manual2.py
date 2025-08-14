# find the factor of any number
# n=int(input("enter a number : "))
# factor = []
# for i in range(1,n+1):
#     if n%i==0:
#         factor.append(i)
# print(factor)  



# wap to arrange all items from list in assending order.
l = eval(input("enter a list : "))
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[j]>l[i]:
            l[i],l[j]=l[j],l[i]
print(l)            
       
    