# BLL
class C1:
    def __init__(self):
        self.a=0
        self.b=0
    def count(self):
        self.a+=1
        self.b+=1
# PL
ob1=C1()
ob2=C1()
ob3=C1()
ob1.count()
print(ob2.a,ob2.b)
print(ob3.a,ob3.b)
print(ob1.a,ob1.b)