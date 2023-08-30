import mysql.connector
def dbconfig():
    
    try:
        db = mysql.connector.connect(
        host="localhost",
        user="syeduzai",
        passwd="Carsham412##",
        )

    except Exception as e:
        print("Could not connect")

    return db


