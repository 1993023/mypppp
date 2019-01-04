import sys
import MySQLdb
from gi.overrides.keysyms import cursor, Begin
from unicodedata import numeric

# Open database connection
db = MySQLdb.connect("localhost","root","admin","Sample" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
'''
cursor.execute(""" create table employee1(
employeeId mediumint(5)  not null auto_increment primary key,
employeeName nvarchar(20),
typeofEmployee nvarchar(1),
telephoneno numeric(10),
skillset nvarchar(50),
yearsofExperience numeric(3),
basicPay numeric(5,2),
allowence numeric(5,2),
salary numeric(5,2),check(typeofEmployee='P' or typeofEmployee='c'))
""")'''
#cursor.execute(""" alter table employee1  auto_increment=1000""")
