import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Hamu@1531",
    database="college"
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE Student(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(20),
        age INT,
        class VARCHAR(20)
    )
""")

print("Table created successfully")

cursor.close()
conn.close()