import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hamu@1531",
    database="college"
)

cursor = conn.cursor()

query = "SELECT * FROM Student"

cursor.execute(query)

result = cursor.fetchall()
# result = cursor.fetchone()
# result = cursor.fetchmany(2)

for row in result:
    print(row)

cursor.close()
conn.close()