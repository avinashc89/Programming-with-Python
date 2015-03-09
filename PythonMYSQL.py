'''
Created on Oct 29, 2014

@author: Avinash
'''
import MySQLdb

db = MySQLdb.connect("localhost","root","mysql","pydev")
statement = db.cursor()

#insert into database
statement.execute("insert into customer(name,sex,birth,age) values('lekha','F',str_to_date('18-7-1990','%d-%m-%Y'),cust_age(str_to_date('18-7-1990','%d-%m-%Y')))")

#update database
statement.execute("update customer set name ='avinash2' where custid=104")

#retrieve from database
statement.execute("select * from customer")
results =  statement.fetchall()
for row in results:
    id = row[0]
    name = row[1]
    sex = row[2]
    birth = row[3]
    age = row[4]
    print "[%s,%s,%s,%s,%s]" %(id, name, sex, birth, age )

db.commit()
db.close()