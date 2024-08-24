#wap to print two separate lines
#print("Hey i am a good girl \n and this viewers are also good boy/girl")


s=(12,3,4,44,78,90)
for i in s:
    if i%2==0:
     print(i)


# s=('jayanti panda')
# index=0
# for index in s:
#    if index % 2 == 0:
#       print('')

#swapping of two number 
a=20
b=45
a=a+b
b=a-b
a=a-b
print('a:',a)
print('b:',b)
#or
a,b=b,a
print('a:',a)
print('b:',b)


#reverse of a number
s='jayanti panda'
rev_s=s[::-1]
print(rev_s)
#or
# s='jayanti panda'  
# for i in s():
#    print(i)


l=['panda','jayanti']
l1=''.join(l[::-1])
print(l1)

#even indwx
s='jayanti panda'
s1=''
for i in range (len(s)):
   if i%2==0:
      s1=s1+s[i]
print(s1)
#or

# s='jayamti panda'
# s1=s(l)
# for i in l:
#    if i%2==0:
#     print(i)

#sorting elements in dict
d={
   3:'of',
   1:'nalanda',
   5:'BBSR',
   4:'technology',
   2:'institute'
}

d1=dict(sorted(d.items()))
print(d1)

#palindrome of a number
l=[12321]
l1=l.copy()
l1.reverse()
print(l1)
for i in l:
 if l==l1:
   print(f'{i} is a palindrome number')
else:
  print(f'{i} is not a palindrome number')


l=[12,3,12,3,4,12,5,6,12]
print(l.count(12))
print(l.count(3))
l2=[l.count (i) for i in l]
result=dict(zip(l,l2))
print(result)

# l=[12,3,45,78,90,11,990]
# max=l[0]
# for i in l:
#   if i>max:
#     max i
# print('max is=',max)

# l=[1,2,2,3,4,9,3,4,5,6,7,8,9]
# cout=1
# for i in l:
#   if i = count
# print(i)

n=5
fact=1
if n>=1:
  for i in range(1,n+1):
    fact=fact*i
print('factorial number:',fact)

a=0
b=1
print(a)
print(b)
s=10
for a in range(1,s):
  c=a+b
  print(c)
  a,b=b,c

  a=[2,6,7,45,78,200,36]
  for i in range(len(a)):
    for j in range(i+1,len(a)):
     if a[i]>=a[j]:
      a[i],a[j]=a[j],a[i]
  dict={key:value for key,value in enumerate(a)}
  print(dict)