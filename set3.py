#add()-
#it adds the value in set.
s={2,3,4,5,5,6,7,9}
s.add(23)
s.add(2)
print(s)
#update()-
s={3,4,5,6}
l=[3,5,6,7]
t=(1,23,45,67,89)
s.update(l,t)
print(s)
#wap to add the different data items and also range function.
s={1,2,3,4}
s1={"jaya","abc","xyz"}
s2=set(range(10))
s.update(s,s1)
print(s)
#remove()-remove method used to remove the values one by one.
#it shows the key error(if remove value is not found in the set)
s={10,20,30,40}
s.remove(20)
print(s)
#discard()-it is similar to remove,but it is not give the key error.
s={1,3,2,4,5}
s.discard(2)
print(s)
#pop()-
s=set()
print(s)
s.pop()
print(s)
#how to get which element is deleted in the set.
s={2,3,4,5,6}
s.remove(3)
print(s)
print(s.pop())
#copy()-it is used to return shallow copy.
s={2,3,4,5,6}
print(s)
s1=s.copy()
print(s1)