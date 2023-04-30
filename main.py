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
        messagebox.showerror("Advertencia","Debes elegir un archivo valido")



move=60
movey=20

bnt_nuevo = Button(raiz,text="Nuevo",height=1,width=20,background="#3352FF",anchor="center",font=("Arial Black",14),command=lambda:SeleccionarArchivo(),borderwidth = 0)
bnt_nuevo.place(x=move,y=movey)

bnt_abrir = Button(raiz,text="Abrir Archivo",height=1,width=20,background="#3352FF",anchor="center",font=("Arial Black",14),command=lambda:SeleccionarArchivo(),borderwidth = 0)
bnt_abrir.place(x=(move+330),y=movey)

bnt_guardar = Button(raiz,text="Guardar",height=1,width=20,background="#3352FF",anchor="center",font=("Arial Black",14),command=lambda:SeleccionarArchivo(),borderwidth = 0)
bnt_guardar.place(x=(move+660),y=movey)

bnt_guardar_como = Button(raiz,text="Guardar Como",height=1,width=20,background="#3352FF",anchor="center",font=("Arial Black",14),command=lambda:SeleccionarArchivo(),borderwidth = 0)
bnt_guardar_como.place(x=(move+990),y=movey)

bnt_salir= Button(raiz,text="Guardar Como",height=1,width=20,background="#3352FF",anchor="center",font=("Arial Black",14),command=lambda:SeleccionarArchivo(),borderwidth = 0)
bnt_salir.place(x=(move+1320),y=movey)
    

def callback(event):
    print("clicked at", event.x, event.y)
    print(text.index(CURRENT).split("."))

text.bind("<Button-1>",callback)



raiz.mainloop()