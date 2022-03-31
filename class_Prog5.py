# To outside class create object of class
class C1:
    s1=5
    s2=7
    def __init__(self):
        self.a1=0
        self.a2=0
# Procedure to create object of class
# object_name/variable_name=class_name()
ob1=C1()
ob1.a1=25
ob1.a2=35
print(ob1.a1,ob1.a2) # 25 35
ob2=C1()
print(ob2.a1,ob2.a2) # 0 0