from tkinter import *
import ttkbootstrap as ttk
from tkinter import messagebox
import openai


def key():
    openai.api_key = llave.get()  

    llave.set("")

def chatGpt():
    global respuesta

    mi_pregunta = pregunta.get()
    
    if mi_pregunta == "exit":
        raiz.destroy


    completion = openai. Completion.create(engine="text-davinci-003",
                            prompt= mi_pregunta,
                            max_tokens=2048)

    respuesta.set(completion.choices[0].text)      
        
raiz = ttk.Window(themename="vapor")
raiz.title("ChatBot-Davinci 003")
#icono = PhotoImage(file="chatp.gif")
#raiz.iconphoto(False, icono)
raiz.resizable(True, True)

frame = ttk.Frame(raiz)
frame.pack()

pregunta = StringVar()
respuesta = StringVar()
llave = StringVar()


etiquetallave = ttk.Label(frame,
                 text="Introduce la Key:",
                 justify=LEFT, 
                 font=("Arial", 10))
etiquetallave.grid(row=0, column=0, pady=20)

entryllave = ttk.Entry(frame, 
                    width=50, 
                    textvariable=llave)
entryllave.grid(row=0, column=1, pady=20)

botonllave = ttk.Button(frame, 
                       text="Conectar",
                       command=key)
botonllave.grid(row=0, column=2, pady=20)

info = ttk.Label(raiz, 
                 text="Introduce una pregunta:",
                 justify=CENTER, 
                 font=("Arial", 20))
info.pack(padx=5, pady=5)

info = ttk.Label(raiz, 
                 text="Actualizado hasta el 2020",
                 justify=CENTER, 
                 font=("Arial", 8))
info.pack(padx=5, pady=5)

entrada = ttk.Entry(raiz, 
                    width=100, 
                    textvariable=pregunta)
entrada.pack(padx=5, pady=10)

preguntar = ttk.Button(raiz, 
                       text="Preguntar",
                       command=chatGpt)
preguntar.pack(padx=5, pady=5)

info = Message(raiz,
                fg="#D3FDDA",
                bg="#190831",
                textvariable=respuesta, 
                font=("Arial", 13))
info.pack(padx=5, pady=5)



raiz.mainloop()