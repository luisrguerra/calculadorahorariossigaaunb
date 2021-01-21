from tkinter import *
from tkinter import ttk
import os.path #para checar se o arquivo existe
import solicitar
import imprimir
import fechar

icone = ".\data\icone.ico"
icone_existe = os.path.exists(icone)

while True:
    cor_fundo = 'white'
    fonte_texto = "Arial"
    tamanho_texto = 12
    tamanho_titulo = 16

    codigo = ""

    solicitar.icone = icone
    codigo = solicitar.codigo_get("Calculadora de horários SIGAA","Código de Horário SIGAA:")

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

        imprimir.fundo = "white"
        imprimir.icone = icone
        imprimir.tamanho_texto = tamanho_texto
        #imprimir.fonte = "Noto Sans" #Segoe UI
        #imprimir.fonte_cor = "#212121"
        imprimir.resultado(
           "Calculadora de horários SIGAA",
           codigo,
           modo,
           texto,
           "Nova Consulta"
        )

