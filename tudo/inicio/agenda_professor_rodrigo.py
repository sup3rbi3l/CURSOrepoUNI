from tkinter import messagebox
import mysql.connector
from tkinter import *
from tkinter import ttk
from mysqlx import Column

cnx = mysql.connector.connect(
    host = '127.0.0.1',
    user='root',
    password='',
)

cursor = cnx.cursor()
cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "agenda"')

num_results = cursor.fetchone()[0]

cnx.close()


if num_results > 0:
 print('O banco de dados agenda existe e esta pronto para uso.')
else:
    cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
)

    cursor = cnx.cursor()
    cursor.execute('CREATE DATABASE agenda')
    cnx.commit()

    cnx = mysql.connector.connect(
    host =  '127.0.0.1',
    user = 'root',
    password = '',
    database = 'agenda',
)

    cursor = cnx.cursor()
    cursor.execute('CREATE TABLE contatos(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255),telefone VARCHAR(255))')
    cnx.commit()
    cnx.close()

class CrudApp:
 

   def __init__(self, window):
    self.window = window
    self.window.title('CRUD usando Python e MySQL')

    self.db = mysql.connector.connect(
      host =  '127.0.0.1',
      user = 'root',
      password = '',
      database = 'agenda'
    )

    self.table = ttk.Treeview(self.window, columns=('ID','Nome','Telefone','Email'),show='headings')
    self.table.heading('ID',text='ID')
    self.table.heading('Nome',text='Nome')
    self.table.heading('Telefone',text='Telefone')
    self.table.heading('Email',text='Email')
    self.table.pack(fill=BOTH,expand=True)
    self.add_btn = Button(self.window,text='Adicionar',command=self.add_data_window)
    self.add_btn.pack()
    self.add_btn = Button()














