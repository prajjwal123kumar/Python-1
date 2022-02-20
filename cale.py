# WAP to create calculator

# BLL code start from here
def sum(no1,no2): # Formal Parameter
    res=no1+no2
    return res
def subtract(no1,no2):
    res=no1-no2
    return res
def multiplication(no1,no2):
    res=no1*no2
    return res
def division(no1,no2):
    res=no1/no2
    return res
# BLL code ends here

# PL code start from here
print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n0.Exit")
ch=input("Enter Your Choice... : ")
if ch=='1':
    no1=int(input("Enter No1. : "))
    no2=int(input("Enter No2. : "))
    r=sum(no1,no2) # Actual Parameter
    print("Sum of Result = ",r)
if ch=='2':
    no1=int(input("Enter No1. : "))
    no2=int(input("Enter No2. : "))
    r=subtract(no1,no2) # Actual Parameter
    print("Subtract of Result = ",r)
if ch=='3':
    no1=int(input("Enter No1. : "))
    no2=int(input("Enter No2. : "))
    r=multiplication(no1,no2) # Actual Parameter
    print("Multiplication of Result = ",r)
if ch=='4':
    no1=int(input("Enter No1. : "))
    no2=int(input("Enter No2. : "))
    r=division(no1,no2) # Actual Parameter
    print("Division of Result = ",r)
# PL code ends here