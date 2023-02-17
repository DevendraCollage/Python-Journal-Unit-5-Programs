# Import SQL module for Database Connection
import mysql.connector as mysql

# Open Database Connection
db = mysql.connect(host="localhost", user="root", password="", database="TEST")

# Create cursor object using cursor method
cursor = db.cursor()

# Create SQL Query
sql = """INSERT INTO STUDENT
         (FIRST_NAME,LAST_NAME,AGE,GENDER,MARKS)
         VALUES('Devendra','Parmar',20,'M',85)
        """

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
