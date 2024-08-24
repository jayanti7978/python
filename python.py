#1
def swaplist(newlist):
    size=len(newlist)
    temp=newlist[0]
    newlist[0]=newlist[size-1]
    newlist[size-1]=temp

    return newlist
newlist=[12,35,9,56,24]
print(swaplist(newlist))

#2.swap the last and first number of a list.
def swaplist(newlist):
    newlist[0],newlist[-1]=newlist[-1],newlist[0]
    return newlist

newlist=[12,35,9,56,24]
print(swaplist(newlist))

#swap 2 position of a list 
def listposition(list,pose1,pose2):
    list[pose1],list[pose2]=list[pose2],list[pose1]

    return list
list=[1,2,3,4,5,6,7,8]
pose1,pose2=1,4
print(listposition(list,pose1,pose2))


#3
def swappositions(list,pose1,pose2):
    for i, x in enumerate(list):
        if i == pose1:
            element1 = x
        if i == pose2:
            element2= x
    list[pose1] = element2
    list[pose2] = element1
    return list
list=[23,65,19,90]
pose1, pose2 =1, 3
print(swappositions(list,pose1-1,pose2-1))


#4
l1= ['Gfg','is','best','for','Geeks']
print("the original list is : " + str(l1))
res= [sub.replace('G','-').replace('e','G').replace('-','e') for sub in l1 ]
print("list after performing character swaps : "+str(res))

#5
l=[10,20,30,40]
n=len(l)
print('the length of list is : ',n)

#6
l2=[1,4,5,7,8]
print('the list is :'+ str(l2))


#7.function
def add(a,b):
    print(a+b)
    return add
obj=add(10,20)
print(obj)

def mul(a,b,c):
    d=a*b*c
    print(d)
    return mul
e=mul(10,20,30)
print(e)

def div(a,b):
    print(a/b)
    return div
obj1=div(123454646,78)
print(obj1)

def muldiv(a,b,c,d):
    e=a*b
    print(e)
    f=c*d
    print(f)
    t=e/f
    print(t)
    return muldiv
obj2=muldiv(100,330,440,2679)
print(obj2)

#8.cal by value
def nit(a):
    print('inside nit before modification',a)
    print('inside nit before modification',id(a))
    a=34000
    print('inside nit after modification',a)
    print('inside nit after modification',id(a))
a=122323432
print(a)
nit(a)
print(a)      


def nit(a):
    print('inside nit before modification',a)
    print('inside nit before modification',id(a))
    a=34000
    print('inside nit after modification',a)
    print('inside nit after modification',id(a))
a=[10,22,32,34,32]
print(a)
nit(a)
print(a) 



#
dict={
    10:'jayanti',
    20:'institute',
    9:'of',
    10:'nalanda'
}

print(dict)

l=[1,2,3,4,6,7,8,9]
l.remove(4)
print(l)

#wap to calculate simple intrest.
#p=float(input('enter value of p'))
#t=float(input('enter the value of t'))
#r=float(input('enter the value of r'))
#si=p*t*r/100
#print('simple intrest',si)


a=int(input('enter a number'))
x=2
n=0
while x<a:
    if a%x==0:
        n=1
        break
        n=n+1