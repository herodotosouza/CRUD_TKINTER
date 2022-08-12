import sqlite3
from tkinter import*
from tkinter import ttk
from turtle import bgcolor


root = Tk()

class Funcs():
    def limpar_tela(self):

        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.telefone_entry.delete(0,END)
        self.cidade_entry.delete(0,END)
    def conecata_bd(self):
        self.conn = sqlite3.connect("clientes.bd")
        self.cursor = self.conn.cursor(); print("Conectando ao Banco de Dados!")
    def desconecta_bd(self):
        self.conn.close(); print('Desconectando do banco de dados')
    def montaTabelas(self):
        self.conecata_bd()

        ###CRIANDO TABELAS
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER (20),
                cidade CHAR(40)
                
            );
        """)
        self.conn.commit(); print('Banco de dados criado')
        self.desconecta_bd()
    def add_cliente(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
        self.conecata_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?) """, (self.nome, self.telefone, self.cidade))
        self.conn.commit()
        self.desconecta_bd
        self.select_lista()
        self.limpar_tela()
    def select_lista(self):
        self.listaHe.delete(*self.listaHe.get_children())
        self.conecata_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_clientes ASC """)
        for i in lista:
            self.listaHe.insert("",END,values=i)
        self.desconecta_bd()


class Aplication(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widghts_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        root.mainloop()
        
    
    def tela(self):
        self.root.title("cadastro de clientes")
        self.root.configure(background='#4682B4')
        self.root.geometry("788x588")
        self.root.resizable(True, True)
        self.root.maxsize(width= 988, height=700)
        self.root.minsize(width=500, height=400)


    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg= '#BEBEBE', 
                            highlightbackground='#F5F5DC', highlightthickness=3)
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth=0.96,relheight=0.46)

        self.frame_2 = Frame(self.root, bd = 4, bg= '#BEBEBE', 
                            highlightbackground='#F5F5DC', highlightthickness=3)
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth=0.96,relheight=0.46)
    
    def widghts_frame1(self):
        # criando botoes limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", bd=4, bg='#B0C4DE',fg='white', font= ('vexana',8,'bold'),command=self.limpar_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        # criando botoes buscar 
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=4, bg='#B0C4DE',fg='white', font= ('vexana',8,'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        # criando botoes Novo
        self.bt_novo = Button(self.frame_1, text="Novo", bd=4, bg='#B0C4DE',fg='white', font= ('vexana',8,'bold'))
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        # criando botoes Alterar
        self.bt_alterar = Button(self.frame_1, text="Alterar", bd=4, bg='#B0C4DE',fg='white', font= ('vexana',8,'bold'),command= self.add_cliente)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        # criando botoes Apagar
        self.bt_apagar = Button(self.frame_1, text="Apagar", bd=4, bg='#B0C4DE',fg='white', font= ('vexana',8,'bold'))
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        #Criação da label e entrada do codigo
        self.lb_codigo = Label(self.frame_1, text = "Código",bg='#BEBEBE' ,fg= '#107db2', font=('vexana',10,'bold'))
        self.lb_codigo.place(relx = 0.05, rely=0.05)
        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx = 0.05, rely=0.15,relwidth=0.08)

        #Criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text = "Nome",bg='#BEBEBE' ,fg= '#107db2', font=('vexana',10,'bold'))
        self.lb_nome.place(relx = 0.05, rely=0.35)
        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx = 0.05, rely=0.45,relwidth=0.8)

        #Criação da label e entrada do telefone
        self.lb_telefone = Label(self.frame_1, text = "telefone",bg='#BEBEBE' ,fg= '#107db2', font=('vexana',10,'bold'))
        self.lb_telefone.place(relx = 0.05, rely=0.6)
        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx = 0.05, rely=0.7,relwidth=0.4)

        #Criação da label e entrada do cidade
        self.lb_cidade = Label(self.frame_1, text = "cidade",bg='#BEBEBE' ,fg= '#107db2', font=('vexana',10,'bold'))
        self.lb_cidade.place(relx = 0.5, rely=0.6)
        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx = 0.5, rely=0.7,relwidth=0.48)
    
    def lista_frame2(self):
        self.listaHe = ttk.Treeview(self.frame_2, height= 3, column=("col1","col2","col3","col4"))
        self.listaHe.heading("#0", text="")
        self.listaHe.heading("#1", text="Codigo")
        self.listaHe.heading("#2", text="Nome")
        self.listaHe.heading("#3", text="Telefone")
        self.listaHe.heading("#4", text="Cidade")

        self.listaHe.column("#0",width=1)
        self.listaHe.column("#1",width=50)
        self.listaHe.column("#1",width=200)
        self.listaHe.column("#1",width=125)
        self.listaHe.column("#1",width=125)

        self.listaHe.place(relx=0.01 , rely=0.1, relwidth=0.95,relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaHe.configure(yscroll =self.scroolLista.set)
        self.scroolLista.place(relx=0.96 ,rely=0.1, relwidth=0.03, relheight=0.85)




Aplication()
