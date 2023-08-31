import mysql.connector

# Replace with your actual database connection details
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Carsham412##",
)

mycursor = db.cursor()

# Create a new database
mycursor.execute("CREATE DATABASE tester")

db.commit()
mycursor.close()
db.close()

print("Database created successfully!")
