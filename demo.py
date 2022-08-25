import mysql.connector as mydb

mydb = mydb.connect(host="localhost", user="root", password="taniyaand123", database="pythontest")

cursor = mydb.cursor()
#creating the table
cursor.execute("create table student12( name varchar(20), sub varchar(20))")

#inserting values to the table
query="insert into student12(name,sub) values(%s,%s)"
values=[("aman","english"),("taniya","hindi"),("neha","maths"),("gautam","science")]

cursor.executemany(query,values)
mydb.commit()
print(cursor.rowcount, "record inserted.")

#fetching the records
cursor.execute("select * from student12")
result=cursor.fetchall()

print(result)

#updating table

sql="update student12 set sub = 'g.k' where sub='english'"
cursor.execute(sql)
print(cursor.rowcount,"record(s) affected")

#new record
cursor.execute("select * from student12")
result=cursor.fetchall()

print(result)
mydb.close()
