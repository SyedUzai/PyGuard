import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="syeduzai",
    passwd="Carsham412##",
    database="testdatabase"
)

mycursor=db.cursor()

