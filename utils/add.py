from utils.dbconfig import dbconfig
from getpass import getpass
import utils.encrypt
from crypto.Protocol.KDF import PBKDF2
from crypto.Hash import SHA512
from crypto.Random import get_random_bytes
import base64

def computeMk(mp,ds):
    password=mp.encode()
    salt = ds.encode()
    key = PBKDF2(password,salt,32,count = 1000000,hmac_hash_module=SHA512)
    return key

def addEntry(mp,secret,sitename,siteurl,email,username):
    # get password from user
    password=getpass("Please type in your password: ")
    mk = computeMk(mp,secret)
    encrypted = utils.encrypt.encrypt(key=mk,source=password,keyType="bytes")

    db= dbconfig()
    mycursor=db.cursor()
    mycursor.execute("USE pyguard")
    query= "INSERT INTO entries (sitename,siteurl,email,username,password) values (%s,%s,%s,%s,%s)"
    val= (sitename,siteurl,email,username,encrypted)
    mycursor.execute(query, val)
    db.commit()

    print("Added entry.")



    
    
