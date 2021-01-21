from tkinter import *
from tkinter import ttk

def copiar(codigo,turno,texto):
    documento = "Código: " + codigo + "\n\n" + turno + "\n\n" + texto
    janela_tmp = Tk()
    janela_tmp.withdraw()
    janela_tmp.clipboard_clear()
    janela_tmp.clipboard_append(documento)
    janela_tmp.after(1, lambda: janela_tmp.destroy())
    janela_tmp.mainloop()


