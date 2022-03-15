# CRUD Operation using List 
# Customer Management System (CMS)
#BLL Code start from here
list_id=[]
list_name=[]
list_address=[]
list_age=[]
list_mobile_no=[]
def add_customer(id,name,address,age,mobile_no):
    list_id.append(id)
    list_name.append(name)
    list_address.append(address)
    list_age.append(age)
    list_mobile_no.append(mobile_no)
def search_customer(id):
    i=list_id.index(id)
    name=list_name[i]
    address=list_address[i]
    age=list_age[i]
    mobile_no=list_mobile_no[i]
    details="Name = {0} Address = {1} Age = {2} Mobile number = {3}".format(name,address,age,mobile_no)
    return details
def update_customer(id,name,address,age,mobile_no):
    i=list_id.index(id)
    list_name[i]=name
    list_address[i]=address
    list_age[i]=age
    list_mobile_no[i]=mobile_no
def delete_customer(id):
    i=list_id.index(id)
    list_id.pop(i)
    list_name.pop(i)
    list_address.pop(i)
    list_age.pop(i)
    list_mobile_no.pop(i)
def show_all_customer():
    for i in range(len(list_id)):
        details="Id={0}, Name={1}, Address={2}, Age={3}, Mobile Number={4}".format(list_id[i],list_name[i],list_address[i],list_age[i],list_mobile_no[i])
        print(details)
# BLL code ends here

#PL Code start from here
while(True):
    print('1.Add Customer\n2.Search Customer\n3.Update/Modify Customer\n4.Delete Customer\n5.Show All Customer\n0.Exit')
    ch=input("Enter Your Choice : ")
    if(ch=='1'):
        id=int(input("Enter Id : "))
        name=input("Enter Name : ")
        address=input("Enter Address : ")
        age=int(input("Enter Age : "))
        mobile_no=input("Enter Mobile Number : ")
        add_customer(id,name,address,age,mobile_no)
        print("Customer Added Successfully.")
        # Write code to add a customer
    elif(ch=='2'):
        id=int(input("Enter Id : "))
        details=search_customer(id)
        print(details)
        # Write code to search a customer
    # Update on what basis = id basis
    # What to Update = name,address,age,mobile no.
    elif(ch=='3'):
        id=int(input("Enter Id for Update/Modify : "))
        name=input("Enter Name for Update/Modify : ")
        address=input("Enter Address for Update/Modify : ")
        age=int(input("Enter Age for Update/Modify : "))
        mobile_no=input("Enter Mobile Number for Update/Modify : ")
        update_customer(id,name,address,age,mobile_no)
        print("Customer Updated Successfully.")
        # Write code to modify/Update a customer
    elif(ch=='4'):
        id=int(input("Enter Id : "))
        details=delete_customer(id)
        print("Customer Delete SuccessFully.")
        # Write code to delete a customer
    elif(ch=='5'):
        show_all_customer()
        # Write code to show all customers
    elif(ch=='0'):
        break
        # Write code to show all customers
# PL code ends here