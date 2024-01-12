import re
from tkinter import messagebox
import mysql.connector
from tkinter import *
from tkinter import ttk
import xlsxwriter
from tkinter import Tk, Toplevel
import reportlab
from reportlab.pdfgen import canvas



class CrudApp:

    def __init__(self, window):
        self.window = window
        self.window.title('CRUD usando Python e MySQL')
       

        # Conectar ao banco de dados MySQL
        self.db = mysql.connector.connect(
           # host='localhost',
           host='127.0.0.1',
            user='root',
            password='',
            database='loja'
        )
       
        # Criar a tabela treeview
        # As colunas da tabela são definidas usando o argumento columns no construtor
        self.table = ttk.Treeview(self.window, columns=('ID', 'Nome', 'Telefone', 'Email'), show='headings')
        # Definindo o cabeçalho das colunas
        # O cabeçalho de cada coluna é definido usando o método heading
        self.table.heading('ID', text='ID')
        self.table.heading('Nome', text='Nome')
        self.table.heading('Telefone', text='Telefone')
        self.table.heading('Email', text='Email')
        # Adicionando a tabela na janela
        # a tabela é adicionada na janela do aplicativo usando o método pack. O argumento fill=BOTH faz com que a tabela ocupe todo o espaço disponível na janela, tanto horizontal quanto verticalmente. O argumento expand=True permite que a tabela seja redimensionada, se necessário
        self.table.pack(fill=BOTH, expand=True)

        # Botão para adicionar
        self.add_btn = Button(self.window, text='Adicionar Contato')
        self.add_btn.pack()

        # Botões para atualizar e deletar
        self.update_btn = Button(self.window, text='Atualizar')
        self.update_btn.pack()

        self.delete_btn = Button(self.window, text='Deletar')
        self.delete_btn.pack()

        report_btn = Button(self.window, text='Gerar relatório')
        report_btn.pack()
        
        self.add_grupo_btn = Button(self.window, text='Adicionar Grupo')
        self.add_grupo_btn.pack()
        
        # Botão para limpar dados
        self.clear_data_btn = Button(self.window, text='Limpar Dados')
        self.clear_data_btn.pack()
        
        # Botão de excluir banco de dados
        self.deletar_banco_de_dados = Button(self.window, text='Deleta o Banco')
        self.deletar_banco_de_dados.pack()
        # Alinhar os botões a esquerda
        self.buttons = [self.add_btn, self.update_btn, self.delete_btn,report_btn, self.add_grupo_btn,self.clear_data_btn]
       
        
        
window = Tk()
app = CrudApp(window)
window.mainloop()

