import MySQLdb

db = MySQLdb.connect(host = 'localhost',
                     user = 'root',
                     passwd = 'gagankainth',
                     db = 'one')

cd = db.cursor()

try:
    cd.execute("insert into new values(2, 'Bill Clinton', 9898989898)")
    print("1 row changed")
except:
    print("Can't insert")

cd.execute("SELECT * FROM new")

for row in cd.fetchall():
    print(row)

db.close()