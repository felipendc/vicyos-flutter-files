# Tracert é um comando do CMD (Prompt de comandos do Windows) que serve
#	para traçar a rota do seu computador até o IP ou site desejado

# Para ver como funciona, digite um IP ou URL de site e aperte o botão "Traçar rota"
# IMPORTANTE: Isso pode demorar um minuto ou mais porque o tracert traça a rota em até 30 níveis

from tkinter import *
import os, re, subprocess
from tkinter import messagebox

app = Tk()
app.title("Sasp - AutoTracert")
app.resizable(False, False)
app.geometry("545x290+600+300")
app.config(bg=None)     #Altere o None para a cor desejada

comando = StringVar()

def tracert():
    global comando
    cmd = "tracert " + str(comando.get())
    resultado = "".join(os.popen(cmd).readlines())
    tx1.insert(END, resultado)

#Respectivamente uma Label, um Entry, um Button e um Text
#A Label é apenas para informar o usuário que informação deve inserir no Entry
#O Entry serve para receber o IP ou RUL digitado (ou colado) pelo usuário
#O Button (botão) deverá invocar a função tracert passando o valor de Entry e
#   o resultado deverá ser exibido no tipo Text
#E por fim o Text para receber o retorno da função ligada ao Button

#PS: Optei pelo tipo tkinter.Text por que é esteticamente melhor que o
#   messagebox para o propósito que você deseja
lb1 = Label(app, text="IP ou URL").place(x=5, y=5)
et1 = Entry(app, width=60, textvariable=comando).place(x=65, y=5)
bt1 = Button(app, text="Traçar rota", width=10, bd=3, command=tracert).place(x=435, y=2)
tx1 = Text(app, bd=2, width=66, height=15)
tx1.place(x=5, y=35)

app.mainloop()