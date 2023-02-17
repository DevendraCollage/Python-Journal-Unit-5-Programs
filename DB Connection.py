# import sql module for database connection
import mysql.connector as mysql

# Open Database Connection
db = mysql.connect(host="localhost", user="root",
                   password="", database="TEST")

# Create cursor object using cursor() method
cursor = db.cursor()

# SQL Query
sql = "SELECT VERSION()"

# Fetch Row From Database
res = cursor.fetchone()
print("Database Version : %s " % res)

# Execute SQL Query
cursor.execute(sql)

# Close Database Connection
db.close()
