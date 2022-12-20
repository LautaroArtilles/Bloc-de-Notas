
from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser



def abrirArchivo():
    archivo = filedialog.askopenfile(title="Abrir", initialdir="C:/", filetypes=[("Documentos de Texto","*.txt")])  #Metodo que permite abrir una ventana para buscar el archivo
    archivo = archivo.name
    
    if archivo is not None:
        blank.delete("1.0",END)  #Borra el Contenido de la ventana
        archivo = open(archivo,"r", encoding="utf-8")
        blank.insert("1.0",archivo.read())
         
        
def Nuevo():
    blank.delete("1.0", END)       
    
def Guardar():
    Texto = blank.get("1.0", END) # Guarda el contenido de todo el texto
    archivo = filedialog.asksaveasfilename(title="Guardar",initialdir="C:/", filetypes=[("Documentos de Texto","*.txt")],defaultextension=".txt")
    with open(archivo,"w") as data:
        data.write(Texto)
        
def Color_Fondo():
    color = colorchooser.askcolor()[1]
    blank.configure(bg = color)   
    
def Color_Texto():
    color = colorchooser.askcolor()[1]
    blank.configure(fg = color,insertbackground=color)          
        

ventana = Tk()
ventana.geometry("600x600")
ventana.title("Notepad")
ventana.iconbitmap("favicon.ico")
ventana.config(background="#212145")

#Paso1. Crear Barra de Menú
barraMenu = Menu(ventana)

#Paso2. Crear Menú
Archivo = Menu(barraMenu, tearoff=0)
Formato = Menu(barraMenu, tearoff=0)

#Paso3. Crear Comandos del menú
Archivo.add_command(label="Abrir", command=abrirArchivo)
Archivo.add_command(label="Nuevo", command=Nuevo)
Archivo.add_command(label="Guardar", command=Guardar)
Archivo.add_separator()
Archivo.add_command(label="Salir", command=ventana.destroy)

Formato.add_command(label="Color de Fondo", command=Color_Fondo)
Formato.add_command(label="Color de Texto", command=Color_Texto)

#Paso 4. Agregar los menús a la barra de Menú
barraMenu.add_cascade(label="Archivo",menu=Archivo)

barraMenu.add_cascade(label="Formato", menu=Formato)

#Paso 5. Indicar que la barra de menús estará en la ventana
ventana.config(menu=barraMenu)

# Agregar el contenedor para escribir
blank = Text(ventana, font=("Times New Roman",13),bg="#1f1f1f",fg="white",insertbackground="white",cursor="pencil", selectbackground="#1f1f8f")
blank.pack(expand= True,padx=30, pady=30)


ventana.mainloop()