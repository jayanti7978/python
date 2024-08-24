a=20

print('outside fun before causing:',a)
print('outside fun before causing:',id(a))
(a)
print('outside fun after causing:',a)
print('outside fun after causing:',id(a))


def fun(a):
    print('inside fun',a)
a=4
print('outside fun',a)
fun(a)
print('outside fun',a)


def fun(a):
    print('inside fun before modification:',a)
    print('inside fun berore modification:',id(a))
a=20
print('output fun before cusing:',a)
print('function fun before cusing:',id(a))
fun(a)
print('outside fun after cusing:',a)
print('outside fun after cusing:',id(a))
