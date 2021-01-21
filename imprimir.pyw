from tkinter import *
from tkinter import ttk
import os.path #para checar se o arquivo existe

import fechar
import salvamento
import clipboard

fundo = 'white'
icone = ""
tamanho_texto = 12
fonte = ""
fonte_cor = "black"

icone_salvar = "data\\save.png"
icone_copiar = "data\\copiar.png"


def resultado(titulo,codigo,modo,texto,botao):

    icone_existe = os.path.exists(icone)
    icone_salvar_existe = os.path.exists(icone_salvar)
    icone_copiar_existe = os.path.exists(icone_copiar)

    codigo_imprimir = "Código: " + codigo
    turno = ""
    if modo == "manha":
        turno = "Turno: manhã"
    if modo == "tarde":
       turno = "Turno: tarde"
    if modo == "noite":
       turno = "Turno: noite"
    janela = Tk()

    #janela.lift()
    janela.attributes('-topmost', True)
    janela.attributes('-topmost', False)
        
    #janela.geometry('350x200')
    janela.minsize(300,10)
    janela.configure(background= fundo)
    janela.configure(height = 1000)
    janela.configure(padx = 0)
    janela.configure(pady = 0)
    janela.title(titulo)

    barra_decima = Frame()
    #barra_decima.configure(padx = 5)
    #barra_decima.configure(pady = 5)
    barra_decima.configure(background = fundo)
    barra_decima.pack(expand = True, fill = BOTH,anchor = NW, side = TOP)

    

    def salvamento_btn():
        salvamento.resultado(codigo,turno,texto)
    
    def copiar_btn():
        clipboard.copiar(codigo,turno,texto)



    corpo = Frame()
    corpo.pack(expand = True, fill = BOTH)
    corpo.configure(padx = 10)
    corpo.configure(pady = 10)
    corpo.configure(background= fundo)


    botao_salvar = Button(barra_decima, text= "Salvar", command = salvamento_btn)
    botao_salvar.configure (background = fundo, activebackground = "#CCE4F7")
    botao_salvar.configure (padx= 10, pady= 5, borderwidth = 0)
    botao_salvar.configure (relief = FLAT)
    if icone_salvar_existe == True:
        imagem_icone_salvar = PhotoImage(file = icone_salvar) 
        botao_salvar.configure( image = imagem_icone_salvar, compound = LEFT)
    botao_salvar.pack(expand = False,anchor = NW, side = LEFT)


    botao_copiar = Button(barra_decima, text= "Copiar", command = copiar_btn)
    botao_copiar.configure (background = fundo, activebackground = "#CCE4F7")
    botao_copiar.configure (padx= 10, pady= 5, borderwidth = 0)
    botao_copiar.configure (relief = FLAT)
    if icone_copiar_existe == True:
        imagem_icone_copiar = PhotoImage(file = icone_copiar) 
        botao_copiar.configure( image = imagem_icone_copiar, compound = LEFT)
    botao_copiar.pack(expand = False,anchor = NW)




    texto_codigo = Label(corpo, fg = fonte_cor, text = codigo_imprimir, font=(fonte,tamanho_texto), justify = LEFT, background = fundo)
    texto_codigo.pack(expand = True, anchor = W)

    texto_turno = Label(corpo, text = turno, fg = fonte_cor, font=(fonte,tamanho_texto), justify = LEFT, background = fundo)
    texto_turno.pack(expand = True, anchor = W)

    texto_corpo = Label(corpo, text=texto, fg = fonte_cor, font=(fonte,tamanho_texto), justify = LEFT, background = fundo)
    texto_corpo.pack(expand = True, anchor = W)

    def fechar_resultado():
        janela.destroy()
            
    botao = ttk.Button(corpo, text= botao, command = janela.destroy)
    botao.pack(expand = True,anchor = SE,side = BOTTOM)
        
    janela.resizable(False,False)
    janela.protocol("WM_DELETE_WINDOW", fechar.programa)
    janela.eval('tk::PlaceWindow . center')
        
    if icone_existe == True:
       janela.iconbitmap(icone)

    janela.mainloop()
