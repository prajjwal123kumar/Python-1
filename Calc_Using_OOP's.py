# WAP to create calculator Using OOP's
# BLL code start from here
class Calculator:
    def __init__(self):
        self.no1=0
        self.no2=0
        self.result=0
    def sum(self):
        self.result=self.no1+self.no2
    def subtract(self):
        self.result=self.no1-self.no2
    def multiplication(self):
        self.result=self.no1*self.no2
    def division(self):
        self.result=self.no1/self.no2
# BLL code ends here

# PL code start from here
print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n0.Exit")
ch=input("Enter Your Choice... : ")
if ch=='1':
    calc=Calculator()
    calc.no1=int(input("Enter No1. : "))
    calc.no2=int(input("Enter No2. : "))
    calc.sum()
    print("Sum of Number = ",calc.result)
if ch=='2':
    calc=Calculator()
    calc.no1=int(input("Enter No1. : "))
    calc.no2=int(input("Enter No2. : "))
    calc.subtract()
    print("Subtract of Result = ",calc.result)
if ch=='3':
    calc=Calculator()
    calc.no1=int(input("Enter No1. : "))
    calc.no2=int(input("Enter No2. : "))
    calc.multiplication()
    print("Multiplication of Result = ",calc.result)  
if ch=='4':
    calc=Calculator()
    calc.no1=int(input("Enter No1. : "))
    calc.no2=int(input("Enter No2. : "))
    calc.division()
    print("Division of Result = ",calc.result)
# PL code ends here