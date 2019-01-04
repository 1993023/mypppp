'''
Created on 07-Dec-2017

@author: rahul
'''
import sys
import MySQLdb
from gi.overrides.keysyms import cursor, Begin

# Open database connection
db = MySQLdb.connect("localhost","root","admin","Sample" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

'''cursor.execute(""" create table Nemployee(
employeeId numeric(5) auto_increament PRIMARY KEY,
employeeName varchar(20),
CHECK(typeofEmployee='p' or typeofEmployee='c'),
telephoneno numeric(10),
skillset varchar(50),
yearsofExperience numeric(3),
basicpay numeric(5,2),
allowence numeric(5,2),
salary numeric(5,2)""")

cursor.execute(""" alter table Nemployee add auto_increament=1000""")

cursor.execute("""create table Nproject(
projectId varchar(5),
employeeid numeric(5).
CHECK(projectTechnology='JEE' OR projectTechnology='MS'),
FOREIGN KEY fk_emp(employeeId) REFERENCES Nemployee(employeeId) ON UPDATE CASCADE)
""")

cursor.execute(""" create table Nconsultant(
employeeId numeric(5),
NoofHrs numeric(5,2),
payRatePerHr numeric(5,2),
consultantFee numeric(5,2)
FOREIGN KEY fk_emp(employeeId) REFERENCES Nemployee(employeeId) ON UPDATE CASCADE)
""")'''
 
class Employee:
    global count
    count=1000
    def __init__(self,employeename,typeofemployee,telephoneno,skillset):
        Employee.counter = Employee.counter+1
        self.__employeeid=Employee.counter
        self.employeename=employeename
        self.typeofemployee=typeofemployee
        self.telephoneno=telephoneno
        self.skillset=skillset
        

    def setemployeename(self, empname):
        self.__employeename = empname
    
    def settypeofemployee(self, emptype):
        self.__typeofemployee = emptype

    def settelephoneno(self, emptelephoneno):
        self.__telephoneno = emptelephoneno
        
    def setskillset(self, empskillset):
        self.__skillset = empskillset
        
    def getemployeeid(self):
        return self.__employeeid

    def getemployeename(self): 
        return self.__employeename
    
    def gettypeofemployee(self): 
        return self.__typeofemployee
    
    def gettelephoneno(self): 
        return self.__telephoneno
    
    def getskillset(self): 
        return self.__skillset
    def validatetelephoneno(self,telephoneno):
        #pass # code to be implemented
        self.telephoneno=telephoneno
        string=str(telephoneno)
        for i in range(0,len(string)):
            if(string[0]=="1" and len(string)=="10"):
                return True
            else:
                return False
        
            
class Salary:
    basicpay=5000
    def calculatesalary(self):
        return 0   
    

class PermanentEmployee(Employee,Salary):
    def __init__(self,employeename,typeofemployee,telephoneno,skillset,yearsofexperience):
        super().__init__(employeename,typeofemployee,telephoneno,skillset)
        self.__yearsofexperience=yearsofexperience
    def setyearsofexperience(self, yrsofexp):
        self.__yearsofexperience =yrsofexp 
            
    def getyearsofexperience(self): 
        return self.__yearsofexperience

    def validatetypeofemployee(self,employeeid,typeofemployee):
        self.employeeid=employeeid
        typeofemployee=typeofemployee
        if(self.typeofemployee=='P' or self.typeofemployee=='p'):
            return True
        else:
            return False
        
            
        #pass # code to be implemented
    
    def calculatesalary(self):
        p1=PermanentEmployee()
        s1=Salary()
        if p1.validatephoneno()=='True' and p1.validatetypeofemployee()=='True':
            if p1.yearsofexperience>=15:
                Salary=s1.basicpay+(s1.basicpay*0.2)
            if p1.yearsofexperience>=10 or p1.yearsofexperience<15:
                Salary=s1.basicpay+(s1.basicpay*0.1)
            if p1.yearsofexperience>=5 or p1.yearsofexperience<5:
                Salary=s1.basicpay+(s1.basicpay*0.05)
            return Salary
               
        else:
            print("telephoneno or typeofemployee is not valid")
                
                
                
            
       # pass # code to be implemented
    
class Consultant(Employee,Salary):
    
    def __init__(self,employeename,typeofemployee,telephoneno,skillset,noofhours):
        super().__init__(employeename,typeofemployee,telephoneno,skillset)
        self.__noofhours=noofhours
    
    def setnoofhours(self, noofhrs):
        self.__noofhours =noofhrs 
            
    def getnoofhours(self): 
        return self.__noofhours
    def consultantskill(self):
        if self.consultantskill=='jee' or self.consultantskill=='ms':
            return True
        else:
            False

    def calculatesalary(self):
        c1=Consultant()
        
        if c1.validatetelephoneno()==True and c1.typeofemployee()=='c' and c1.consulatntskill==True:
            if c1.consulatntskill=='jee':
                payrateperhr=500
            if c1.consulatntskill=='ms':
                payrateperhr=350
            else:
                payrateperhr=250
        else:
            print("invalid ")
                
            
        
                
        #pass # code to be implemented
class Project:
    counter=5000
    
    def __init__(self):
        Project.counter = Project.counter+1
        self.__projectidid='P' + Project.counter

    
    def setemployee(self, employee):
        self.__employoee =employee
            
    def getprojectid(self): 
        return self.__projectid
       
    def getemployee(self): 
        return self.__employoee
    
    def setprojecttechnology(self,projecttech):
        self.__projecttechnology=projecttech
            
    def getprojecttechnology(self):
        return self.__projecttechnology
    
    def allocateproject(self):
        emp=Project()
        eligible=""
        projecttecnology=['jee','ms']
        if emp.typeofemployee=='p' or emp.typeofemployee=='c':
            # pass  # code to be implemented
      
'''objcust = Employee()
print("Employee Id: ", objcust.getemployeeid())

objcust2 = Employee()
print("Employee Id: ", objcust2.getemployeeid())'''

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
        
        #pass  #Database code to insert employee details 
    def updaterecord(self):
        
        #pass  #Database code to update employee details 
    def deleterecord(self):
        
        #pass #Database code to delete employee details 
    def viewbyid(self):
        
        #pass #Database code to view employee details by id
    def viewall(self):
        
        
       # pass #Database code to view all employees 
    
    def gotooptions(self):
        ch=input("Do you wish to continue(y/n)")
        if(ch=='y' or ch=='Y'):
            Demo.employeeoptions(self)
            
    
dobj=Demo()
dobj.employeeoptions()
dobj.gotooptions()
        
        
    
   