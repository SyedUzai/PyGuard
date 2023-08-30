import mysql.connector
def dbconfig():
    #Connecting with MySql server
    
    try:
        db = mysql.connector.connect(
        host="localhost",
        user="syeduzai",
        passwd="Carsham412##",
        )

    except Exception as e:
        print("Could not connect")

    return db


print(dbconfig())