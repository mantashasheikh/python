def Factors(n):
    factors = [] 
    for i in range(1,n+1): 
        if n%i==0: 
            factors.append(i) 
    return factors
num = int(input("enter a number : "))
ans = Factors(num)
print(ans)



def Sort(l):
    for i in range(len(l)-1): 
        for j in range(len(l)-i-1): 
            if l[j] > l[j+1]: 
                l[j], l[j+1] = l[j+1], l[j] 
    return l            
list = [64, 34, 25, 12, 22, 11, 90, 5] 
sort = Sort(list)            
print(sort)




 
def Descending(l):
    n = len(l) 
    for i in range(n-1): 
        for j in range(n-i-1): 
            if l[j] < l[j+1]: 
                l[j], l[j+1] = l[j+1], l[j]
    return l             
list = [64, 34, 25, 12, 22, 11, 90, 5] 
sort = Descending(list)            
print(sort)  




 = [2,4,9,3,5] 
max = l[0] 
for i in range(len(l)-1): 
    if l[i]>l[i+1]: 
        max = l[i] 
        l[i],l[i+1]=l[i+1],l[i]   
    else: 
        max=l[i+1] 
print(max)           









 

            
        
          
         
    

    
    
    