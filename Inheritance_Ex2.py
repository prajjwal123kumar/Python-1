# BLL
class C1:
    def __init__(self):
        self.a=1
        self.b=2
    def setdata(self):
        print("I am calling C1 class.")
class C2(C1):
    def __init__(self):
        super().__init__()
        self.c=3
        self.d=4
    def setdata(self):
        super().setdata()
        print("I am calling C2 class.")
# PL
ob1=C1()
ob2=C2()
# ob1.setdata()
ob2.setdata()
print("OK")
