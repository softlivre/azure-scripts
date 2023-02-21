# connect to remote sql server and query some data

from remoteCredentials import *
import pyodbc

cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};Server='+server+';DATABASE='+database+';ENCRYPT=no;UID='+username+';PWD='+password+';Trusted_Connection=no;')

cursor = cnxn.cursor()

# connect to host and query the version
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()

# connect to host and query some data
cursor.execute("select top(5) ProductID, Name, Color from SalesLT.Product order by ProductID")
for row in cursor.fetchall():
    print(row)

