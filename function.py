def hello():
    print("hellothere!")
def goodbye():
    print("see ya!")

hello()
goodbye()

# def biodata():
#     name:jayanti panda
#     dis:bhadrak 
# biodata()

def add_numbers(num1,num2):
    return num1+num2
number1=float(input("enter the 1st number"))
number2=float(input("enter the 2nd number"))
result=add_numbers(number1,number2)
print('the sum of',number1,'and',number2,'is',result)