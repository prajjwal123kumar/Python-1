class C1:
    s1=0
    s2=0
    def __init__(self):
        self.a=1
        self.b=2
    def showdata(self):
        print(self.a,self.b)
ob=C1()
ob.showdata()
C1.showdata(ob) # Method Resulation Technique