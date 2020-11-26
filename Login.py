import tkinter

ventana = tkinter.Tk()
ventana.geometry("500x600")

etiqueta = tkinter.Label(ventana, text="Log in")
etiqueta.pack()
etiqueta.config(fg="black", font=("BERNARD MT CONDENSED",24))

etiqueta = tkinter.Label(ventana, text="Usuario")
etiqueta.pack()
etiqueta.config(fg="black", font=("ARIAL",10))

cajaTexto1 = tkinter.Entry(ventana, bg="light blue")
cajaTexto1.pack()


etiqueta = tkinter.Label(ventana, text="Contraseña")
etiqueta.pack()
etiqueta.config(fg="black", font=("ARIAL",10))

cajaTexto2 = tkinter.Entry(ventana, bg="light blue")
cajaTexto2.pack()

def insesion():
    C1 = cajaTexto1.get()
    C2 = cajaTexto2.get()
    print(C1)
    print(C2)

boton1 = tkinter.Button(ventana, text="Iniciar sesión", command=insesion, bg="light blue")
boton1.pack()

ventana.mainloop()