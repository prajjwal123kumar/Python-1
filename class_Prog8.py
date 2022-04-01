class C1:
    count=0
    def __init__(self):
        self.c=0
        self.c+=1
        C1.count+=1
        print("Total object created = ",self.c,C1.count)
        # print("Total object created = ",self.c)
ob1=C1()
ob2=C1()
ob3=C1()

# Output -:
# Total object created =  1 1
# Total object created =  1 2
# Total object created =  1 3


