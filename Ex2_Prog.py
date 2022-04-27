class C1:
    s1=10
    s2=20
    def __init__(self):
        self.a=1
        self.b=2
    def showdata(self):
        print(self.a,self.b,self.s1,self.s2,C1.s1,C1.s2)
ob1=C1()
ob2=C1()
ob1.showdata()
print(ob1.a,ob1.b)
print(ob1.s1,ob1.s2)