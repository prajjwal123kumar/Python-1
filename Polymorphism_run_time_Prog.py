# BLL
class C1:
    def showdata(self):
        print("I am in C1 class.")
    def getobjectbyid(self,id):
        if id==5:
            ob=C1()
        else:
            ob=C2()
        return ob
class C2(C1):
    def showdata(self):
        print("I am in C2 class.")
# PL
ob1=C1()
ob2=C2()
ob1.showdata()
ob2.showdata()
while(True):
    id=int(input("Enter Id : "))
    ob=ob1.getobjectbyid(id)
    ob.showdata()