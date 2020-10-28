import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="myml"
)
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE myml");

# mycursor.execute("""CREATE TABLE User
#                                       (
#                                           ID INT AUTO_INCREMENT PRIMARY KEY,
#                                           Name VARCHAR(30),
#                                           Lastname VARCHAR(30),
#                                           Age INT,
#                                           Date DATE,
#                                           Reg_Date DATE,
#                                           Password VARCHAR(50),
#                                           Gender VARCHAR(20)
#                                     )
#                 """)
                

sql =   (""" INSERT INTO user(Name,Lastname,Age,Date,Reg_Date,Password,Gender)
             VALUES(%s,%s,%s,%s,%s,%s,%s)
        """)
        
val = [('Lado','nik',21,'01.02.2012','01.02.2012','as','sss'),
       ('Lado','nik',21,'01.02.2012','01.02.2012','as','sss')]
#mycursor.execute(sql,val)
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

# mycursor.execute("SELECT Age, Date, Reg_date, Gender FROM users LIMIT 3")

# mycursor.execute("SELECT * FROM users LIMIT 2")

# mycursor.execute("SELECT * FROM users WHERE Id>1 AND Id<4")

# mycursor.execute("SELECT * FROM users WHERE Id>2 OR Id>=4")

# mycursor.execute("SELECT * FROM users WHERE Date=2014-07-04")

# mycursor.execute("SELECT * FROM users WHERE Date>'2014-07-04'")

# mycursor.execute("SELECT * FROM users WHERE Date>'2014-06-04' AND Date<'2014-07-04'")

# mycursor.execute("SELECT * FROM users WHERE Age>=10 AND Age<=18")
myresult = mycursor.fetchall()
                                     
                        