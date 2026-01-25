import sqlite3

#Connect to SQlite
connection = sqlite3.connect("student.db")

#Create a cursor object to insert, record, create table

cursor = connection.cursor()

#Create the table 
table_info="""
Create table if not exists STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25));
"""

cursor.execute(table_info)

# Insert some record

cursor.execute('''Insert into STUDENT values ('Krish', 'Data Science', 'A')''')
cursor.execute('''Insert into STUDENT values ('Yash', 'IBM', 'B')''')
cursor.execute('''Insert into STUDENT values ('Balaguru', 'ML', 'C')''')
cursor.execute('''Insert into STUDENT values ('Aaditya', 'Cybersecurity', 'D')''')

# Display the records
connection.commit()

print("The inserted records are")
data = cursor.execute('''Select *from STUDENT''')
for row in data:
    print(row)