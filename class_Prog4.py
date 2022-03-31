# Write Process to print static & actual variable & actual function in class.
class C1:
    s1=5
    s2=6
    def __init__(self):
        self.a1=10
        self.a2=20
    def fun1(self):
        print(self.a1,self.a2)
        print(C1.s1,C1.s2)
    def fun2(self):
        self.fun1()