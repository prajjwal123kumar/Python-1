# WAP to find greatest no. from input 3 numbers

# BLL code start from here
def greatestNo(n1,n2,n3):
    if n1>n2:
        if n1>n3:
            print(n1,"is greatest number.")
        else:
            print(n3,"is greatest number.")
    else:
        if n2>n3:
            print(n2,"is greatest number.")
        else:
            print(n3,"is greatest number.")
# BLL code ends here

# PL code start from here
n1=int(input("Enter first number : "))
n2=int(input("Enter second number : "))
n3=int(input("Enter third number : "))
greatestNo(n1,n2,n3)
# PL code ends here

















