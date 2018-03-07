import MySQLdb
import mysql.connector

db = MySQLdb.connect(host = 'localhost',
                     user = 'root',
                     passwd = 'gagankainth',
                     db = 'one')

cur = db.cursor()

print("1. Show the Database.")
print("2. Insert value into the Database.")
print("3. Delete values from the Database.\n")
x = int(input("Enter your choice: "))

if x == 1:
    cur.execute("select * from new")
    for d in cur.fetchall():
        print(d)

if x == 2:
    i = int(input("Enter customer id: "))
    na = input("Enter customer name: ")
    ph = input("Enter customer phone: ")
    cmd = "insert into new values(%i , '%s', '%s')"
    # cmd = "insert into new values(" + str(i) + "," + na + "," + ph + ")"
    cmd = cmd % (i, na , ph)
    print(cmd)
    try:
        cur.execute(cmd)
        cur.execute("select * from new")
        for d in cur.fetchall():
            print(d)
    except:
        print("Cannot insert.")

db.commit()
cur.close()
db.close()
