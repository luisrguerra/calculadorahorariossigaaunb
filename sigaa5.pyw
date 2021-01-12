from tkinter import *
from tkinter import ttk
import os

def fechar():
    os._exit(0)

while True:
    cor_fundo = 'white'
    fonte_texto = "Arial"
    tamanho_texto = 12
    tamanho_titulo = 16

    codigo = ""

    def solicitar_codigo(titulo,texto):
        
        janela_codigo = Tk()
        
        
        #janela_codigo.lift()
        janela_codigo.attributes('-topmost', True)
        janela_codigo.attributes('-topmost', False)
        janela_codigo.configure(background = cor_fundo)
        #janela_codigo.configure(height = 1000)
        janela_codigo.configure(padx = 10)
        janela_codigo.configure(pady = 10)
        janela_codigo.title(titulo)

        
        texto = ttk.Label(janela_codigo, text=texto, font=(tamanho_texto), background = cor_fundo)
      
        texto.pack(anchor = NW)
        
        entrada = ttk.Entry(janela_codigo, font=(fonte_texto, tamanho_texto))
        entrada.pack(anchor = SW, fill = X, pady = 10)
            
        def get_codigo():
            global codigo
            codigo = entrada.get()
            if codigo != "":
               janela_codigo.destroy()
            
        botao = ttk.Button(janela_codigo, text="Calcular", command = get_codigo)
        botao.pack(anchor = SE) 

        janela_codigo.resizable(False,False)
        janela_codigo.protocol("WM_DELETE_WINDOW", fechar)
        janela_codigo.eval('tk::PlaceWindow . center')
        janela_codigo.iconbitmap('icone.ico')
        janela_codigo.mainloop()
        
        
    def imprimir_resultado(titulo,codigo,modo,texto):
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
        janela.configure(background= cor_fundo)
        janela.configure(height = 1000)
        janela.configure(padx = 10)
        janela.configure(pady = 10)
        janela.title(titulo)
        
        texto_codigo = Label(janela, text = codigo_imprimir, font=(tamanho_texto), justify = LEFT, background = cor_fundo)
        texto_codigo.pack(expand = True, anchor = W)

        texto_turno = Label(janela, text = turno, font=(tamanho_texto), justify = LEFT, background = cor_fundo)
        texto_turno.pack(expand = True, anchor = W)

        #font=(fonte_texto, tamanho_texto)
        texto = Label(janela, text=texto, font=(tamanho_texto), justify = LEFT, background = cor_fundo)
        texto.pack(expand = True, anchor = W)

        def fechar_resultado():
            janela.destroy()
            
        botao = ttk.Button(janela, text="Novo cálculo", command = janela.destroy)
        botao.pack(expand = True,anchor = SE,side = BOTTOM)
        
        janela.resizable(False,False)
        janela.protocol("WM_DELETE_WINDOW", fechar)
        janela.eval('tk::PlaceWindow . center')
        janela.iconbitmap('icone.ico')
        janela.mainloop()

    solicitar_codigo("Calculadora de horários SIGAA","Código de Horário SIGAA:")

    if codigo != "":
        
        modo  = "dia"
        dia   = [False,False,False,False,False,False,False,False]#7
        manha = [False,False,False,False,False,False,False,False]
        tarde = [False,False,False,False,False,False,False,False]
        noite = [False,False,False,False,False,False,False,False]


        for posicao in codigo:
              
           if posicao == "m" or posicao == "M":
              modo = "manha"
           if posicao == "t" or posicao == "T":
              modo = "tarde"
           if posicao == "n" or posicao == "N":
              modo = "noite"
               
           if modo == "dia":
             if posicao == "1":
                dia[1] = True
             if posicao == "2":
                dia[2] = True
             if posicao == "3":
                dia[3] = True
             if posicao == "4":
                dia[4] = True
             if posicao == "5":
                dia[5] = True
             if posicao == "6":
                dia[6] = True
             if posicao == "7":
                dia[7] = True

           if modo == "manha":
             if posicao == "1":
                manha[1] = True
             if posicao == "2":
                manha[2] = True
             if posicao == "3":
                manha[3] = True
             if posicao == "4":
                manha[4] = True
             if posicao == "5":
                manha[5] = True

           if modo == "tarde":
             if posicao == "1":
                tarde[1] = True
             if posicao == "2":
                tarde[2] = True
             if posicao == "3":
                tarde[3] = True
             if posicao == "4":
                tarde[4] = True
             if posicao == "5":
                tarde[5] = True
             if posicao == "6":
                tarde[6] = True
             if posicao == "7":
                tarde[7] = True

           if modo == "noite":
             if posicao == "1":
                noite[1] = True
             if posicao == "2":
                noite[2] = True
             if posicao == "3":
                noite[3] = True
             if posicao == "4":
                noite[4] = True
        #imprimir
        texto = ""

        texto = texto + "Dias da semana:\n"

        if dia[1] == True:
              texto = texto + "Domingo\n"
        if dia[2] == True:
              texto = texto + "Segunda-feira\n"
        if dia[3] == True:
              texto = texto + "Terça-feira\n"
        if dia[4] == True:
              texto = texto + "Quarta-feira\n"
        if dia[5] == True:
              texto = texto + "Quinta-feira\n"
        if dia[6] == True:
              texto = texto + "Sexta-feira\n"
        if dia[7] == True:
              texto = texto + "Sábado\n"

        texto = texto + "\n"        
        texto = texto + "Horário:\n"
        if modo == "manha":
                 
            if manha[1] == True:
              texto = texto + "8am - 8:55am\n"
            if manha[2] == True:
              texto = texto + "8:55am - 9:50am\n"
            if manha[3] == True:
              texto = texto + "10am - 10:50am\n"
            if manha[4] == True:
              texto = texto + "10:55am - 11:50am\n"
            if manha[5] == True:
              texto = texto + "12am - 12:55am\n"
              
        if modo == "tarde":
           if tarde[1] == True:
              texto = texto + "12:55am - 13:50\n"
           if tarde[2] == True:
              texto = texto + "14h - 14:55\n"
           if tarde[3] == True:
              texto = texto + "14:55 - 15:50\n"
           if tarde[4] == True:
              texto = texto + "16h - 16:55\n"
           if tarde[5] == True:
              texto = texto + "16:55 - 17:50\n"
           if tarde[6] == True:
              texto = texto + "18h - 18:50\n"
           if tarde[7] == True:
              texto = texto + "18:55 - 19:50\n"

        if modo == "noite":
           if noite[1] == True:
              texto = texto + "19h - 19:50\n"
           if noite[2] == True:
              texto = texto + "19:50 - 20:40\n"
           if noite[3] == True:
              texto = texto + "20:50 - 21:40\n"
           if noite[4] == True:
              texto = texto + "21:40 - 22:30\n"

        imprimir_resultado("Calculadora de horários SIGAA",codigo,modo,texto)

