from tkinter import messagebox
import mysql.connector
from tkinter import *
from tkinter import ttk
import xlsxwriter

# Conectar ao banco de dados MySQL
cnx = mysql.connector.connect(
    host = '127.0.0.1',
    user='root',
    password='',
)

#executar s instruçao sql para verificar se o banco de dados existe
cursor = cnx.cursor()
cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "agenda"')

# obter o numero de resultados
num_results = cursor.fetchone()[0]

# fechar a conexao como o banco de dados
cnx.close()

# se o numero de resultados for maior que zero, o banco de dados existe
if num_results > 0:
 print('O banco de dados agenda existe e esta pronto para uso.')
else:

    # conectar-se ao servidor mysql para criar o banco de dados 
    cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
)
    # criar o anco de dados agenda
    cursor = cnx.cursor()
    cursor.execute('CREATE DATABASE agenda')
    cnx.commit()

    cnx = mysql.connector.connect(
    host =  '127.0.0.1',
    user = 'root',
    password = '',
    database = 'agenda', # especificar o banco de dados
)
    #criar a tabela contatos
    cursor = cnx.cursor()
    cursor.execute('CREATE TABLE contatos(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255),telefone VARCHAR(255))')

    cursor.execute(""""
        CREATE TABLE grupos
            id INT AUTO_INCEMNT PRIMARY KEy,
            nomme VARCHAR(255
            )
    
    
   """ )


    # fechar a conexao com o banco de dados
    cnx.commit()
    cnx.close()

class CrudApp:
 

   def __init__(self, window):
    self.window = window
    self.window.title('CRUD usando Python e MySQL')

    #conectar ao banco de dados  mysql 
    self.db = mysql.connector.connect(
        #host="localhost",
      host =  '127.0.0.1',
      user = 'root',
      password = '',
      database = 'agenda',
    )
    
    # Criar a tabela treeview
    # As colunas da tabela são definidas usando o argumento columns no constructor
    self.table = ttk.Treeview(self.window, columns=('ID','Nome','Telefone','Email'),show='headings')
    # Definindo o cabeçalho das colunas
    # O cabeçalho de cada coluna é definido usando o método heading
    self.table.heading('ID',text='ID')
    self.table.heading('Nome',text='Nome')
    self.table.heading('Telefone',text='Telefone')
    self.table.heading('Email',text='Email')
    # Adicionando a tabela na janela
    # a tabela é adicionada na janela do aplicativo usando o método
    #pack. O argumento fill=BOTH faz com que a tabela ocupe todo o espaço
    self.table.pack(fill=BOTH,expand=True)
    self.add_btn = Button(self.window,text='Adicionar',command=self.add_data_window)
    self.add_btn.pack()
    self.update_btn = Button(self.window, text='Atualizar', command=self.update_data_window)
    self.update_btn.pack() 
    self.delete_btn = Button(self.window, text='Deletar', command=self.delete_data)
    self.delete_btn.pack()

    self.buttons = [self.add_btn, self.ubdate_btn, self.delete_btn, report_btn, self.add_grupo_btn] 
    self..align_buttons() 

    self.fetch_data()

def align_buttons(self):
   for button in self.buttons:
       button.pack(side=LEFT)

       # Posicionar os botôes na horizontal

def generate_report(self):
   # Obter os dadosw da tabela

   cursor = self.db.cursor()
   cursor.execute('SELECT * FROM contatos')
   data = []
   for row in cursor.fetchall():
      data.append(row)

   worKsheet.write('A1' , 'ID')
   worKsheet.write('B1', 'Nome')
   worKsheet.write('C1', 'Telefone')
   worksheet.write('D1' , 'Email')

   # Escrever os dados da tabela na planilha

   for i, row in enumerate(data):
      worksheet.write(i + 1,0 row)        

def fetch_data(self):
    cursor = self.db.cursor()
    cursor.execute("SELECT * FROM contatos")
    data = []
    for row in cursor.fetchall():
       data.append
    rows = cursor.fetchall()





  










