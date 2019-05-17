import pymysql

conn=pymysql.connect(user="root",password="root",host="localhost",database="gb8am")

cur=conn.cursor()
print(cur)

# cur.execute("create database gb8am")
# cur.execute("create table std_details(std_name varchar(20),std_mobile varchar(10),std_email varchar(25))")
# cur.execute("insert into std_details(std_name,std_mobile,std_email) values('rajesh','8298292822','rajesh@gmail.com')")
# cur.execute('update std_details set std_mobile="920222282" where std_name="rajesh"')
cur.execute('drop database gb8am')
conn.commit()
conn.close()