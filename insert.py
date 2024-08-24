#wap to create a list and add the float value in a different specific location.
s=["jaya","ab","def"]
s.insert(1,3.4)
s.insert(2,6.7)
print(s)

#if the insert index is not found in the list then it insert the values at 1st and last.
s1=["jaya","ab","def"]
s1.insert((-3),3.4)
s1.insert(7,6.7)
print(s1)