#def case_1(s):
    #r = ""
    #for i, char in enumerate(s):
        #if i % 2 == 0:
       #     r =r + char.upper()
      #  else:
     #       r =r + char.lower()
    #return r
#print(case_1("jayanti"))


s='nalanda'
a=s[0:4].upper()+s[4:7].lower()
print(a)


s='jyni'
s1='aati'
s2=''
for i in range(len(s)):
    s2=s2+s[i]+s1[i]
print(s2)





s='nalanda'
s3=''
for i in range(len(s)):
    if i%2==0:
        s3=s3+s[i].upper()
    else:
        s3=s3+s[i].lower()
s=s3
print(s)



s='institute'
print(s.upper())


l=[1,2,3,[4,5,4,6],8]
print(l[3])
#sum of the nested list:
nested_list=l[3]
s=sum(nested_list)
print(s)
#print the unique element from the nested list:
l=[1,2,3,[4,5,4,6],8]
nested_list=l[3]
print(set(nested_list))