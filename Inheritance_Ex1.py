class Class1:
    def __init__(self):
        self.a=1
        self.b=2
    def setdata(self):
        print("I am calling Class1.")
class Class2(Class1):
    def __init__(self):
        super().__init__()
        self.c=3
        self.d=4
    def setdata(self):
        print("I am calling Class2.")
ob1=Class1()
ob2=Class2()
print("OK")
    