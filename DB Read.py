# Import sql module for database connection
import mysql.connector as mysql

# Open Database Connection
db = mysql.connect(host="localhost", user="root", password="", database="TEST")

# Create cursor object using cursor() method
cursor = db.cursor()

# Create SQL Query
sql = "SELECT * FROM STUDENT"

# Execute SQL Query
res = cursor.execute(sql)

# Fetching All Row From the Database
data = cursor.fetchall()
for x in data:
    print(x)

# Close Database Connection
db.close()
