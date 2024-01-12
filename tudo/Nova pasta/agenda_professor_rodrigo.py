from tkinter import messagebox
import mysql.connector
from tkinter import *
from tkinter import ttk
from mysqlx import Column
import xlsxwriter

cnx = mysql.connector.connect(
    host = '127.0.0.1',
    user='root',
    password='',
)
#Executar a instrução SQL para verificar se o banco de dados exsite
cursor = cnx.cursor()
cursor.execute('SELECT COUNT(*) FROM information_schema.SCHEMATA WHERE SCHEMA_NAME = "agenda"')
#obter o numero de resultados
num_results = cursor.fetchone()[0]
# Fechar a conexão com o banco de dados
cnx.close()

# Se o numero de resultados for maior que zero o banco de dados existe
if num_results > 0:
 print('O banco de dados agenda existe e esta pronto para uso.')
else:
    # conectar-se ao sevidor MySQL para criar o banco de dados
    cnx = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
)
    #Criar o banco de dados agenda
    cursor = cnx.cursor()
    cursor.execute('CREATE DATABASE agenda')
    cnx.commit()
    
    #Conectar-se ao banco de dados agenda recem-criado
    cnx = mysql.connector.connect(
        host =  '127.0.0.1',
        user = 'root',
        password = '',
        database = 'agenda',    #Especificar o banco de dados
    )
    #criar a tabela contados
    cursor = cnx.cursor()
    cursor.execute('CREATE TABLE contatos(id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255),telefone VARCHAR(255), telefone VARCHAR(255), email VARCHAR(255));')
    
    cursor.execute("""
                   CREATE TABLE grupos(
                       id INT AUTO_INCREMENT PRIMARY KEY,
                       nome VARCHAR(255)
                       )""")
    
    # Fechar a conexão com o banco de dados
    cnx.commit()
    cnx.close()

class CrudApp:

    def __init__(self, window):
        self.window = window
        self.window.title('CRUD usando Python e MySQL')
        # Conectar ao banco de dados MySQL
        self.db = mysql.connector.connect(
            #host='localhost',
            host =  '127.0.0.1',
            user = 'root',
            password = '',
            database = 'agenda',
        )

        #Criar a tabela treeview
        #As colunas da tabela são definidas usando o argumento colunms no construtor 
        self.table = ttk.Treeview(self.window, columns=('ID','Nome','Telefone','Email'),show='headings')
        #Definindo o cabeçalho das colunas
        #O cabeçalho de cada coluna e definido usando o metodo heading
        self.table.heading('ID',text='ID')
        self.table.heading('Nome',text='Nome')
        self.table.heading('Telefone',text='Telefone')
        self.table.heading('Email',text='Email')
        #Adicionando a tabela na janela
        # a tabela é adicionada na janela do aplicativo usando o metodo pack. O argumento fill=BOTH faz com que a tabela ocupe todo o espaço disponivel na janela, tanto horizontal quanto verticalmente. O argumento expand=True permite que a tabela seja redimencionada, se necessario
        self.table.pack(fill=BOTH,expand=True)
        self.add_btn = Button(self.window,text='Adicionar',command=self.add_data_window)
        self.add_btn.pack()

        self.update_btn = Button(self.window, text='Update', command=self.update_data_window)
        self.update_btn.pack()

        self.delete_btn = Button(self.window, text='Delete', command=self.delete_data)
        self.delete_btn.pack()

        self.report_btn = Button(self.window, text='Gerar Relatorio', command=self.generate_report)
        self.report_btn.pack()

        self.add_grupo_btn = Button(self.window, text='Adicionar Grupo', command=self.add_data_grupo_window)
        self.add_grupo_btn.pack()

        #alinhar os botoes
        self.button = [self.add_btn, self.update_btn, self.delete_btn, self.report_btn, self.add_grupo_btn]
        self.align_buttons()

        #Atualizar a tabela inicialmente
        self.fetch_data()
        

    def align_buttons(self):
        for button in self.button:
            button.pack(side=LEFT)
        #Posicionar os botoes na horizontal

    def generate_report(self):
        #Obter os dados da tabela
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM contatos')
        data = []
        for row in cursor.fetchall():
            data.append(row)
            
        #Criar um objeto de planilha do Excel
        workbook = xlsxwriter.Workbook('contatos.xlsx')
        worksheet = workbook.add_worksheet()
        
        #Definir o cabeçalho da planilha
        worksheet.write('A1', 'ID')
        worksheet.write('B1', 'Nome')
        worksheet.write('C1', 'Telefone')
        worksheet.write('D1', 'Email')

        # Escrever os dados da tabela na planilha
        for i, row in enumerate(data):
            worksheet.write(i + 1, 0, row[0])
            worksheet.write(i + 1, 1, row[1])
            worksheet.write(i + 1, 2, row[2])
            worksheet.write(i + 1, 3, row[3])
            
        # Salvar a planilha
        workbook.close()
        
        #Exibit uma mensagem de confirmação
        messagebox.showinfo('Sucesso', 'Relatório gerado com sucesso!')

    def fetch_data(self):
        #Buscar dados do banco de dados e popular a tabela treeview
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM contatos')
        rows = cursor.fetchall()
        
        #Limpar dados anteriores 
        for row in self.table.get_children():
            self.table.delete(row)
            
        #Adionar novos dados
        for row in rows:
            self.table.insert('', 'end', value=row)
        # Adicionar um evento de seleção
        self.table.bind('<<TreeviewSelect>>', self.on_select)
        
    def on_select(self, event):
        #Obter o item selecionado
        item = self.table.selection()[0]
        
        #Pegar os dados do item selecionado
        data = self.table.item(item, 'values')
        id= data[0]
        nome = data[1]
        telefone = data[2]
        email = data[3]
        
        #GFazer algo com os dados
        
    def add_data_window(self):
        #Janela para acionar dados
        #Cria uma nova janela chamada add_window como filha da janela principal
        #Configura a nova janela para que sua origem esteja no canto superior esquerdo da janela principal
        add_window = Toplevel(self.window)
        add_window.title('Adicionar Contato')
        
        #Entradas para adicionar dados
        nome_label = Label(add_window, text='Nome: ')
        nome_label.grid(row=0, column=0, padx=10, pady=10)
        nome_entry = Entry(add_window)
        nome_entry.grid(row=0, column=1, padx=10, pady=10)
        
        telefone_label = Label(add_window, text='Telefone: ')
        telefone_label.grid(row=1, column=0, padx=10, pady=10)
        telefone_entry = Entry(add_window)
        telefone_entry.grid(row=1, column=1, padx=10, pady=10)
        
        email_label = Label(add_window, text='Email: ')
        email_label.grid(row=2, column=0, padx=10, pady=10)
        email_entry = Entry(add_window)
        email_entry.grid(row=2, column=1, padx=10, pady=10)
        
        # Botao para confirmar a adiçaõ
        confirm_btn = Button(add_window, text='Adicionar', comand=lambda:self.add_data(nome_entry.get(), telefone_entry.get(), email_entry.get(), add_window))
        confirm_btn.grid(row=3, column=0, columnspan=2, pady=10)
        
    def add_data_grupo_window(self):
        #Janela para adicionar dados
        #Cria uma nova janela chamada add_window como filha da janela principal
        #configura a nova janela para que sua origem esteja no canto superior esquerdo da janela principal
        add_window = Toplevel(self.window)
        add_window.title('Adicionar Grupo')
        
        #Entradas para adicionar dados
        nome_label = Label(add_window, text='Nome do grupo: ')
        nome_label.grid(row=0, column=0, padx=10, pady=10)
        nome_entry = Entry(add_window)
        nome_entry.grid(row=0, column=1, padx=10, pady=10)
        
        #Botao para confirmar a adição
        confirm_btn = Button(add_window, text='Adicionar', comand=lambda:self.add_data_grupo(nome_entry.get(), add_window))
        confirm_btn.grid(row=3, column=0, columnspan=2, pady=10)

    def add_data_grupo(self,nome,add_window):
        #Validar o nome do grupo
        if nome == '':
            messagebox.showerror('Error', 'O nome do grupo não pode estar vazio.')
            return
        
        #Adiocionar dados ao banco de dados
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO grupos (nome) VALUE (%s)', (nome,))
        self.db.commit()
        add_window.destroy()
        self.fetch_data()

    def add_data(self, nome, telefone, email, add_window):
        #Adicionar dados ao banco de dados
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO contatos (nome, telefone, email) VALUES (%s, %s, %s)', (nome, telefone, email))
        self.db.commit()
        add_window.destroy()
        self.fetch_data()
        
    def update_data_window(self):
        #Janela para atualizar dados
        update_window = Toplevel(self.window)
        update_window.title('Atualizar Contato')
        
        
        nome_label = Label(update_window, text='Novo Nome: ')
        nome_label.grid(row=1, column=0, padx=10, pady=10)
        nome_entry = Entry(update_window)
        nome_entry.grid(row=1, column=1, padx=10, pady=10)
        
        telefone_label = Label(update_window, text='Novo Telefone: ')
        telefone_label.grid(row=2, column=0, padx=10, pady=10)
        telefone_entry = Entry(update_window)
        telefone_entry.grid(row=2, column=1, padx=10, pady=10)
        
        email_label = Label(update_window, text='Novo Email: ')
        email_label.grid(row=3, column=0, padx=10, pady=10)
        email_entry = Entry(update_window)
        email_entry.grid(row=3, column=1, padx=10, pady=10)

        #Botão para confirmar a atualização
        #A função self.update_data é chamada quando o botão é pressionado. Esta função atualiza os dados do usuario com base nas informações inseridas nos campos de entrada(Entry). Os argumentos da função self.update_data são os valores obtidos dos campos de entrada, bem como a janeça update_window.
        #Ao executar este codigo, um botão chamado 'Atualizar' será exibido na janela. Quando o botão é pressionado, a função self.update_data será chamada, atualizando os dados do usuario com base nas informações inseridas
        
        confirm_btn = Button(update_window, text='Atualizar', command=lambda:self.update_data(nome_entry.get(), telefone_entry.get(), email_entry.get(), update_window))
        confirm_btn.grid(row=4, column=0, columnspan=2, pady=10)
        
    def update_data(self, novo_nome, novo_telefone, novo_email, update_window):
        item = self.table.selection()[0]
        data = self.table.item(item, 'values')
        id = data[0]
        #Atualizar dados no banco de dados
        #o objeto 'cursor' é utilizado para executar a instrução SQl.
        cursor = self.db.cursor()
        cursor.execute('UPDATE contatos SET nome=%s, telefone=%s, email=%s WHERE id=%s', (novo_nome, novo_telefone, novo_email, id))
        #confirma a alteração dno banco de dados usando a função commit
        self.db.commit()
        #Fecha a janela de atualização
        update_window.destroy()
        #Recupera os dadso atuaçozados da tabela 'contatos' usando a função 'fetch_data'
        self.fetch_data()
        
    def delete_data(self):
        #Obter o item selecionado
        item = self.table.selection()[0]
        #Pegar o ID do contato selecionado
        data = self.table.item(item,'values')
        id = data[0]



        #Verificar se o usuario realmente deseja excluir o registro
        if messagebox.askyesno('Confirmação', 'Tem certeza de que deseja excluir o registro?'):
            #Deletar dados do banco de dados
            cursor = self.db.cursor()
            cursor.execute('DELETE FROM contatos WHERE id=%s', (id,))
            #Passe o ID como uma tupla de um elemento
            self.db.commit()
            self.fetch_data()

if __name__== "__main__":
    window = Tk()
    app = CrudApp(window)
    window.mainloop()







