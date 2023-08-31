import mysql.connector
def dbconfig():
    #Connecting with MySql server
    try:
        DB = mysql.connector.connect(
         host="localhost",
         user="syeduzai",
         passwd="Carsham412##",
         )
        print("Connected to db.")

    except Exception as e:
        print(f'exception occurred: {str(e)}')

    return DB

