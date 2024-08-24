#it is called as iteation.
#wap to print 1 to 10 numberw.
num=1
while(num<=10): 
   print(num,end="")
   num+=1

#sum of 1 to 100.
   total=0
   num=1
   while(num<=100):
      print(num)
      num+=1
      total+=1
      print("total",total)

#wap to print the even num between 1 to 10.
num=1
while num<=10:
      if num % 2 ==0:
        print(num)
      num+=1

#wap to print initialize the list value
#wap to print the factorial of a number. 
n=int(input('enter a number:'))
fact=1
num=1
while(num<=n):
    fact*=num
    num+=1
print('factorial:',fact)

#print 1 to 10 numbers
for num in range(1,11,1):
    print(num,end="")

#print 10 to 1 numbers
for num in range(10,0,-1):
    print(num,end="")

#membership operatoe(in and not in)
fruits=["apple","banana","orange","grape","kiwi"]
print("is banana in the list of fruits?",'banana'in fruits)
print("is watermelon in the list of fruits?",'watermelon'in fruits)
print("is mango not in the list of fruits?",'mango'not in fruits)
print("is grape not in the list of fruits?",'grape'not in fruits)

#nested loops
city=['jaipur','delhi','mumbai']
fruits=['apple','mango','cherry']
for x in city:
    for y in fruits:
        print(x,":",y)

#pass statement
a=int(input('enter the 1st number:'))
b=int(input('enter the 2nd number:'))
if(b==0):
    pass
else:
    print('a/b=',a/b)

#break statement
n=1
while(n<=5):
    print('n=',n)
    k=1
    while(k<=5):
        if(k==3):
         break
    print('k=',k,end='')
    k+=1 
    n+=1
    print()