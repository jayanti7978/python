#here float value cann't be interprited bytes can accept only integer value.
l1=[1,2,3,4,5]
l2=[5.2,7.3,6.3,5.4]
a=bytes(l1)
for i in a:
    print(i)
b=bytes(l2)
for j in b:
    print(j)