b=[1,2,3,4,5]
print(b[-1])
print(b[-2])
print(b[-3])
print(b[-4])
print(b[-5])

a=bytearray(b)
a[0]=35
for i in a:
    print (i)
