import mysql.connector
from tkinter import *
from tkinter import ttk
import xlsxwriter
class CrudApp:
    def __init__(self, window):
        self.window = window
        self.window.title('CRUD usando Python e MySQL')

        # Conectar ao banco de dados MySQL
        self.db = mysql.connector.connect(  
            host='localhost',
            user='root',
            password='',
            database='agenda'
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
        self.add_btn = Button(self.window, text='Adicionar', command=self.add_data_window)
        self.add_btn.pack()

        # Botões para atualizar e deletar
        self.update_btn = Button(self.window, text='Atualizar', command=self.update_data_window)
        self.update_btn.pack()

        self.delete_btn = Button(self.window, text='Deletar', command=self.delete_data)
        self.delete_btn.pack()

        # Atualizar a tabela inicialmente
        self.fetch_data()

    def fetch_data(self):
        # Buscar dados do banco de dados e coloca na tabela treeview
        cursor = self.db.cursor()
        cursor.execute('SELECT * FROM contatos')
        rows = cursor.fetchall()

        # Limpar dados anteriores
        for row in self.table.get_children():
            self.table.delete(row)

        # Adicionar novos dados
        for row in rows:
            self.table.insert('', 'end', values=row)

    def add_data_window(self):
        # Janela para adicionar dados
        # Cria uma nova janela chamada add_window como filha da janela principal
        # Configura a nova janela para que sua origem esteja no canto superior esquerdo da janela principal
        add_window = Toplevel(self.window)
        add_window.title('Adicionar Contato')

        # Entradas para adicionar dados
        nome_label = Label(add_window, text='Nome:')
        nome_label.grid(row=0, column=0, padx=10, pady=10)
        nome_entry = Entry(add_window)
        nome_entry.grid(row=0, column=1, padx=10, pady=10)

        telefone_label = Label(add_window, text='Telefone:')
        telefone_label.grid(row=1, column=0, padx=10, pady=10)
        telefone_entry = Entry(add_window)
        telefone_entry.grid(row=1, column=1, padx=10, pady=10)

        email_label = Label(add_window, text='Email:')
        email_label.grid(row=2, column=0, padx=10, pady=10)
        email_entry = Entry(add_window)
        email_entry.grid(row=2, column=1, padx=10, pady=10)

        # Botão para confirmar a adição
        confirm_btn = Button(add_window, text='Adicionar', command=lambda: self.add_data(nome_entry.get(), telefone_entry.get(), email_entry.get(), add_window))
        confirm_btn.grid(row=3, column=0, columnspan=2, pady=10)

    def add_data(self, nome, telefone, email, add_window):
        # Adicionar dados ao banco de dados
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO contatos (nome, telefone, email) VALUES (%s, %s, %s)', (nome, telefone, email))
        self.db.commit()
        add_window.destroy()
        self.fetch_data()

    def update_data_window(self):
        # Janela para atualizar dados
        update_window = Toplevel(self.window)
        update_window.title('Atualizar Contato')

        # Entradas para atualizar dados
        id_label = Label(update_window, text='ID do Contato:')
        id_label.grid(row=0, column=0, padx=10, pady=10)
        id_entry = Entry(update_window)
        id_entry.grid(row=0, column=1, padx=10, pady=10)

        nome_label = Label(update_window, text='Novo Nome:')
        nome_label.grid(row=1, column=0, padx=10, pady=10)
        nome_entry = Entry(update_window)
        nome_entry.grid(row=1, column=1, padx=10, pady=10)

        telefone_label = Label(update_window, text='Novo Telefone:')
        telefone_label.grid(row=2, column=0, padx=10, pady=10)
        telefone_entry = Entry(update_window)
        telefone_entry.grid(row=2, column=1, padx=10, pady=10)

        email_label = Label(update_window, text='Novo Email:')
        email_label.grid(row=3, column=0, padx=10, pady=10)
        email_entry = Entry(update_window)
        email_entry.grid(row=3, column=1, padx=10, pady=10)

        # Botão para confirmar a atualização
        # A função self.update_data é chamada quando o botão é pressionado. Esta função atualiza os dados do usuário com base nas informações inseridas nos campos de entrada (Entry). Os argumentos da função self.update_data são os valores obtidos dos campos de entrada, bem como a janela update_window.
        #Ao executar este código, um botão chamado 'Atualizar' será exibido na janela. Quando o botão é pressionado, a função self.update_data será chamada, atualizando os dados do usuário com base nas informações inseridas
        confirm_btn = Button(update_window, text='Atualizar', command=lambda: self.update_data(id_entry.get(), nome_entry.get(), telefone_entry.get(), email_entry.get(), update_window))
        confirm_btn.grid(row=4, column=0, columnspan=2, pady=10)

    def update_data(self, id_contato, novo_nome, novo_telefone, novo_email, update_window):
        # Atualizar dados no banco de dados
        # o objeto 'cursor' é utilizado para executar a instrução SQL
        cursor = self.db.cursor()
        cursor.execute('UPDATE contatos SET nome=%s, telefone=%s, email=%s WHERE id_contato=%s', (novo_nome, novo_telefone, novo_email, id_contato))
        # Confirma a alteração no banco de dados usando a função commit
        self.db.commit()
        # Fecha a janela de atualização
        update_window.destroy()
        # Recupera os dados atualizados da tabela 'contatos' usando a função 'fetch_data'
        self.fetch_data()

    def delete_data(self):
        # Deletar dados
        delete_window = Toplevel(self.window)
        delete_window.title('Deletar Contato')

        # Entrada para deletar dados
        id_label = Label(delete_window, text='ID do Contato:')
        id_label.grid(row=0, column=0, padx=10, pady=10)
        id_entry = Entry(delete_window)
        id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Botão para confirmar a exclusão
        confirm_btn = Button(delete_window, text='Deletar', command=lambda: self.delete_data_confirm(id_entry.get(), delete_window))
        confirm_btn.grid(row=1, column=0, columnspan=2, pady=10)

    def delete_data_confirm(self, id_contato, delete_window):
        # Deletar dados do banco de dados
        cursor = self.db.cursor()
        cursor.execute('DELETE FROM contatos WHERE id_contato=%s', (id_contato,))
        self.db.commit()
        delete_window.destroy()
        self.fetch_data()

if __name__ == "__main__":
    window = Tk()
    app = CrudApp(window)
    window.mainloop()
