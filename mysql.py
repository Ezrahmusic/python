import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "myusername",
    passwd = "mypassword",
    database = "mydatabase"
)
print(mydb)
mycursor = mydb.cursor()
cursor =connection.cursor() # used to get cursor
mycursor.execute("CREATE DATABASE mydatabase")


for x in mycursor:
    print(x)

    use admin;
    db.runcommand( {storageSetConfig})

