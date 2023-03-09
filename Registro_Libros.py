from tkinter import *
#import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
from io import open


#----------------FUNCIONES-----------------------------------------------
def salirAplicación():
    valor = messagebox.askquestion("Salir", "¿Deséa salir de la aplicación")
    if valor == "yes":
        raiz.destroy()


def insertar_Datos():
    mi_Orden = miOrden.get()
    mi_Autor = miAutor.get()
    mi_Apellido = miApellido.get()
    mi_Libro = miLibro.get()
    mi_Comentario = miComentario.get()

#-----Creacion del archivo txt de la lista de libros---------------
    file = open("Libreria_de_Casa.txt", "a+", encoding="utf-8")
    file.write(mi_Orden + "\t")
    file.write(mi_Autor + "\t")
    file.write(mi_Apellido + "\t")
    file.write(mi_Libro + "\t")
    file.write(mi_Comentario + "\n")
    
    messagebox.showinfo("Insertar", "Registro ralizado con exito")

    lista = file.read()

    file.close()





#-------------Borrar los Campos de los Entry--------------------
def borrar_Campos():
    miOrden.set("")
    miAutor.set("")
    miApellido.set("")
    miLibro.set("")
    miComentario.set("")




raiz = ttk.Window(themename="vapor")
raiz.title("Libros de Casa")
#raiz.config(width=300, height=200)
raiz.iconbitmap("librero.ico")
raiz.resizable(0, 0)


#----Ventana Label----------
ventana_Datos = LabelFrame(raiz, text="Insertar Datos")
ventana_Datos.grid(row=0, column=0, sticky="news")

#-----------Ventana Botones------------
ventana_Botones = LabelFrame(raiz)
ventana_Botones.grid(row=1, column=0, sticky="news")

#-----------Ventana Cuadro Texto------------
ventana_Texto = Frame(raiz, width=80, height=300)
ventana_Texto.grid(row=2, column=0)


#----------------Barra Menus------------------
barra_Menu = ttk.Menu(raiz)
raiz.config(menu=barra_Menu, width=250)
#--------Pestañas--------
menu_Salir = ttk.Menu(barra_Menu, tearoff=0)
barra_Menu.add_cascade(label="Salir", menu=menu_Salir)
menu_Salir.add_command(label="Cerrar", command=salirAplicación)

menu_Editar = ttk.Menu(barra_Menu, tearoff=0)
barra_Menu.add_cascade(label="Editar", menu=menu_Editar)
menu_Editar.add_command(label="Modificar")
menu_Editar.add_command(label="Imprimir")
menu_Editar.add_command(label="Crear PDF")

menu_Ayuda = ttk.Menu(barra_Menu, tearoff=1)
barra_Menu.add_cascade(label="Ayuda", menu=menu_Ayuda)
menu_Ayuda.add_command(label="Licencia")
menu_Ayuda.add_command(label="Acerca de..")


#----------------Etiquetas---------------------
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
                        text="Comentarios",                        
                        font=8).grid(row=4, column=0, padx=5, pady=10, sticky="e")


#---------------Variables de los Entry-------------------------
miOrden = StringVar()
miAutor = StringVar()
miApellido = StringVar()
miLibro = StringVar()
miComentario= StringVar()


#----------------Entradas-----------------------------------
entryOrden = Entry(ventana_Datos, 
                    width=10, fg="#00F6FA", textvariable=miOrden).grid(row=0, column=1, padx=20, sticky="w")

entryAutor = Entry(ventana_Datos, 
                    width=25, fg="#00F6FA", textvariable=miAutor).grid(row=1, column=1, padx=20, sticky="w")

entryApellido = Entry(ventana_Datos, 
                    width=25, fg="#00F6FA", textvariable=miApellido).grid(row=2, column=1, padx=20, sticky="w")

entryLibro = Entry(ventana_Datos, 
                    width=50, fg="#00F6FA", textvariable=miLibro).grid(row=3, column=1, padx=20, sticky="w")

entryComentario = Entry(ventana_Datos, 
                        width=50, fg="#00F6FA", textvariable=miComentario).grid(row=4, column=1, padx=20, sticky="w")



#------------Botones--------------------------------------

boton_Insertar = Button(ventana_Botones,
                           text="Insertar", command=insertar_Datos).grid(row=0, column=0, padx=40, pady=10)

boton_Leer = Button(ventana_Botones, 
                           text="Leer").grid(row=0, column=1, padx=40, pady=10)

boton_Modificar = Button(ventana_Botones, 
                           text="Modificar").grid(row=0, column=2, padx=40, pady=10)

boton_BorrarCampos = Button(ventana_Botones, 
                           text="Borrar Campos", command=borrar_Campos).grid(row=0, column=3, padx=40, pady=10)


#------------Barra Desplazadora----------------------



#-------------Ventana de Texto-----------------------
cuadro_Texto = Text(ventana_Texto,
                       width=50, height=8,
                       pady=20,
                      font=("Times New Roman", 13))
cuadro_Texto.config(fg="#00F6FA")
cuadro_Texto.grid(row=3, column=0, sticky="news")
#cuadro_Texto.config(yscrollcommand=barra_desplaza.set)

barra_desplaza = Scrollbar(ventana_Texto, orient=VERTICAL, command=cuadro_Texto.yview)
barra_desplaza.grid(row=3, column=1, sticky="news")
cuadro_Texto.config(yscrollcommand=barra_desplaza.set)



raiz.mainloop()
