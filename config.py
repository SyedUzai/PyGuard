from utils.dbconfig import dbconfig
def config():
    #Creating Database
    db = dbconfig()
    mycursor = db.cursor()
    try:
        mycursor.execute("CREATE DATABASE pyguard")

    except Exception as e:
        print("Could not create database! please try again")
        exit()

    print("Database Created!")

    #Creating tables
    query1 = "CREATE TABLE hidden (masterkey_hashed TEXT NOT NULL, secret TEXT NOT NULL)"
    execute=mycursor.execute(query1)
    print("Table 'Hidden' Created")

    query2 = "CREATE TABLE entries (sitename TEXT NOT NULL, siteurl TEXT, email TEXT, username TEXT, password TEXT NOT NULL)"
    execute2=mycursor.execute(query2)
    print("Table 'entries' Created")

print(config())