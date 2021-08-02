# Aaliyah

import mysql.connector


mydb = mysql.connector.connect(
    user='lifechoices',
    password = '@Lifechoices1234',
    host = 'localhost',
    database = 'LC_ONLINE',
    auth_plugin = 'mysql_native_password')

cursor = mydb.cursor()

query = "create table users(" \
        "ID varchar(13) NOT NULL," \
        "name varchar(30) NOT NULL," \
        "surname varchar(30) NOT NULL," \
        "phone varchar(13) NOT NULL," \
        "role varchar(30) NOT NULL," \
        "password varchar(25) NOT NULL," \
        "Primary key(ID))"

cursor.execute(query)

mydb.close()
