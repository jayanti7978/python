std={'aba','abc','abd','xyz','aba'}
std2={'xyz','abd','fgh','kjl'}
print(std2.difference(std))
print(std.union(std2))
print(std.issubset(std2))
# it is used to return all the elements present in set A or B but in both.
#union is used to return all the elemets.