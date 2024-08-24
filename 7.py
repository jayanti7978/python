#wap to input the basic salary of an employee and find out the gross salary.
#gs=bs+ta+da+hra
bs=float(input('enter basic salary'))
ta=bs*5/100
#if you want to print the value of ta then you must write print('ta=',ta)
da=bs*6/100
hra=bs*30/100
gs=bs+ta+da+hra
print('gross salary',gs)
