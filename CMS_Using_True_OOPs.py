# Customer Management System (CMS)
# BLL Code start from here
class Customer:
    list_cus=[] # Static Member it has only one memory blocks.
    def __init__(self):
        self.id=0
        self.name=""
        self.address=""
        self.mobile_no=""
        self.age=0
    def __str__(self):
        return "Id:{0},NAme:{1},Address:{2},Mobile Number:{3},Age:{4}".format(self.id,self.name,self.address,self.mobile_no,self.age)
    def add_customer(self): # self=get data to add
        Customer.list_cus.append(self)
    def search_customer(self,cus_id):
        for e in Customer.list_cus:
            if e.id==cus_id:
                self.id=e.id
                self.name=e.name
                self.address=e.address
                self.mobile_no=e.mobile_no
                self.age=e.age
                return True
        return False
    def update_customer(self,cus_id):
        for e in Customer.list_cus:
            if e.id==cus_id:
                e.id=self.id
                e.name=self.name
                e.address=self.address
                e.mobile_no=self.mobile_no
                e.age=self.age
                return True
        return False
    def delete_customer(self,cus_id):
        for i in range(len(Customer.list_cus)):
            if Customer.list_cus[i].id==cus_id:
                Customer.list_cus.pop(i)
                return True
        return False
# BLL code ends here

#PL Code start from here
def show_all_customer():
    for cus in Customer.list_cus:
        details="Id:{0}, Name:{1}, Address:{2}, Mobile Number:{3}, Age:{4}".format(cus.id,cus.name,cus.address,cus.mobile_no,cus.age)
        print(details)
if __name__=="__main__":
    while(True):
        print('1.Add Customer\n2.Search Customer\n3.Update/Modify Customer\n4.Delete Customer\n5.Show All Customer\n0.Exit')
        ch=input("Enter Your Choice : ")
        if(ch=='1'):
            cus=Customer()
            cus.id=int(input("Enter Id : "))
            cus.name=input("Enter Name : ")
            cus.address=input("Enter Address : ")
            cus.mobile_no=input("Enter Mobile Number : ")
            cus.age=int(input("Enter Age : "))
            cus.add_customer()
            print("Customer Added Successfully.")
            # Write code to add a customer
        elif(ch=='2'):
            cus=Customer()
            cus_id=int(input("Enter Id : "))
            check=cus.search_customer(cus_id)
            if check==False:
                print("Id Not Found.")
            else:
                print("Id=",cus.id,"Name=",cus.name,"Address=",cus.address,"Mobile Number=",cus.mobile_no,"Age=",cus.age)
        # Write code to search a customer
    # Update on what basis = id basis
    # What to Update = name,address,age,mobile no.
        elif(ch=='3'):
            cus=Customer()
            # cus.id=int(input("Enter Id for Update/Modify : "))
            cus.name=input("Enter Name for Update/Modify : ")
            cus.address=input("Enter Address for Update/Modify : ")
            cus.mobile_no=input("Enter Mobile Number for Update/Modify : ")
            cus.age=int(input("Enter Age for Update/Modify : "))
            # check=cus.update_customer(cus.id)
            check=cus.update_customer(cus_id)
            if check==False:
                print("Id Not Found.")
            else:
                print("Customer Updated Successfully.")
        # Write code to modify/Update a customer
        elif(ch=='4'):
            cus=Customer()
            id=int(input("Enter Id : "))
            check=cus.delete_customer(id)
            if check==False:
                print("Id Not Found.")
            else:
                print("Customer Delete SuccessFully.")
        # Write code to delete a customer
        elif(ch=='5'):
            show_all_customer()
        # Write code to show all customers
        elif(ch=='0'):
            break
        # Write code to show all customers
# PL code ends here