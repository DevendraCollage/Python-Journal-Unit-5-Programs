# Import SQL module for Database Connection
import mysql.connector as mysql

# Open Database Connection
db = mysql.connect(host="localhost", user="root", password="", database="TEST")

# Create cursor object using cursor() method
cursor = db.cursor()

# Create SQL Query
sql = """UPDATE STUDENT
         SET AGE = 21, MARKS = 75
         WHERE ID = 1"""

try:
    # Execute SQl Query
    res = cursor.execute(sql)
    # Commit in Database
    db.commit()
except:
    # Rollback in Database
    db.rollback()

# Close Database Connection
db.close()
