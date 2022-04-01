# BLL
class C1:
    c=0 # Static/Shared Variable
    def __init__(self):
        self.a=0
        self.b=0
    def count(self):
        C1.c+=1
# PL
ob1=C1()
ob2=C1()
ob1.count()
print(C1.c) # 1