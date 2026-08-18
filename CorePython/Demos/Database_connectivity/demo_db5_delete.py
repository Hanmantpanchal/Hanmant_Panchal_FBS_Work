import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hamu@1531",
    database="college"
)

cursor = conn.cursor()

query = "DELETE FROM Student WHERE id = 2"

cursor.execute(query)

conn.commit()

print("Record deleted successfully")

cursor.close()
conn.close()