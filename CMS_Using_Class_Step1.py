# CRUD Operation using Class (User Defined Data Type)
# Customer Management System (CMS)
# All Globle Variables.
class Customer:
    def __init__(self):
        self.id=0
        self.name=""
        self.address=""
        self.mobile_no=""
        self.age=0
list_cus=[]
#BLL Code start from here
def add_customer(cus):
    list_cus.append(cus)
def search_customer(cus_id):
    for e in list_cus:
        if e.id==cus_id:
            return e
    return False
def update_customer(cus_id,cus):
    for e in list_cus:
        if e.id==cus_id:
            e.name=cus.name
            e.address=cus.address
            e.mobile_no=cus.mobile_no
            e.age=cus.age
            return True
    return False
def delete_customer(id):
    for i in range(len(list_cus)):
        if list_cus[i].id==id:
            list_cus.pop(i)
            return True
    return False
def show_all_customer():
    for i in range(len(list_cus)):
        details="Id={0}, Name={1}, Address={2}, Mobile Number={3}, Age={4}".format(list_cus[i].id,list_cus[i].name,list_cus[i].address,list_cus[i].mobile_no,list_cus[i].age)
        print(details)
# BLL code ends here

#PL Code start from here
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
        add_customer(cus)
        print("Customer Added Successfully.")
        # Write code to add a customer
    elif(ch=='2'):
        cus_id=int(input("Enter Id : "))
        cus=search_customer(cus_id)
        if cus==False:
            print("Id Not Found.")
        else:
            print("Id=",cus.id,"Name=",cus.name,"Address=",cus.address,"Mobile Number=",cus.mobile_no,"Age=",cus.age)
        # Write code to search a customer
    # Update on what basis = id basis
    # What to Update = name,address,age,mobile no.
    elif(ch=='3'):
        cus=Customer()
        cus.id=int(input("Enter Id for Update/Modify : "))
        cus.name=input("Enter Name for Update/Modify : ")
        cus.address=input("Enter Address for Update/Modify : ")
        cus.mobile_no=input("Enter Mobile Number for Update/Modify : ")
        cus.age=int(input("Enter Age for Update/Modify : "))
        update_customer(cus.id,cus)
        if cus==False:
            print("Id Not Found.")
        else:
            print("Customer Updated Successfully.")
        # Write code to modify/Update a customer
    elif(ch=='4'):
        id=int(input("Enter Id : "))
        details=delete_customer(id)
        if cus==False:
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