import sqlite3

# Create a connection to the database
connection = sqlite3.connect("students.db")


# Create a cursor object using the cursor() method
cursor = connection.cursor()

# Create a table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25));
"""

cursor.execute(table_info)

# Insert data into the table
cursor.execute("INSERT INTO STUDENT VALUES ('jacob', '10th', 'A')")
cursor.execute("INSERT INTO STUDENT VALUES ('sudhanshu', '9th', 'A')")
cursor.execute("INSERT INTO STUDENT VALUES ('kadher', '8th', 'B')")
cursor.execute("INSERT INTO STUDENT VALUES ('kunji', '10th', 'B')")


# display all the rows in the table

print('The inserted records are:')
data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)