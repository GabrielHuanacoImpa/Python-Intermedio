import tkinter as tk
from tkinter import ttk
from modelo.consultas_dao import Peliculas,crear_tabla, guardar_peli,listar_peli, listar_generos, editar_peli, borrar_peli, listar_nacionalidades
from tkinter import messagebox

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root,width=480,height=320) # en pixeles
        self.root = root
        self.id_peli = None
        self.pack()
        #self.config(bg='green')
        
        self.label_form() # instancio
        self.input_form()
        self.botones_principales()
        self.bloquear_campos()
        self.mostrar_tabla() # instancio mostrar tabla

#***************************Label fijos ***************
    def label_form(self):
        self.label_nombre = tk.Label(self, text="Nombre: ")
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row= 0, column=0,padx=10,pady=10)
        self.label_nombre = tk.Label(self, text="Duración: ")
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row= 1, column=0,padx=10,pady=10)
        self.label_nombre = tk.Label(self, text="Genero: ")
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row= 2, column=0,padx=10,pady=10)

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.label_protagonista= tk.Label(self, text="Protagonista: ")
        self.label_protagonista.config(font=('Arial',12,'bold'))
        self.label_protagonista.grid(row= 0, column=2,padx=10,pady=10)

        self.label_director= tk.Label(self, text="Director: ")
        self.label_director.config(font=('Arial',12,'bold'))
        self.label_director.grid(row= 1, column=2,padx=10,pady=10)

        self.label_nacionalidad = tk.Label(self, text="Nacionalidad: ")
        self.label_nacionalidad.config(font=('Arial',12,'bold'))
        self.label_nacionalidad.grid(row= 2, column=2,padx=10,pady=10)

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#***************************Input ***************
    def input_form(self):
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)
        self.entry_nombre.config(width=30)
        self.entry_nombre.grid(row= 0, column=1,padx=10,pady=10, columnspan='1')
        
        self.duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.duracion)
        self.entry_duracion.config(width=30)
        self.entry_duracion.grid(row= 1, column=1,padx=10,pady=10, columnspan='1')
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.protagonista = tk.StringVar()
        self.entry_protagonista = tk.Entry(self, textvariable=self.protagonista)
        self.entry_protagonista.config(width=30)
        self.entry_protagonista.grid(row= 0, column=3,padx=10,pady=10, columnspan='1')

        self.director = tk.StringVar()
        self.entry_director = tk.Entry(self, textvariable=self.director)
        self.entry_director.config(width=30)
        self.entry_director.grid(row= 1, column=3,padx=10,pady=10, columnspan='1')
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        x = listar_generos()
        y = []
        for i in x:
            y.append(i[1])
        
        #cancatenamos el nuevo array
        self.generos = ['Seleccione Uno'] + y
        self.entry_genero = ttk.Combobox(self, state="readonly")
        self.entry_genero['values'] = self.generos
        self.entry_genero.current(0)
        self.entry_genero.config(width=25)
        self.entry_genero.bind("<<ComboboxSelected>>")
        self.entry_genero.grid(row= 2, column=1,padx=10,pady=10, columnspan='1')
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        xx = listar_nacionalidades()
        yy = []
        for i in xx:
            yy.append(i[1])
        
        #cancatenamos el nuevo array
        self.nacionalidades = ['Seleccione Uno'] + yy
        self.entry_nacionalidad = ttk.Combobox(self, state="readonly")
        self.entry_nacionalidad['values'] = self.nacionalidades
        self.entry_nacionalidad.current(0)
        self.entry_nacionalidad.config(width=25)
        self.entry_nacionalidad.bind("<<ComboboxSelected>>")
        self.entry_nacionalidad.grid(row= 2, column=3,padx=10,pady=10, columnspan='1')
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#***************************Botones ***************
    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.btn_alta.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,
        bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_alta.grid(row= 3, column=0,padx=10,pady=10)

        self.btn_modi = tk.Button(self, text='Guardar', command= self.guardar_campos)
        self.btn_modi.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,
        bg='#0D2A83',cursor='hand2',activebackground='#7594F5',activeforeground='#000000')
        self.btn_modi.grid(row= 3, column=1,padx=10,pady=10)

        self.btn_cance = tk.Button(self, text='Cancelar', command=self.bloquear_campos)
        self.btn_cance.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,
        bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_cance.grid(row= 3, column=2,padx=10,pady=10)
#***************************Guardar peliculas***********************
    def guardar_campos(self):
        pelicula = Peliculas(
            self.nombre.get(), # recibe nombre
            self.duracion.get(),            
            self.entry_genero.current(), # correcta seleccion de combo box
            self.protagonista.get(),
            self.director.get(),
            self.entry_nacionalidad.current()
        ) # instancio

        if self.id_peli == None:
            guardar_peli(pelicula)
        else:
            editar_peli(pelicula,int(self.id_peli))

        self.bloquear_campos()
        self.mostrar_tabla()

#***************************Habilitar y bloquear***********************
    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_protagonista.config(state='normal')
        self.entry_director.config(state='normal')
        self.entry_genero.config(state='normal')
        self.entry_nacionalidad.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')
    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_protagonista.config(state='disabled')
        self.entry_director.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.entry_nacionalidad.config(state='disabled')
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.btn_alta.config(state='normal')
        self.nombre.set('')
        self.duracion.set('')
        self.protagonista.set('')
        self.director.set('')
        self.entry_genero.current(0)
        self.id_peli = None
        self.entry_nacionalidad.current(0)

#***************************Mostrar Tabla en ventana******
    def mostrar_tabla(self):
        self.lista_p = listar_peli()
        
        # reverse() = lista invertida
        self.lista_p.reverse()
        self.tabla = ttk.Treeview(self, columns=('Nombre','Duracion','Genero','Protagonista','Director','Nacionalidad'))
        self.tabla.grid(row=4,column=0,columnspan=4, sticky='nse')
        # sticky='nse' fija tabla

        self.scroll = ttk.Scrollbar(self, orient='vertical', command= self.tabla.yview)
        self.scroll.grid(row=4,column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Duración')
        self.tabla.heading('#3', text='Genero')
        self.tabla.heading('#4', text='Protagonista')
        self.tabla.heading('#5', text='Director')
        self.tabla.heading('#6', text='Nacionalidad')

        for p in self.lista_p:
            self.tabla.insert('',0,text=p[0],
                              values=(p[1],p[2],p[8],p[4],p[5],p[10]))

        self.btn_editar = tk.Button(self, text='Editar', command= self.editar_registro)
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,
        bg='#1C500B',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_editar.grid(row= 5, column=0,padx=10,pady=10)

        self.btn_delete = tk.Button(self, text='Delete', command= self.eliminar_registro)
        self.btn_delete.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' ,
        bg='#A90A0A',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_delete.grid(row= 5, column=1,padx=10,pady=10)

    #****************************Editar registro**************************
    def editar_registro(self):
        try:
            self.id_peli = self.tabla.item(self.tabla.selection())['text']

            self.nombre_peli = self.tabla.item(self.tabla.selection())['values'][0]
            self.dura_peli = self.tabla.item(self.tabla.selection())['values'][1]
            self.gene_peli = self.tabla.item(self.tabla.selection())['values'][2]
            self.prota_peli = self.tabla.item(self.tabla.selection())['values'][3]
            self.dire_peli = self.tabla.item(self.tabla.selection())['values'][4]
            self.nacio_peli = self.tabla.item(self.tabla.selection())['values'][5]

            self.habilitar_campos()
            self.nombre.set(self.nombre_peli)
            self.duracion.set(self.dura_peli)
            self.entry_genero.current(self.generos.index(self.gene_peli))
            self.protagonista.set(self.prota_peli)
            self.director.set(self.dire_peli)
            self.entry_nacionalidad.current(self.nacionalidades.index(self.nacio_peli))

        except:
            pass
    def eliminar_registro(self):
        resp = messagebox.askquestion("Pregunta 1","¿Quieres borrar registro?") #devuelve yes o no
        print
        if resp == "yes" :
            self.id_peli = self.tabla.item(self.tabla.selection())['text']
            borrar_peli(int(self.id_peli))
            self.mostrar_tabla()

#****************************MENU**************************

def barrita_menu(root):
    barra = tk.Menu(root)
    root.config(menu = barra, width = 300 , height = 300)
    menu_inicio = tk.Menu(barra, tearoff=0)
    menu_inicio2 = tk.Menu(barra, tearoff=0)
    # niveles #
    #principal
    barra.add_cascade(label='Inicio', menu = menu_inicio)
    barra.add_cascade(label='Consultas', menu = menu_inicio)
    barra.add_cascade(label='Acerca de..', menu = menu_inicio)
    barra.add_cascade(label='Ayuda', menu = menu_inicio2)
    #submenu
    menu_inicio.add_command(label='Conectar DB', command= crear_tabla)
    menu_inicio.add_command(label='Desconectar DB')
    menu_inicio.add_command(label='Salir', command= root.destroy)

    #submenu Ayuda
    menu_inicio2.add_command(label='Conectar DB')
    menu_inicio2.add_command(label='Buscar')
    menu_inicio2.add_command(label='Hola como estas')