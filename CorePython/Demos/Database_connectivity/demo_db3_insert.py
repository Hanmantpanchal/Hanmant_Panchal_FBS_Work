import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hamu@1531",
    database="college"
)

cursor = conn.cursor()

query1 = "INSERT INTO Student (id, name, age, class) VALUES (1, 'Rahul', 21, 'BCA')"
query2 = "INSERT INTO Student (id, name, age, class) VALUES (2, 'Amit', 22, 'BCA')"
query3 = "INSERT INTO Student (id, name, age, class) VALUES (3, 'Priya', 20, 'MCA')"

cursor.execute(query1)
cursor.execute(query2)
cursor.execute(query3)

conn.commit()

print("Records inserted successfully")

cursor.close()
conn.close()