a = int(input('Enter a number: '))
x = 2
n = 0
while x < a:
    if a % x == 0:
        n = 1
        break
    x += 1

if n == 1:
    print(f'{a} is not a prime number.')
else:
    print(f'{a} is a prime number.')




def case_1(s):
    result = ""
    for i, char in enumerate(s):
        if i % 2 == 0:
            result =result + char.upper()
        else:
            result =result + char.lower()
    return result
print(case_1("jayanti"))




def custom_case(s):
    if len(s) >= 3:
        return s[:3].upper() + s[3:].lower()
    else:
        return s.upper()
print(custom_case("ranjan"))




def merge_strings(s1, s2):
    if len(s1) >= 2 and len(s2) >= 2:
        return s1[:2] + s2[1:]
    else:
        return s1 + s2
print(merge_strings("Bsa", "iwa"))



def upper_case_strip(s):
    return s.strip().upper()
print(upper_case_strip("jayanti "))




from itertools import zip_longest

def merge_strings(s1, s2):
    merged = ''.join(a + b for a, b in zip_longest(s1, s2, fillvalue=''))
    return merged

string1 = "Bsa"
string2 = "iwa"
output = merge_strings(string1, string2)
print(output)



a=int(input('enter a number:'))
x=2
n=0
while x < a:
    if a%x ==0:
     n=1
     break
    x=x+1
if n==1:
    print(f'{a} is not a prime number:')
else:
    print(f'{a} is a prime number:')

a=int(input('enter a number'))
x=2
n=0
while x< a:
    if a%x==0:
        n=1
        break
    x=x+1
if n==1:
    print(f'{a} is not a prime number')
else:
    print(f'{a} is a prime number')

a=int(input('enter a number'))
x=2
n=0
while x<a:
    if a%x==0:
        n=1
        break
    x=x+1
if n==1:
    print(f'{a} is not a prime number')
else:
    print(f'{a}is a prime number')