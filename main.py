from tkinter import *
import ctypes
from tkinter import filedialog
from tkinter import messagebox 
import os
from datetime import datetime
from PIL import Image,ImageTk
import webbrowser


user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho=user32.GetSystemMetrics(0)
alto =user32.GetSystemMetrics(1)



#Corazon programa
grafico_archivo=""
texto_archivo=""
ruta_raiz=""
errores_documento=""

#Tamaño y configuracion de la ventana pricipan
altor=920
largor=508
dimensior="+"+str(int((ancho-largor)/2))+"+"+str(int((alto-altor)/2))
tamañor=str(900)+"x"+str(largor)
raiz=Tk()
raiz.config()

raiz.title("Proyecto 1")
raiz.geometry(dimensior)
raiz.geometry("1800x920")
raiz.iconbitmap("Imagenes/favicon.ico")
imagen=PhotoImage(file="Imagenes/BackGround.png")
background=Label(raiz,image=imagen)
background.place(x=0,y=0)


scrollbar =Scrollbar(raiz, orient=VERTICAL)
text = Text(raiz,height=30,width=80,wrap = "none",yscrollcommand=scrollbar.set)

text.place(x=50,y=100)
scrollbar.place(in_=text, relx=1, relheight=1, bordermode="outside")
scrollbar.config(command=text.yview)

scrollbar1 =Scrollbar(raiz, orient=VERTICAL)
text1 = Text(raiz,height=30,width=80,wrap = "none",yscrollcommand=scrollbar1.set)

text1.place(x=900,y=100)
scrollbar1.place(in_=text1, relx=1, relheight=1, bordermode="outside")
scrollbar1.config(command=text1.yview)


line=StringVar()
line.set("Linea: ")
column=StringVar()
column.set("Columna: ")
x=StringVar()
x.set("X: ")
y=StringVar()
y.set("Y: ")
#etiquetas posicion
Linea=Label(raiz,textvariable=line,width=10,font=("Arial Black",11)).place(x=50,y=700)
Columna=Label(raiz,textvariable=column,width=11,font=("Arial Black",11)).place(x=180,y=700)
Cx=Label(raiz,textvariable=x,width=11,font=("Arial Black",11)).place(x=323,y=700)
Cy=Label(raiz,textvariable=y,width=11,font=("Arial Black",11)).place(x=465,y=700)

def Nuevo():
    global text
    global ruta_raiz
    texto_editor=text.get("1.0","end")
    def GuardarArchivoComo():
        global texto_archivo
        filename=filedialog.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        try:
            ruta=str(filename)
            new=open(ruta,"w")
            new.write(texto_editor)
            new.close()
            messagebox.showinfo("Aviso", "Archivo guardado correctamente")
        except:
            messagebox.showerror("Advertencia", "Tienes que elegir una ruta y un nombre para el guardado")
    
    if texto_editor!="\n":
        guardar=messagebox.askyesno(message="¿Quieres guardar el archivo?", title="Guardar")
        if guardar==True:
            GuardarArchivoComo()
            text.delete("1.0","end")
            ruta_raiz=""
        else:
            text.delete("1.0","end")
            ruta_raiz=""
            messagebox.showinfo("Notificacion","Editor limpiado correctamente")
    else:
        text.delete("1.0","end")
        ruta_raiz=""
        messagebox.showinfo("Notificacion","Editor limpiado correctamente")

    

    





move=60
movey=20

bnt_nuevo = Button(raiz,text="Nuevo",height=1,width=20,background="#3352FF",anchor="center",font=("Arial Black",14),command=lambda:Nuevo(),borderwidth = 0)
bnt_nuevo.place(x=move,y=movey)


def Abrir():
    global text
    texto_editor=text.get("1.0","end")
    def GuardarArchivoComo():
        global texto_archivo
        filename=filedialog.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
        try:
            ruta=str(filename)
            new=open(ruta,"w")
            new.write(texto_editor)
            new.close()
            messagebox.showinfo("Aviso", "Archivo guardado correctamente")
        except:
            messagebox.showerror("Advertencia", "Tienes que elegir una ruta y un nombre para el guardado")
    
    def SeleccionarArchivo():
        
        filename = filedialog.askopenfilename(title = "Selecciona un archivo",filetypes = (("Text files","*.txt*"),("all files","*.*")))
        try:
            ruta=str(filename)
            file=open(ruta,"r")
            escritura=""
            texto_crudo=file.readlines()
            for i in texto_crudo:
                escritura+=i
            global ruta_raiz
            ruta_raiz=ruta

            file.close()
            text.delete("1.0","end")
            text.insert('1.0',escritura)
        except:
            messagebox.showerror("Advertencia", "Tienes que elegir una ruta y un nombre para el guardado")
    
    if texto_editor!="\n":
        guardar=messagebox.askyesno(message="¿Quieres guardar el archivo?", title="Guardar")
        if guardar==True:
            GuardarArchivoComo()
            text.delete("1.0","end")
            SeleccionarArchivo()
        else:
            text.delete("1.0","end")
            SeleccionarArchivo()
    else:
        text.delete("1.0","end")
        SeleccionarArchivo()



bnt_abrir = Button(raiz,text="Abrir Archivo",height=1,width=20,background="#3352FF",anchor="center",font=("Arial Black",14),command=lambda:Abrir(),borderwidth = 0)
bnt_abrir.place(x=(move+330),y=movey)

def Guardar():
    global ruta_raiz
    global text
    def GuardaDocumento():
        if ruta_raiz=="":
            messagebox.showerror("Advertencia", "Tienes que cargar un archivo primero")
        else:
            file=open(ruta_raiz,"w")
            file.write(text.get("1.0","end"))
            file.close()
            messagebox.showinfo("Aviso", "Archivo guardado correctamente")
    print(ruta_raiz)
    if ruta_raiz=="":
        messagebox.showerror("Advertencia", "Tienes que cargar un archivo primero")
    else:
        GuardaDocumento()


bnt_guardar = Button(raiz,text="Guardar",height=1,width=20,background="#3352FF",anchor="center",font=("Arial Black",14),command=lambda:Guardar(),borderwidth = 0)
bnt_guardar.place(x=(move+660),y=movey)

def GuardarArchivoComo():
    global text
    texto_editor=text.get("1.0","end")
    filename=filedialog.asksaveasfilename(initialdir = "/",title = "Guardar como",filetypes = (("txt files","*.txt"),("todos los archivos","*.*")))
    try:
        ruta=str(filename)
        new=open(ruta,"w")
        new.write(texto_editor)
        new.close()
        messagebox.showinfo("Aviso", "Archivo guardado correctamente")
    except:
        messagebox.showerror("Advertencia", "Tienes que elegir una ruta y un nombre para el guardado")
    

bnt_guardar_como = Button(raiz,text="Guardar Como",height=1,width=20,background="#3352FF",anchor="center",font=("Arial Black",14),command=lambda:GuardarArchivoComo(),borderwidth = 0)
bnt_guardar_como.place(x=(move+990),y=movey)

def Salir():
    raiz.destroy()

bnt_salir= Button(raiz,text="Salir",height=1,width=20,background="#3352FF",anchor="center",font=("Arial Black",14),command=lambda:Salir(),borderwidth = 0)
bnt_salir.place(x=(move+1320),y=movey)

bnt_analizar= Button(raiz,text="Analizar",height=1,width=20,background="#3352FF",anchor="center",font=("Arial Black",14),command=lambda:SeleccionarArchivo(),borderwidth = 0)
bnt_analizar.place(x=310,y=800)

bnt_tokens= Button(raiz,text="Tokens",height=1,width=20,background="#3352FF",anchor="center",font=("Arial Black",14),command=lambda:SeleccionarArchivo(),borderwidth = 0)
bnt_tokens.place(x=1000,y=750)

bnt_errores= Button(raiz,text="Errores",height=1,width=20,background="#3352FF",anchor="center",font=("Arial Black",14),command=lambda:SeleccionarArchivo(),borderwidth = 0)
bnt_errores.place(x=1330,y=750)

def callback(event):
    var=text.index(CURRENT).split(".")
    y.set("Y: "+str(event.y))
    x.set("X: "+str(event.x))
    line.set("Linea: "+var[0])
    column.set("Columna: "+str(int(var[1])+1))

text.bind("<Button-1>",callback)



raiz.mainloop()