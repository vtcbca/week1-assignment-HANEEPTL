Write a python script to perform CRUD operation on following table of "ESM.db" database.
Employee ( eid, ename, dept, basic, branch). eid must be primary key.
Department : Account, Inventory, IT, HR.
Peform Following Operation.

1. Create table

import sqlite3 as sq
conn=sq.connect('c:\sqlite\sqlite3\esm.db')
cursor=conn.cursor()
query='''CREATE TABLE Employee101(eid int PRIMARY KEY,ename text,dept text,basic int,branch text)'''
cursor.execute(query)


2. Insert 5 Records directly, 5 records using tuple and 5 records using taking input from user

#direct record
q="INSERT INTO Employee101
VALUES(1,'Hanee','HR',50000,'Surat'),(2,'Heer','IT',50000,'Surat'),(3,'Riya','Inventory',15000,'Bardoli'),(4,'deep','Accountant',60000,'Baroda'),(5,'rinkal','Accountant',50000,'Baroda')"
cursor.execute(q)

#tuple format
q1=[(6,'mansi','HR',30000,'Bardoli'),(7,'hardik','IT',50000,'Navsari'),(8,'Shiv','IT',80000,'Pune'),(9,'divya','HR',50000,'Surat'),(10,'Pooja','Inventory',50000,'Bharuch')]
cursor.executemany("INSERT INTO Employee101 VALUES (?, ?, ?, ?, ?)",q1)

#user input
for i in range(5):
    eid = int(input("Enter employee ID: "))
    ename = input("Enter employee name: ")
    dept = input("Enter employee department: ")
    basic = int(input("Enter employee basic salary: "))
    branch = input("Enter employee branch: ")
    cursor.execute("INSERT INTO Employee101 VALUES (?, ?, ?, ?, ?)", (eid, ename, dept, basic, branch))


3. Update records who are from "Surat" branch with increment in salary 10%.
cursor.execute("UPDATE Employee101 SET basic=(basic+basic*0.01) WHERE branch='Surat'")


4. Print All records.
cursor.execute("SELECT * FROM Employee101")
for i in cursor.fetchall():
    print(i)


5. Print records where dept is "HR" and "IT".
cursor.execute("SELECT * FROM Employee101 WHERE dept IN('IT','HR')")
for i in cursor.fetchall():
    print(i)


6. Print records in sorting order of department.
cursor.execute("SELECT * FROM Employee101 ORDER BY dept")
for i in cursor.fetchall():
    print(i)

cursor.execute("SELECT * FROM Employee101 ORDER BY dept desc")
for i in cursor.fetchall():
    print(i)


7. Print records where basic is >6000.
cursor.execute("SELECT * FROM Employee101 WHERE basic>6000")
for i in cursor.fetchall():
    print(i)


8. Print records whrere employee name second character is "r".
cursor.execute("SELECT * FROM Employee101 WHERE ename LIKE '_r%'")
for i in cursor.fetchall():
    print(i)


9. Grouping record of employee who are from "Account" and "Inventory".
cursor.execute("SELECT dept, COUNT(*) AS NumOfRecords FROM Employee101 WHERE dept IN ('Accountant', 'Inventory') GROUP BY dept")
for i in cursor.fetchall():
    print(i)


10. Print all records based on branch name in descending order.
cursor.execute("SELECT * FROM Employee101 ORDER BY branch desc")
for i in cursor.fetchall():
    print(i)
