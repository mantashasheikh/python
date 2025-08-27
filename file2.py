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


with open('n1.txt') as f:
    data = f.read()
    print(data)
print(f.closed)    








