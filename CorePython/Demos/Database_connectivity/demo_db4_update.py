import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hamu@1531",
    database="college"
)

cursor = conn.cursor()

query = "UPDATE Student SET age = 23 WHERE id = 1"

cursor.execute(query)

conn.commit()

print("Record updated successfully")

cursor.close()
conn.close()