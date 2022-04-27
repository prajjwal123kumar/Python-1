# BLL
class C1:
    def __init__(self):
        self.a=1
        self.b=2
    def showdata(self):
        print(self.a,self.b)
class C2(C1):
    def __init__(self):
        super().__init__()
        self.c=3
        self.d=4
    def showdata(self):
        super().showdata()
        print(self.c,self.d)
class C4:
    def __init__(self):
        self.g=7
        self.h=8
    def showdata(self):
        print(self.g,self.h)
        
class C3(C2,C4):
    def __init__(self):
        super().__init__()
        C4.__init__(self)

        self.e=5
        self.f=6
    def showdata(self):
        super().showdata()
        print(self.e,self.f)

# PL
ob1=C1()
ob1.showdata()
ob2=C2()
ob2.showdata()
C1.showdata(ob2)
ob4=C4()
ob4.showdata()
ob3=C3()
ob3.showdata()
C2.showdata(ob3)
C4.showdata(ob3)