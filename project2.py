'''
Created on 11-Dec-2017

@author: rahul
'''
import sys
import MySQLdb
from gi.overrides.keysyms import cursor, Begin
from unicodedata import numeric
from pickle import NONE

# Open database connection
db = MySQLdb.connect("localhost","root","admin","Sample" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
'''
cursor.execute(""" create table employee1(
employeeId numeric(5)  auto_increment primary key,employeeName nvarchar(20),
typeofEmployee nvarchar(1),
telephoneno numeric(10),
skillset nvarchar(50),
yearsofExperience numeric(3),
basicPay numeric(5,2),
allowence numeric(5,2),
salary numeric(5,2),check(typeofEmployee='P' or typeofEmployee='c')
""")
'''
#cursor.execute(""" alter table employee1  auto_increment=1000""")

#cursor.execute(""" create table project(
#projectId numeric(5),
#employeeId numeric(5) references employee1(employeeId),
#projectTechnology varchar(50) check(projectTechnology='jee' or projectTecnology='ms'))""")

#cursor.execute(""" create table consultant(
#emloyeeId numeric(5) references employee1(employeeId),
#noofHrs numeric(5,2),
#payRateprHr numeric(5,2),
#consultantfee numeric(5,2))
#""")
'''cursor.execute(""" create table project(
projectId numeric(5),
employeeId numeric(5) references employee1(employeeId),
projectTechnology varchar(50) check(projectTechnology='jee' or projectTechnology='ms'))
""")'''


'''cursor.execute("""create table consultant(
employeeId numeric(5) references employee1(employeeId),
noofHrs numeric(10,2),
payRateprHr numeric(10,2),
consultantfee numeric(10,2))
""")'''

'''cursor.execute("""create procedure cons(IN employeeId numeric(5),
IN noofHrs numeric(5,2),IN payRateprHr numeric(5,2),IN consultantfee numeric(5,2))
BEGIN
insert into consultant(employeeId,noofHrs,payRateprHr,consultantfee) values(employeeId,noofHrs,payRateprHr,consultantFee);
commit;
end;""")'''

'''cursor.execute("""create procedure prj(IN  projectId varchar(10),IN employeeId numeric(5),
IN projectTechnology varchar(10))
BEGIN
insert into project(projectId,employeeId,projectTechnology) values(projectId,employeeId,projectTechnology);
commit;
END;""")'''

class Employee:
    global count
    counter=1000
    def __init__(self,employeeName,typeofEmployee,telephoneno,skillset):
        Employee.counter = Employee.counter+1
        self.__employeeId=Employee.counter
        self.__employeeName=employeeName
        self.__typeofEmployee=typeofEmployee
        self.__telephoneno=telephoneno
        self.__skillset=skillset
        

    def setemployeeName(self, empname):
        self.__employeeName = empname
    
    def settypeofEmployee(self, emptype):
        self.__typeofEmployee = emptype

    def settelephoneno(self, emptelephoneno):
        self.__telephoneno = emptelephoneno
        
    def setskillset(self, empskillset):
        self.__skillset = empskillset
        
    def getemployeeId(self):
        return self.__employeeId

    def getemployeeName(self): 
        return self.__employeeName
    
    def gettypeofEmployee(self): 
        return self.__typeofEmployee
    
    def gettelephoneno(self): 
        return self.__telephoneno
    
    def getskillset(self): 
        return self.__skillset
    def validatetelephoneno(self):
        #pass # code to be implemented
        
        string=str(self.__telephoneno)
        if(string[0]=='1' and len(string)==10):
            return True
        else:
            return False
        
            
class Salary:
    basicPay=5000
    def calculatesalary(self):
        return 0   
    

class PermanentEmployee(Employee,Salary,object):
    def __init__(self,employeeName,typeofEmployee,telephoneno,skillset,yearsofExperience):
        super(PermanentEmployee,self).__init__(employeeName,typeofEmployee,telephoneno,skillset)
        self.__yearsofExperience=yearsofExperience
    def setyearsofExperience(self, yrsofexp):
        self.__yearsofExperience =yrsofexp 
            
    def getyearsofExperience(self): 
        return self.__yearsofExperience

    def validatetypeofEmployee(self):
        if(self.gettypeofEmployee()=='P' or self.gettypeofEmployee()=='p'or self.gettypeofEmployee()=='c' or self.gettypeofEmployee()=='C')  is True:
            return True
        else:
            return False
           
        
            
        #pass # code to be implemented
    
    def calculatesalary(self):

        s1=Salary()
        if self.validatetelephoneno() and self.validatetypeofEmployee() is True:
            if self.__yearsofExperience>=15:
                return (s1.basicPay*0.2)
            elif self.__yearsofExperience>=10 or self.__yearsofExperience<15:
                return(s1.basicPay*0.1)
            elif self.__yearsofExperience>=5 or self.__yearsofExperience<5:
                return (s1.basicPay*0.05)

            # pass # code to be implemented
    
class Consultant(Employee,Salary,object):
    
    def __init__(self,employeeName,typeofEmployee,telephoneno,skillset,noofHrs):
        super(Consultant,self).__init__(employeeName,typeofEmployee,telephoneno,skillset)
        self.__noofHrs=noofHrs
    
    def setnoofHrs(self, noofhrs):
        self.__noofHrs =noofhrs 
            
    def getnoofHrs(self): 
        return self.__noofHrs
    def consultantskill(self):
        if self.consultantskill=='jee' or self.consultantskill=='ms':
            return True
        else:
            False
    
    def validatetypeofEmployee(self):
        if(self.typeofEmployee=='C' or self.typeofEmployee=='c'):
            return True
        else:
            return False
        

    def calculatesalary(self):
        
        if (self.validatetelephoneno() and Employee.gettypeofEmployee(self)=='c') is True:
            if self.getskillset()=='jee':
                return self.__noofHrs*500
            elif self.getskillset()=='ms':
                return self.__noofHrs*350
            else:
                return self.__noofHrs*250
          
        #pass # code to be implemented
class Project:
    counter=5000
    
    def __init__(self):
        Project.counter = Project.counter+1
        self.__projectId='P' + str(Project.counter)
        self.__projectTechnology=['jee','ms']

    
    def setemployee(self, employee):
        self.__employoee =employee
            
    def getprojectId(self): 
        return self.__projectId
       
    def getemployee(self): 
        return self.__employoee
    
    def setprojectTechnology(self,projecttech):
        self.__projectTechnology=projecttech
            
    def getprojectTechnology(self):
        return self.__projectTechnology
    
    def allocateproject(self,pobj):
        if (pobj.validatetypeofEmployee()and pobj.validatetelephoneno()) is True:
            print("yes")
            if (pobj.getskillset() in self.__projectTechnology)is True:
                pid=self.__projectId
                eligible="you are allocated for project with id is"+pid
                print(eligible)
                return True
               
                
            else:
                eligible="you are not allocated for project"
                print(eligible)
                return False
    
            
       
                
            #pass  # code to be implemented
      
'''objcust = Employee()
print("Employee Id: ", objcust.getemployeeId())

objcust2 = Employee()
print("Employee Id: ", objcust2.getemployeeId())'''

class Demo:
    n=0
    ch='n'
    
    def employeeoptions(self):
        
        print("hai")
        print("******************************")
        print("  Employee Management System  ")
        print("******************************")
        print("1. Add New Employee")
        print("2. Modify Employee")
        print("3. Delete Employee")
        print("4. View Employee By ID")
        print("5. View All")
        print("6. Exit")
        n=int(input("Select your choice"))
        if(n==1):
            print("haibye")
            dobj.insertrecord()
            dobj.gotooptions()
        elif n==2:
            dobj.updaterecord()
        elif n==3:
            dobj.deleterecord()
        elif n==4:
            dobj.viewbyid()
        elif n==5:
            dobj.viewall()
        elif n==6:
            print("Thank You!!!")
            sys.exit
    



    def insertrecord(self):
        
        employeeName=raw_input("enter employee name")
        typeofEmployee=raw_input("enter type of employee")
        telephoneno=input("enter telephone number")
        skillset=raw_input("enter skillset")
        yearsofExperience=input("enter yearsofExprience")
        noofHrs=input("enter noofhrs")
        consultantfee=input("enter consultant fee")
        if skillset=='jee':
            payRateprHr=500
        elif skillset=='ms':
            payRateprHr=350
        else:
            payRateprHr=250 
            
        
        probj=Project()
        pobj=PermanentEmployee(employeeName,typeofEmployee,telephoneno,skillset,yearsofExperience)
        cobj=Consultant(employeeName,typeofEmployee,telephoneno,skillset,noofHrs)
        basicPay=pobj.basicPay
        salary=NONE
        if typeofEmployee=='p':
            allowence=pobj.calculatesalary()
            salary=basicPay+allowence
            print("permanent employee salary is:%d"%salary)
            if pobj.validatetelephoneno() and pobj.validatetypeofEmployee() is True:    
                s=""" insert into employee1(employeeName,typeofEmployee,telephoneno,skillset,yearsofExperience,basicPay,allowence,salary)
                values('%s','%s','%s','%s','%s','%s','%s','%s')"""%(employeeName,typeofEmployee,telephoneno,skillset,yearsofExperience,basicPay,allowence,salary)
            
                cursor.execute(s)
                db.commit()
                cursor.execute("""select employeeId from employee1 where employeeName=%s and telephoneno=%s""",(employeeName,telephoneno))
                employeeId=cursor.fetchall()
               
                if(probj.allocateproject(pobj)is True):
                    projectId=probj.getprojectId()
                    projectTechnology=skillset
                    cursor.callproc('prj',[projectId,employeeId,projectTechnology])
                    db.commit()
           
        elif typeofEmployee=='c':
            allowence=cobj.calculatesalary()
            salary=allowence
            if cobj.validatetelephoneno() is True:    
                s=""" insert into employee1(employeeName,typeofEmployee,telephoneno,skillset,yearsofExperience,basicPay,allowence,salary)
                values('%s','%s','%s','%s','%s','%s','%s','%s')"""%(employeeName,typeofEmployee,telephoneno,skillset,yearsofExperience,basicPay,allowence,salary)
                cursor.execute(s)
                db.commit()
                print("consultant salry is:%d"%salary)
                
                cursor.execute("""select employeeId from employee1 where employeeName=%s and telephoneno=%s""",(employeeName,telephoneno))
                employeeId=cursor.fetchall()
                
                cursor.callproc('cons',[employeeId,noofHrs,payRateprHr,consultantfee])
                if(probj.allocateproject(pobj)is True):
                    projectId=probj.getprojectId()
                    projectTechnology=skillset
                    cursor.callproc('prj',[projectId,employeeId,projectTechnology])
                    db.commit()
        else:
            print("invalid type of employee")
   
        
        #pass  #Database code to insert employee details 
    def updaterecord(self):
        input_col_name=raw_input("enter  colmn name")
        set_col_name=raw_input("enter set colmn")
        changed_col_name=input("enter id which you want to modify")
        if("employeeName"==input_col_name):
            cursor.execute("""update employee1 set employeeName=%s where employeeId=%s """,(set_col_name,changed_col_name))
            db.commit()
        elif("typeofEmployee"==input_col_name):
            cursor.execute(""" update employee1 set typeofEmployee=%s where employeeId=%s""",(set_col_name,changed_col_name))
            db.commit()
        elif ("telephoneno"==input_col_name):
            cursor.execute(""" update employee1 set telephoneno=%s where employeeId=%s""",(set_col_name,changed_col_name))
            db.commit()
        elif("skilllset"==input_col_name):
            cursor.execute(""" update employee1 set skillset=%s where employeeId=%s""", (set_col_name,changed_col_name))
            db.commit()
        elif("yearsofExperience"==input_col_name):
            cursor.execute(""" update employee1 set yearsofExperience=%s where employeeId=%s""",(set_col_name,changed_col_name))
            db.commit()
        else:
            print("invalid input")
        
        #Database code to update employee details 
    def deleterecord(self):
        deleterec=raw_input("enter rec u want to delt")
        cursor.execute("""delete from employee1 where employeeId=%s"""%deleterec)
        db.commit()
        
        #pass #Database code to delete employee details 
    def viewbyid(self):
        viewId=input("enter id for view")
        cursor.execute("select * from employee1 where employeeId=%d"%viewId)
        print(cursor.fetchall())
        db.commit()
        pass #Database code to view employee details by id
    def viewall(self):
        n=int(input("select your choice"))
        if n==1:
            cursor.execute("""select * from employee1""")
        if n==2:
            cursor.execute("""select * from consultant""")
        if n==3:
            cursor.execute("""select * from project""")
        print(cursor.fetchall())
        db.commit()
        
        
        pass #Database code to view all employees 
    
    def gotooptions(self):
        ch=raw_input("Do you wish to continue(y/n)")
        if(ch=='y' or ch=='Y'):
            Demo.employeeoptions(self)
            
    
dobj=Demo()
dobj.employeeoptions()
dobj.gotooptions()
        
print(cursor.fetchall())

db.close()