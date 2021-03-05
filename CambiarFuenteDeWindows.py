# Programa para cambiar la fuente del sistema #
# Resulta que en windows ya no se permite cambiar la fuente del sistema, por ello podemos recurrir a unas lineas de código para cambiar 
# el registro del sistema. Podemos crear un archivo *.reg que al ejecutar cambie la fuente por lo que hayamos especificado en sus lineas.

# Conseguir acceso a la carpeta donde se alojan las fuentes instaladas en el sistema normalmente C:/Widows/Fonts

# Importamos las bibliotecas necesarias
import os, sys, shutil
from subprocess import call
import tkinter as tk
from tkinter import ttk

nombre_archivo = ""

# Definimos un método que creará un archivo *.reg con el nombre de la nueva fuente
# Definir funcion para ejecutar el archivo de registro
def ejecutar():
    os.system(nombre_archivo + ".reg")

# Definir el texto que será escrito
nombre_fuente = ""
def registrar():
    # Recogemos el valor seleccionado en el combobox
    global nombre_fuente
    global nombre_archivo

    nombre_fuente = combo.get()
    nombre_archivo = nombre_tf.get() 

    # intenta reemplazar las extensiones y si falla pasa al siguiente DE FORMA AUTOMATICA
    nombre_fuente = nombre_fuente.replace(".ttf","")
    nombre_fuente = nombre_fuente.replace(".TTF","")
    print("Nuevo nombre de fuente " + nombre_fuente + " nombre archivo" + nombre_archivo)

    nueva_fuente = '"Segoe UI"="'+nombre_fuente+'"'
    print("la nueva fuente aparece como " + nueva_fuente)

    texto_base = ("Windows Registry Editor Version 5.00\n"
    + '[HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Fonts]\n'
    + '"Segoe UI (TrueType)"=""'
    + '"Segoe UI Bold (TrueType)"=""\n'
    + '"Segoe UI Bold Italic (TrueType)"=""\n'
    + '"Segoe UI Italic (TrueType)"=""\n'
    + '"Segoe UI Light (TrueType)"=""\n'
    + '"Segoe UI Semibold (TrueType)"=""\n'
    + '"Segoe UI Symbol (TrueType)"=""\n'
    + '[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\FontSubstitutes]\n'
    + nueva_fuente)

    # Crea el archivo con el nuevo nombre de la fuente
    file = open(nombre_archivo + ".reg","w")
    file.write(texto_base)
    file.close()

    ejecutar()

# Listaremos los archivos de ese directorio
fuentes = os.listdir("C:/Windows/Fonts")
fuentes_ttf = []
# Contruimos un bucle que se ejecute el len(tamaño) de la lista veces y que imprima cada fuente que SON SOLO LOS ARCHIVOS *.TTF
for a in range(len(fuentes)):
    if(".ttf" in fuentes[a] or ".TTF" in fuentes[a]):
        print(fuentes[a])
        fuentes_ttf.append(fuentes[a])
    #else:
        #print("ignorado por no ser ttf: " + fuentes[a])

ventana = tk.Tk()
boton_aceptar = tk.Button("Change Font")

ventana.geometry("450x235")

# Etiqueta encima de la lista de fuentes
fuentes_lb = tk.Label(ventana,text="Fuentes del Sistema")
fuentes_lb.place(x=50,y=20)

# lista de fuentes del sistema
combo = ttk.Combobox(ventana)
combo.place(x=50, y=50)
combo["values"] = fuentes_ttf
combo.bind("<<ComboboxSelected>>" )

# Boton aceptar que recoge la opcion del ComboBox para crear el archivo

boton_aceptar = tk.Button(ventana,command=registrar,width=15,height=1,text="Registrar")
boton_aceptar.place(x=250,y=50)

nombre_lb = tk.Label(ventana,text="Nombre de Archivo")
nombre_lb.place(x=50,y=75)

nombre_tf = tk.Entry(ventana)
nombre_tf.place(x=50,y=100)

ventana.mainloop()