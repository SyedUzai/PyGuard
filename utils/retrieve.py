from utils.dbconfig import dbconfig
from rich.table import Table
from crypto.Protocol import KDF
from crypto.Random import get_random_bytes
from crypto.Hash import SHA512
from utils.encrypt import decrypt_AES_CBC_256
import pyperclip

def computeMk(mp,ds):
    password=mp.encode()
    salt = ds.encode()
    key = KDF(password,salt,32,count = 1000000,hmac_hash_module=SHA512)
    return key
def retrieveEntries (mp,secret,search,decryptPassword=False):
    db=dbconfig()
    mycursor=db.cursor()
    #mycursor.execute("USE pyguard")

    query = ""

    #If user does NOT specify --> show all 
    if len(search) == 0:
        query="SELECT * FROM entries"
    #If user specifies --> show selected
    else:
        query="SELECT * FROM entries"
        for i in search:
            query+=f"{i} = '{search[i]}' AND"
        query = query[: -5]

    mycursor.execute(query)
    results = mycursor.fetchall()

    if len(results) == 0:
        print("No results for search.")
        return
    if(decryptPassword and len(results >1)) or (not decryptPassword):
        table = Table(title="Results")
        table.add_column("Site Name")
        table.add_column("URL")
        table.add_column("Email")
        table.add_column("Username")
        table.add_column("Password")

        for i in results:
            table.add_row(i[0],i[1],i[2],i[3],"{Hidden}")
        print(table)

        return
    if len(results) ==1 and decryptPassword:
        mk = computeMk(mp,secret)
        decrypted = decrypt_AES_CBC_256(mk,results[0][4])
        pyperclip.copy(decrypted.decode())
        print("Password copied to clipboard.")

    db.close()


        









