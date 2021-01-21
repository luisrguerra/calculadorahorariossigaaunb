from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import salvar

def resultado(codigo,turno,texto):
    
    documento = "Código: " + codigo + "\n\n" + turno + "\n\n" + texto
    formatos = (("Arquivo de texto", "*.txt"),("Outro Formato", "*"))

    arquivo = filedialog.asksaveasfilename( initialfile = codigo, filetypes = formatos, defaultextension = formatos)
    #arquivo = "salvo\\" + codigo + ".txt"
    if arquivo != "":
       salvar.texto(documento, arquivo)


