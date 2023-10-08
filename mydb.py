import mysql.connector

database = mysql.connector.connect(
 host="localhost", user="root", passwd="vis20adm", 
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE placement_database")

print("All Done!")