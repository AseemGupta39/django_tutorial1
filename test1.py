import mysql.connector
from datetime import datetime

now1 = datetime.now()

mydb = mysql.connector.connect(
  host="localhost",
  user="gan",
  password="1234",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (firstname, lastname, MobileNo, DATE_OF_PURCHASE, TIME_OF_PURCHASE) VALUES (%s, %s, %d, %s, %s)"
fn = input("firstname: ")
ln = input("lastname: ")
mn = int(input("mobile no: "))
val = (fn,ln,mn,f"""{now1.strftime("%Y-%m-%d")}""",now1.strftime("%H:%M:%S"))

print(sql,val)
mycursor.execute(sql, val)


mycursor.execute("SELECT max(id) FROM customers")

myresult = mycursor.fetchone()

condition = True
while condition:
    id = myresult
    med = int(input("med code: "))
    qty = int(input("qty: "))
    renewal_time = int(input("no of days for renewal"))
    loop = input("enter y to continue or any thing to stop")
    sql = "INSERT INTO customer_order (id,Medicine_code,qty,RENEWAL) VALUES (%d, %d, %d, %d)"
    val = (id,med,qty,renewal_time)
    print(val)

    mycursor.execute(sql, val)

    if loop == "y":
        condition = True
    else:
        condition = False
    
mydb.commit()

print(mycursor.rowcount, "record inserted.")

##### f"""{now1.strftime("%Y-%m-%d")}"""
# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY,firstname VARCHAR(20) NOT NULL,lastname VARCHAR(20),MobileNo INT(10) NOT NULL,DATE_OF_PURCHASE DATE,TIME_OF_PURCHASE TIME,CONSTRAINT UC_Person UNIQUE (firstname,MobileNo))")
## mycursor.execute("CREATE TABLE customer_order (id INT NOT NULL REFERENCES customers(id) ,DATE_OF_PURCHASE DATE,TIME_OF_PURCHASE TIME,Medicine VARCHAR(30),qty TINYINT,RENEWAL INT")

#### INSERT INTO customers (firstname, lastname, MobileNo, DATE_OF_PURCHASE, TIME_OF_PURCHASE) VALUES ('Aseem', 'Gupta', 8005502214, '2023-05-04', '23:28:55');
