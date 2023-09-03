from utils.dbconfig import dbconfig
from getpass import getpass
from utils.encrypt import encrypt_AES_CBC_256
from crypto.Protocol.KDF import PBKDF2
from crypto.Hash import SHA512
from crypto.Random import get_random_bytes
import base64

def computeMk(mp,ds):
    password=mp.encode()
    salt = ds.encode()
    key = PBKDF2(password,salt,32,count = 1000000,hmac_hash_module=SHA512)
    return key

def addEntry(mp,secret,sitename,url,email,username):
    # get password from user
    password=getpass("Please type in your password: ")
    mk = computeMk(mp,secret)
    encrypted = encrypt_AES_CBC_256(mk,password)

    db= dbconfig()
    mycursor=db.cursor()
    mycursor.execute("USE pyguard")
    query= "INSERT INTO entries (sitename,url,email,username,password) "
    val= (sitename,url,username,encrypted)
    mycursor.execute(query,val)
    db.commit()

    print("Added entry.")



    
    
