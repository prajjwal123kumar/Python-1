# Employee Management System (EMS) Using Inheritance
# BLL code starts here
class EMP:
    list_emp=[]
    def __init__(self):
        self.id=0
        self.name=""
        self.type=""
    def __str__(self):
        return "Id = {0} , Name = {1} , Type = {2}".format(self.id,self.name,self.type)
    @ staticmethod
    def get_employee_type_by_id(emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                return e.type
        return False
    def add(self):
        EMP.list_emp.append(self)
    def search(self,emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                self.id=e.id
                self.name=e.name
                self.type=e.type
                return True
        return False
    def update(self,emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                e.name=self.name
                e.type=self.type
                return True
        return False
    def delete(self,emp_id):
        for i in range(len(EMP.list_emp)):
            if EMP.list_emp[i].id==emp_id:
                EMP.list_emp.pop(i)
                return True
        return False
class DIR(EMP):
    def __init__(self):
        super().__init__()
        self.dir_special=''
        self.share=''
    def __str__(self):
        # str_data=super().__str__()
        # return str_data+" Dir Special = {0} , Share = {1}".format(self.dir_special,self.share)
        return super().__str__()+ " , Dir Special = {0} , Share = {1}".format(self.dir_special,self.share)
    def add(self):
        super().add()
    def search(self,emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                self.dir_special=e.dir_special
                self.share=e.share
                super().search(emp_id)
                return True
        return False
    def update(self,emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                e.dir_special=self.dir_special
                e.share=self.share
                super().update(emp_id)
                return True
        return False
    def delete(self, emp_id):
        return super().delete(emp_id)
class MGR(EMP):
    def __init__(self):
        super().__init__()
        self.mgr_special=''
        self.incentive=''
    def __str__(self):
        # str_data=super().__str__()
        # return str_data+ " Mgr Special = {0} , Incentive = {1}".format(self.mgr_special,self.incentive)
        return super().__str__()+ " , Mgr Special = {0} , Incentive = {1}".format(self.mgr_special,self.incentive)
    def add(self):
        super().add()
    def search(self,emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                self.mgr_special=e.mgr_special
                self.incentive=e.incentive
                super().search(emp_id)
                return True
        return False
    def update(self,emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                e.mgr_special=self.mgr_special
                e.incentive=self.incentive
                super().update(emp_id)
                return True
        return False
    def delete(self, emp_id):
        return super().delete(emp_id)
class TT(EMP):
    def __init__(self):
        super().__init__()
        self.tt_special=''
        self.salary=''
    def __str__(self):
        # str_data=super().__str__()
        # return " Technical Trainer Special = {0} , Salary = {1}".format(self.tt_special,self.salary)+str_data
        return super().__str__()+ " , Technical Trainer Special = {0} , Salary = {1}".format(self.tt_special,self.salary)
    def add(self):
        super().add()
    def search(self,emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                self.tt_special=e.tt_special
                self.salary=e.salary
                super().search(emp_id)
                return True
        return False
    def update(self,emp_id):
        for e in EMP.list_emp:
            if e.id==emp_id:
                e.tt_special=self.tt_special
                e.salary=self.salary
                super().update(emp_id)
                return True
        return False
    def delete(self, emp_id):
        return super().delete(emp_id)
# BLL code ends here
# PL code starts here
def show_all_employee():
    for e in EMP.list_emp:
        print(e)
while(True):
    print("1.Add\n2.Search\n3.Update\n4.Delete\n5.Show All Employee\n0.Exit")
    ch=input("Enter Your Choice : ")
    if ch=='1':
        print("1.Add Director\n2.Add Manager\n3.Add Technical Trainer")
        ch=input("Enter Your Choice : ")
        if ch=='1':
            # write code to add Director
            ob_dir=DIR()
            ob_dir.type='Dir'
            ob_dir.id=int(input("Enter Id : "))
            ob_dir.name=input("Enter Name : ")
            ob_dir.dir_special=input("Enter Direcor Special : ")
            ob_dir.share=input("Enter Share of Director : ")
            ob_dir.add() # Director class ke add method ko call krega
            print("Director Added Successfully.")
        elif ch=='2':
            # write code to add Manager
            ob_mgr=MGR()
            ob_mgr.type='Mgr'
            ob_mgr.id=int(input("Enter Id : "))
            ob_mgr.name=input("Enter Name : ")
            ob_mgr.mgr_special=input("Enter Manager Special : ")
            ob_mgr.incentive=input("Enter Incentive of Manager : ")
            ob_mgr.add() # Manager class ke add method ko call krega
            print("Manager Added Successfully.")
        elif ch=='3':
            # write code to add Technical Trainer
            ob_tt=TT()
            ob_tt.type='TT'
            ob_tt.id=int(input("Enter Id : "))
            ob_tt.name=input("Enter Name : ")
            ob_tt.tt_special=input("Enter Technical Trainer Special : ")
            ob_tt.salary=input("Enter Salary of Technical Trainer : ")
            ob_tt.add() # Technical Trainer class ke add method ko call krega
            print("Technical Trainer Added Successfully.")
    elif ch=='2':
        # write code to search Employee
        emp_id=int(input("Enter Id : "))
        type=EMP.get_employee_type_by_id(emp_id)
        if type=='Dir':
            ob_dir=DIR()
            ob_dir.search(emp_id)
            print(ob_dir)
        elif type=='Mgr':
            ob_mgr=MGR()
            ob_mgr.search(emp_id)
            print(ob_mgr)
        elif type=='TT':
            ob_tt=TT()
            ob_tt.search(emp_id)
            print(ob_tt)
        else:
            print("Id Not Found.")
    elif ch=='3':
        # write code to update Employee
        emp_id=int(input("Enter Id : "))
        type=EMP.get_employee_type_by_id(emp_id)
        if type=='Dir':
            ob_dir=DIR()
            ob_dir.type='Dir'
            # ob_dir.id=int(input("Enter Id For Update : "))
            ob_dir.name=input("Enter Name For Update : ")
            ob_dir.dir_special=input("Enter Direcor Special For Update : ")
            ob_dir.share=input("Enter Share of Director For Update : ")
            check=ob_dir.update(emp_id) # Director class ke add method ko call krega
            if check==False:
                print("Id Not Found.")
            else:
                print("Director Updated Successfully.")
        elif type=='Mgr':
            ob_mgr=MGR()
            ob_mgr.type='Mgr'
            # ob_mgr.id=int(input("Enter Id For Update : "))
            ob_mgr.name=input("Enter Name For Update : ")
            ob_mgr.mgr_special=input("Enter Manager Special For Update : ")
            ob_mgr.incentive=input("Enter Incentive of Manager For Update : ")
            check=ob_mgr.update(emp_id) # Manager class ke add method ko call krega
            if check==False:
                print("Id Not Found.")
            else:
                print("Manager Updated Successfully.")
        elif type=='TT':
            ob_tt=TT()
            ob_mgr.type='TT'
            # ob_tt.id=int(input("Enter Id For Update : "))
            ob_tt.name=input("Enter Name For Update : ")
            ob_tt.tt_special=input("Enter Technical Trainer Special For Update : ")
            ob_tt.salary=input("Enter Salary of Technical Trainer For Update : ")
            check=ob_tt.update(emp_id) # Technical Trainer class ke add method ko call krega
            if check==False:
                print("Id Not Found.")
            else:
                print("Technical Trainer Updated Successfully.")
        else:
            print("Id Not Found.")
    elif ch=='4':
        # write code to delete Employee
        emp_id=int(input("Enter Id : "))
        type=EMP.get_employee_type_by_id(emp_id)
        if type=='Dir':
            ob_dir=DIR()
            check=ob_dir.delete(emp_id)
            if check==False:
                print("Id Not Found.")
            else:
             print("Director Deleted Successfully.")
        elif type=='Mgr':
            ob_mgr=MGR()
            check=ob_mgr.delete(emp_id)
            if check==False:
                print("Id Not Found.")
            else:
                print("Manager Deleted Successfully.")
        elif type=='TT':
            ob_tt=TT()
            check=ob_tt.delete(emp_id)
            if check==False:
                print("Id Not Found.")
            else:
                print("Technical Trainer Deleted Successfully.")
        else:
            print("Id Not Found.")
    elif ch=='5':
        # write code to show all Employee
        show_all_employee()
    elif ch=='0':
        break
# PL code ends here