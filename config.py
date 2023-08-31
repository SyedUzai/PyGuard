from utils.dbconfig import dbconfig
from getpass import getpass
import hashlib
import random
import string

def genDs(length=10):
    return''.join(random.choices(string.ascii_uppercase + string.digits, k = length))

def config():
    #Creating Database
    db = dbconfig()
    mycursor = db.cursor()
    print("Creating new configuration...")

    try:
        mycursor.execute("CREATE DATABASE pyguard")
        db.commit()

    except Exception as e:
        print(f'exception occurred: {str(e)}')
        exit()

    print("Database Created!")

    mycursor.execute("USE pyguard")

    #Creating tables
    query = "CREATE TABLE hidden (masterkey_hashed TEXT NOT NULL, secret TEXT NOT NULL)"
    mycursor.execute(query)
    print("Table 'hidden' created")

    query = "CREATE TABLE entries (sitename TEXT NOT NULL, siteurl TEXT, email TEXT, username TEXT, password TEXT NOT NULL)"
    mycursor.execute(query)
    print("Table 'entries' created")

    while 1:
        mp = getpass("Create your Master Password: ")
        if mp == getpass("Please Re-type:") and mp!="":
            break
        print("Please try again, passwords need to match and cannot be empty.")

    #Hashing the MP
    hashMp=hashlib.sha256(mp.encode()).hexdigest()
    print("Hash Generated.")

    #Generating secret
    secret=genDs()
    print("Secret key Generated.")

    #Adding to database
    query="INSERT INTO hidden (masterkey_hashed, secret) values(%s,%s)"
    res=(hashMp,secret)
    mycursor.execute(query,res)
    db.commit()
    print("Added Hash and secret to database.")

    db.close()


config()



