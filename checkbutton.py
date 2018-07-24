from tkinter import *

def seleccionar():
	cadena = ""
	if (leche.get()):
		cadena+='con leche'
	else:
		cadena+= 'sin leche'

	if (azucar.get()):
		cadena+=' y con azucar'
	else:
		cadena+= ' y sin azucar'

	monitor.config(text=cadena)

#Configuración de la raiz
root = Tk()
root.title('Cafeteria')
root.config(bd = 15)
root.iconbitmap('hola.ico')

leche = IntVar() #1 si, 0 no
azucar = IntVar() #1 si, 0 no

imagen = PhotoImage(file='imagen.gif')
Label(root, image=imagen).pack(side='left')

frame=Frame(root)
frame.pack(side='left')

Label(frame, text='¿como quieres el café?').pack(anchor='w')
Checkbutton(frame, text='Con leche', variable=leche, onvalue=1, offvalue=0, command=seleccionar).pack(anchor='w')
Checkbutton(frame, text='Con Azucar', variable=azucar, onvalue=1, offvalue=0, command=seleccionar).pack(anchor='w')

monitor = Label(frame)
monitor.pack()

# Finalmente bucle de la aplicación
root.mainloop()