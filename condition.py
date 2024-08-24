#1:=wap to enter 3 nos and check the greatest no by using ladder.
x=input('enter the 1st number')
y=input('enter the 2nd number')
z=input('enter the 3rd number')
if(x>y):
    print('x is greater')
elif(y>x):
    print('y is greater')
elif(z>x):
    print('z is greater')
else:
    print('all are equal')

#2:-
a=int(input('enter marks out of 300'))
b=a/300*100
print('percentage is',b,'%')
if(a>300):
    print('you enter a wrong marks')
elif(b>60):
    print('your division is first')
elif(b>50 and b<53):
    print('your division is second')
elif(b>33 and b<50):
    print('your division is third')
else:
    print('you failed')

#s craiteria
a=int(input('enter your age'))