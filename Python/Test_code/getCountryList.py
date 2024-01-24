import mysql.connector

def getCountryList():

    mydatabase=mysql.connector.connect(
        host="localhost",
	user="root",
	password="admin@123",
	database="world"
	)
	
    cur = mydatabase.cursor()
    sql = 'select name from country'
    cur.execute(sql)
    records = cur.fetchall()
    print("Total number of rows in table: ", cur.rowcount)
    print("\nPrinting each row")
	
    for row in records:
        return row[0]
