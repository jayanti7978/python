#fabonacci series
a=0
b=1
print(a)
print(b)
s=10
for a in range (1,s):
     c=a+b
     print(c)
     a,b=b,c


#even numbers

   
     for i in range(0,101):
          if i%2 ==0:
             print(i)

#factorial number
n=8
fact=1
if n>=1: 
   for i in range(1,n+1):
     fact=fact*i
print(fact)


#prime number
a=int(input('enter a number'))
x=2
n=0
while x<a:
    if a%x==0:
        n=1
        break
        n=n+1
#if n==1:
 #   print('a is not a primr number')
#else:
#    print('a is a prime number')