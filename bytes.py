#can you modify the bytes elements?
#ans:-no
#e.g-
b=[1,2,3,4,5]
a=bytes(b)
for i in a:
    a[0]=45
print(i)