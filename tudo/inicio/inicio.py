from tkinter import messagebox
import mysql.connector

from tkinter import *
from tkinter import ttk



cnx = mysql.connector.connect(
    host = '127.0.0.1',
    user='root',
    password = '',
)


cursor = cnx.cursor()

cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "agenda"')


num_results = cursor.fetchone()[0]

cnx.close()


if num_results >0:
    print('O banco de dados agenda existe e esta pronto para uso')
    
else:
    cnx = mysql.connector.connect(
    host = '127.0.0.1',
    user='root',
    password = '',
)
