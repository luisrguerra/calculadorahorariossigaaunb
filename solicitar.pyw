from tkinter import *
from tkinter import ttk
import os.path #para checar se o arquivo existe
import fechar

codigo_tmp = ""
fundo = 'white'
icone = ""
tamanho_texto = 12
fonte = ""
fonte_cor = "black"

def codigo_get(titulo,texto):
    global codigo_tmp
    global icone

    icone_existe = os.path.exists(icone)

    janela_codigo = Tk()
                
    #janela_codigo.lift()
    janela_codigo.attributes('-topmost', True)
    janela_codigo.attributes('-topmost', False)
    janela_codigo.configure(background = fundo)
    #janela_codigo.configure(height = 1000)
    janela_codigo.configure(padx = 10)
    janela_codigo.configure(pady = 10)
    janela_codigo.title(titulo)

    
    texto = Label(janela_codigo, text=texto, fg = fonte_cor, font = (fonte,tamanho_texto), background = fundo)
    
    texto.pack(anchor = NW)
    
    entrada = ttk.Entry(janela_codigo, font=(fonte, tamanho_texto))
    entrada.focus()
    entrada.pack(anchor = SW, fill = X, pady = 10)
        
    def get_codigo(event=None):
        global codigo_tmp
        codigo_tmp = entrada.get()
        if codigo_tmp != "":
           janela_codigo.destroy()

    entrada.bind('<Return>', get_codigo)  
    botao = ttk.Button(janela_codigo, text="Calcular", command = get_codigo)
    botao.pack(anchor = SE) 

    janela_codigo.resizable(False,False)
    janela_codigo.protocol("WM_DELETE_WINDOW", fechar.programa)
    janela_codigo.eval('tk::PlaceWindow . center')
    
    if icone_existe == True:
       janela_codigo.iconbitmap(icone)

    janela_codigo.mainloop()
    return codigo_tmp
