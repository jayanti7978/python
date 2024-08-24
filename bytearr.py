#to display the list element after converting the bytearray & modify the values.
l=[2,3,4,5]
print(l)
b=bytearray(l)
b[0]=89
b[1]=90
b[2]=45
b[3]=34
for i in b:
    print(i)