# Import mysql module for Database Connection
import mysql.connector as mysql

# Open Database Connection
db = mysql.connect(host="localhost", user="root", password="", database="TEST")

# Create cursor object using cursor() method
cursor = db.cursor()

# Create SQl Query
sql = """CREATE TABLE STUDENT (
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT,
         GENDER CHAR(1),
         MARKS INT
)"""

try:
    # Execute SQL Query
    data = cursor.execute(sql)
    # Commit in Database
    db.commit()
except:
    # Rollback in Database
    db.rollback()

# Close Database Connection
db.close()
