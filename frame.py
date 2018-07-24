from tkinter import *

#configuracion de la raiz
root = Tk()
root.title('Hola Mundo')
root.resizable(1,1)
root.iconbitmap('hola.ico')

frame = Frame(root, width=480, height=380)
frame.pack(fill='both ', expand=1)
frame.config(cursor='pirate')
frame.config(bg='lightblue')
frame.config(bd=25)
frame.config(relief='sunken')



root.config(cursor='arrow')
root.config(bg='blue')
root.config(bd=15)
root.config(relief='ridge')

#debe ir abajo del todo
root.mainloop()  