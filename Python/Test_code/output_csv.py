import mysql.connector

mydatabase=mysql.connector.connect(
   host="localhost",
   user="root",
   password="admin@123",
   database="world"
)

print(mydatabase)

cur = mydatabase.cursor()
sql = 'select * from country'
cur.execute(sql)
records = cur.fetchmany(3)

f = open('country.txt', 'w')

print("Total number of rows in table: ", cur.rowcount)

print("\nPrinting each row")

with open('country.txt', 'w') as f:
    for row in records:
        f.write("\"%s\"," % str(row[0]))
        f.write("\"%s\"" % str(row[1]))
        f.write("\n")
    
f.close()
