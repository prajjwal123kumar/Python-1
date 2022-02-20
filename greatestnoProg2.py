# WAP to find greatest no. from input 4 numbers

# BLL code start from here
def greatestNo(n1,n2,n3,n4):
    if n1>n2:
        if n1>n3:
            if n1>n4:
                print(n1,"is greatest no.")
            else:
                print(n4,"is greatest no.")
        else:
            if n3>n4:
                print(n3,"is greatest no.")
            else:
                print(n4,"is greatest no.")
    else:
        if n2>n3:
            if n2>n4:
                print(n2,"is greatest no.")   
            else:
                print(n4,"is greatest no.")   
        else:
            if n3>n4:
                print(n3,"is greatest no.")
            else:
                print(n4,"is greatest no.")

    
# BLL code ends here

# PL code start from here
n1=int(input("Enter first number : "))
n2=int(input("Enter second number : "))
n3=int(input("Enter third number : "))
n4=int(input("Enter fourth number : "))
greatestNo(n1,n2,n3,n4)
# PL code ends here


