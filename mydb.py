"""Run one time to create the Database and view it on Mysql Workbench"""

import mysql.connector

database = mysql.connector.connect(host="localhost", user="root", passwd="12345678")

# Create a Cursor Object
cursor = database.cursor()

# Create a Database
cursor.execute(operation="CREATE DATABASE django_crm")

# Terminal Message
print("All Done! ✅")