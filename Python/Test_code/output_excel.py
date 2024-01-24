from pymysql import*
from openpyxl import Workbook
import mysql.connector

conn=mysql.connector.connect(
   host="localhost",
   user="root",
   password="admin@123",
   database="world"
)

print(conn)

cur = conn.cursor()
sql = 'select code, name, continent, region from country'
cur.execute(sql)
records = cur.fetchall()

wb = Workbook(write_only=True)
country_ws = wb.create_sheet("Country")
# write header
country_ws.append(["Code", "Country Name", "Continent", "Region"])

# write data
for country in records:
    country_code = country[0]
    country_name = country[1]
    continent = country[2]
    region = country[3]
    country_ws.append([country_code, country_name, continent, region])

wb.save("Country.xlsx")

conn.close()