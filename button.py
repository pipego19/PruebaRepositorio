from tkinter import *

def sumar():
	r.set(float(n1.get()) + float(n2.get()))
	borrar()

def borrar():
	n1.set("")
	n2.set("")

#Configuración de la raiz
root = Tk()
root.title('Calculadora')
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()


Label(root, text='numero 1').grid(row=0,column=0,padx=5,pady=5)
Entry(root, justify='center', textvariable=n1).grid(row=0,column=1,padx=5,pady=5) # primer numero
Label(root, text='numero 2').grid(row=1,column=0,padx=5,pady=5)
Entry(root, justify='center', textvariable=n2).grid(row=1,column=1,padx=5,pady=5) # segundo numero 
#Label(root, text='suma').grid(row=2,column=0,padx=5,pady=5)
Entry(root, justify='center', textvariable=r, state='disable').grid(row=2,column=1,padx=5,pady=5) # tercer numero


Button(root,text='Sumar',command=sumar).grid(row=2,column=0,padx=5,pady=5)



# Finalmente bucle de la aplicación
root.mainloop()