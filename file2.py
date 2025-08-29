# write()

# f = open('n1.txt','a')
# f.write('''\n this is a python class
#         this is a python class
#         this is a python class \n''')
# f.close()
# print(f.closed)

# f = open('n2.txt','a')
# f.writelines(['hello\n','hi\n','welcome\n'])
# f.close()

# f = open('n2.txt','a')
# print(f.writable())



# read()

f = open('n1.txt')
# print(f.mode)

# data = f.read()
# print(data)
# f.close()

# data = f.read(10)
# print(data)
# data = f.read(10)
# print(data)

# data = f.readline()
# print(data)

# data = f.readlines()
# print(data)

# print(f.readable())


# with open('n1.txt') as f:
#     data = f.read()
#     print(data)
# print(f.closed)



# 27/8/25

# with open('n1.txt','a+') as f:
#     print(f.name)
#     print(f.mode)
#     print(f.closed)
# print(f.closed) 


# with open('n1.txt','a+') as f:
#     print(f.tell())


# with open('n6.txt','x') as f:
#     print(f.tell())
    
    
# with open('n6.txt','w') as f:
#     print(f.tell())  


# with open('n6.txt','r') as f:
#     print(f.tell())
#     data = f.read(5)
#     print(data)
#     print(f.tell())


# with open('n6.txt','rb') as f:
#     print(f.tell())
#     data = f.read(5)
#     print(f.tell())
#     f.seek(0)
#     print(f.tell())
#     data = f.read(10)
#     print(f.tell())
#     f.seek(5,0)
#     print(f.tell())
#     f.seek(2,1)
#     print(f.tell())
#     f.seek(-5,1)
#     print(f.tell())
#     f.seek(-5,2)
#     print(f.tell())


# 28/8/25

# import pickle
# f = open('n1.pkl','ab')
# data = {
#     'name':'neeraj',
#     'age':33,
#     'quali':'btech'
# }
# pickle.dump(data,f)
# f.close


# import pickle
# f = open('n1.pkl','ab')
# data = "this is python class"
# pickle.dump(data,f)
# f.close


# import pickle
# f = open('n2.pkl','ab+')
# data = {"this" ,"is" ,"python" ,"class"}
# pickle.dump(data,f)
# f.close
# import pickle
# f = open('n2.pkl','rb+')
# data = pickle.load(f)
# print(data)


# import pickle
# f = open('n3.pkl','ab+')
# data = ["this" ,"is" ,"python" ,"class"]
# pickle.dump(data,f)
# f.close
# import pickle
# f = open('n3.pkl','rb+')
# data = pickle.load(f)
# print(data)



import pickle
l = []
with open('n1.pkl','rb+') as f:
    while True:
        try:
            data = pickle.load(f)
            l.append(data)
        except EOFError:
            break
        
print(l)        



    
    




       


    
    
    


   
 








