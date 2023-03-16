from tkinter import *
import ttkbootstrap as ttk
from tkinter import messagebox
from io import open
import openai



#----------------FUNCIONES-----------------------------------------------
def salirAplicación():
    valor = messagebox.askquestion("Salir", "¿Deséa salir de la aplicación")
    if valor == "yes":
        raiz.destroy()

#----------------Añadiendo libros en el archivo txt.--------------
def insertar_Datos():
        
    mi_Orden = miOrden.get()
    mi_Autor = miAutor.get()
    mi_Apellido = miApellido.get()
    mi_Libro = miLibro.get()
    mi_Comentario = miComentario.get()
    
    try:
        file = open("Libreria_de_Casa.txt", "r", encoding="utf-8")
        valorfila = file.readlines()
        fila = len(valorfila)
        file.close()
        
    except FileNotFoundError:
        file = open("Libreria_de_Casa.txt", "a", encoding="utf-8")
        file.close()
            
    mi_Orden = int(mi_Orden, base=10)   
    if mi_Orden <= fila:
        messagebox.showinfo("Modificar", f"El numero de la lista ya esta en uso.\n Su ultima etrada es la nº{fila}")
        miOrden.set("")
        
    else:  
#-----------------Creacion del archivo txt de la lista de libros-------------------------
        mi_Orden = str(mi_Orden)
        file = open("Libreria_de_Casa.txt", "a+", encoding="utf-8")
        file.write(mi_Orden + "\t")
        file.write(mi_Autor + "\t\t")
        file.write(mi_Apellido + "\t\t")
        file.write(mi_Libro + "\t\t\t")
        file.write(mi_Comentario + "\n")
        file.close()
        messagebox.showinfo("Insertar", "Registro ralizado con exito")
        file.close()
        def insertar_Tabla():
            tabla.insert("", END, text=mi_Orden, values=(mi_Autor, mi_Apellido, mi_Libro, mi_Comentario))
    
        insertar_Tabla()

#---------------Muestra el listado creado en una ventana distita-----------------
def mostrar_Lista():

    ventana_Lista= ttk.Toplevel()
    ventana_Lista.title("Lista de Libros Guardados")
    lista = open("Libreria_de_Casa.txt", "r")
    extraerTexto = lista.read()
    #----------Estas dos lineas hacen que aparezca el mismo icono en este  nivel----------------
    iconoVentana = PhotoImage(file="icono.png")
    ventana_Lista.iconphoto(False, iconoVentana)

        
    botonCerrar = Button(
        ventana_Lista,
        text="Cerrar",
        command=ventana_Lista.destroy    
    )
    botonCerrar.pack(side=BOTTOM)
    
    archivoLista = Label(ventana_Lista, justify='left',
                        text=extraerTexto,
                        font=5
    )
    archivoLista.pack(padx=30)
    lista.close()

    '''¡barra_desplaza = Scrollbar(ventana_Lista, orient=VERTICAL)
    barra_desplaza.pack( side=RIGHT, fill=Y)
    barra_desplaza.config(command=ventana_Lista.yview)'''

    
#-------------Borrar los Campos de las Entradas(Entry)--------------------
def borrar_Campos():
    miOrden.set("")
    miAutor.set("")
    miApellido.set("")
    miLibro.set("")
    miComentario.set("")

def borrar_Linea():
    eliminar_Linea = ttk.Toplevel()
    eliminar_Linea.config(width=100, height=100)
    eliminar_Linea.title("Eliminar Linea")
    lista = open("Libreria_de_Casa.txt", "a+")
    linea = lista.readlines()
    lista = len(linea)
    #----------Estas dos lineas hacen que aparezca el mismo icono en este  nivel----------------
    iconoVentana = PhotoImage(file="icono.png")
    eliminar_Linea.iconphoto(False, iconoVentana)
 
    archivoLista = Label(eliminar_Linea,
                        text="Elija la linea a eliminar",
                        font=5)
    archivoLista.pack(padx=20, pady=20)

    
    caja_Elegir = Spinbox(eliminar_Linea,
                          values= lista,
                          increment=1,
                          state="readonly",
                          command=linea_Eliminada,
                          font=5)
    caja_Elegir.pack(padx=20, pady=20)

    def linea_Eliminada():
        lista.delete()

    
    botonCerrar = Button(
        eliminar_Linea,
        text="Cerrar",
        command=eliminar_Linea.destroy)
    botonCerrar.pack(side=BOTTOM)

    lista.close()

#-------------Interfaz Chat-------------------------------

def chat():
    chatgpt = ttk.Toplevel()
    chatgpt.config(width=200, height=100)
    chatgpt.title("Chat-Davinci")
    openai.api_key ="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"
    global respuesta

    mi_pregunta = pregunta.get()
    
    completion = openai. Completion.create(engine="text-davinci-003",
                            prompt= mi_pregunta,
                            max_tokens=2048)

    respuesta.set(completion.choices[0].text)      
        
    pregunta = StringVar()
    respuesta = StringVar()

    info = ttk.Label(chatgpt, 
                     text="Introduce una pregunta:",
                     justify=CENTER, 
                     font=("Arial", 20))
    info.pack(padx=5, pady=5)

    info = ttk.Label(chatgpt, 
                     text="Información actualizada hasta el 2020",
                     justify=CENTER, 
                     font=("Arial", 8))
    info.pack(padx=5, pady=5)

    entrada = ttk.Entry(chatgpt, 
                        width=100, 
                        textvariable=pregunta)
    entrada.pack(padx=5, pady=5)

    preguntar = ttk.Button(chatgpt, 
                           text="Preguntar",
                           command=chatGpt)
    preguntar.pack(padx=5, pady=5)

    info = Message(chatgpt,
                    fg="#D3FDDA",
                    bg="#2b3e50",
                    textvariable=respuesta, 
                    font=("Arial", 10))
    info.pack(padx=5, pady=5)


#----------------------------------Ventana Principal-----------------------------------
raiz = ttk.Window(themename="superhero")
raiz.title("Libros de Casa")
raiz.config(width=500, height=300, padx=10, pady=10)
icono = PhotoImage(file="icono.png")
raiz.iconphoto(False, icono)
raiz.resizable(0, 0)

#----Ventana para las etiquetas de los diferentes campos(Label)----------
ventana_Datos = LabelFrame(raiz, text="Insertar Datos", padx=10, pady=10)
ventana_Datos.grid(row=0, column=0, sticky="news")

#-----------Ventana Botones de acción------------
ventana_Botones = LabelFrame(raiz, text="Acciones",)
ventana_Botones.grid(row=1, column=0, sticky="news")

#-----------Ventana donde se actualizas los libros ingresados------------
ventana_Tabla = Frame(raiz, padx=10, pady=10)
ventana_Tabla.grid(row=2, column=0)


#---------------------------------Barra Menus---------------------------------------------------
barra_Menu = ttk.Menu(raiz)
raiz.config(menu=barra_Menu, width=250)
#--------Pestañas--------
menu_Salir = ttk.Menu(barra_Menu, tearoff=0)
barra_Menu.add_cascade(label="Salir", menu=menu_Salir)
menu_Salir.add_command(label="Cerrar", command=salirAplicación)

menu_Editar = ttk.Menu(barra_Menu, tearoff=0)
barra_Menu.add_cascade(label="Editar", menu=menu_Editar)
menu_Editar.add_command(label="Chat", command=chat)
menu_Editar.add_command(label="Imprimir")
menu_Editar.add_command(label="Crear PDF")

menu_Ayuda = ttk.Menu(barra_Menu, tearoff=0)
barra_Menu.add_cascade(label="Ayuda", menu=menu_Ayuda)
menu_Ayuda.add_command(label="Licencia")
menu_Ayuda.add_command(label="Acerca de..")

#---------------Variables de los Entry-------------------------
miOrden = StringVar()
miAutor = StringVar()
miApellido = StringVar()
miLibro = StringVar()
miComentario= StringVar()



#----------------Etiquetas de los campos---------------------
labelOrden = Label(ventana_Datos, 
                       text="Nº Orden",                        
                       font=8).grid(row=0, column=0, padx=5, pady=10, sticky="e")

labelAutor = Label(ventana_Datos, 
                       text="Nombre Autor",                       
                       font=8).grid(row=1, column=0, padx=5, pady=10, sticky="e")

labelApelli = Label(ventana_Datos, 
                        text="Apellido Autor",                         
                        font=8).grid(row=2, column=0, padx=5, pady=10, sticky="e")

labelLibro = Label(ventana_Datos, 
                       text="Libro",                       
                       font=8).grid(row=3, column=0, padx=5, pady=10, sticky="e")

labelComent = Label(ventana_Datos, 
                        text="Descripción",                        
                        font=8).grid(row=4, column=0, padx=5, pady=10, sticky="e")


#----------------Entradas para rellenar los diferentes campos-----------------------------------
entryOrden = ttk.Entry(ventana_Datos,
                        font=("Arial", 10), 
                        width=10, 
                        textvariable=miOrden).grid(row=0, column=1, padx=20, sticky="w")

entryAutor = ttk.Entry(ventana_Datos,
                        font=("Arial", 10), 
                        width=25, 
                        textvariable=miAutor).grid(row=1, column=1, padx=20, sticky="w")

entryApellido = ttk.Entry(ventana_Datos,
                        font=("Arial", 10), 
                        width=25, 
                        textvariable=miApellido).grid(row=2, column=1, padx=20, sticky="w")

entryLibro = ttk.Entry(ventana_Datos, 
                        font=("Arial", 10),
                        width=50, 
                        textvariable=miLibro).grid(row=3, column=1, padx=20, sticky="w")

entryComentario = ttk.Entry(ventana_Datos, 
                        font=("Arial", 10),
                        width=50, 
                        textvariable=miComentario).grid(row=4, column=1, padx=20, sticky="w")



#------------Botones de acciones--------------------------------------

boton_Insertar = ttk.Button(ventana_Botones,
                           text="Insertar", 
                           command=insertar_Datos).grid(row=0, column=0, padx=40, pady=10)

boton_Leer = ttk.Button(ventana_Botones, 
                           text="Ventana Lista", 
                           command=mostrar_Lista).grid(row=0, column=1, padx=40, pady=10)

boton_Modificar = ttk.Button(ventana_Botones, 
                           text="Eliminar Linea", 
                           command=borrar_Linea).grid(row=0, column=2, padx=40, pady=10)

boton_BorrarCampos = ttk.Button(ventana_Botones, 
                           text="Borrar Campos", 
                           command=borrar_Campos).grid(row=0, column=3, padx=40, pady=10)


#------------Tabla de Datos que se muestra en el fondo de la aplicación----------------
tabla = ttk.Treeview(ventana_Tabla, columns=["col1", "col2", "col3", "col4"])
tabla.column("#0", width=50)
tabla.column("col1", width=80, anchor=CENTER)
tabla.column("col2", width=80, anchor=CENTER)
tabla.column("col3", width=150, anchor=CENTER)
tabla.column("col4", width=200, anchor=CENTER)

tabla.heading("#0", text="Nº Orden", anchor=CENTER)
tabla.heading("col1", text="Nombre", anchor=CENTER)
tabla.heading("col2", text="Apellido", anchor=CENTER)
tabla.heading("col3", text="Libro", anchor=CENTER)
tabla.heading("col4", text="Comentarios", anchor=CENTER)
tabla.pack()


raiz.mainloop()