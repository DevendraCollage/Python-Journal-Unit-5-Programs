# Import sql module for database connection
import mysql.connector as mysql

# Open Database Connection
db = mysql.connect(host="localhost", user="root", password="", database="TEST")

# Create cursor object using cursor() method
cursor = db.cursor()

# Create SQL Query
sql = "DELETE FROM STUDENT WHERE ID = 1"

try:
    # Execute SQL Query
    res = cursor.execute(sql)
    # Commit in Database
    db.commit()
except:
    # Rollback in Database
    db.rollback()

# Close Database Connection
db.close()
