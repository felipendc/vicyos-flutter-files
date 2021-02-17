# Port scanner é um programa para verificar quais portas estão abertas em um IP ou site
# Para testar digite o endereço do site, a porta inicial e a porta finally

# Exemplo:
# URL ou IP: google.com
# 75 
# 85

# O resultado será que apenas a porta 80 do site do Google estará aberta

from tkinter import *
from socket import *

fonte = font=("Arial","11")
c = "gray15"
co = "green2"
scanner = Tk()

lb = Label(scanner, text="Port Scanner", font=("Gang of Three", "20"), bg=c, fg=co)
lb.place(x=1, y=1)

lb1 = Label(scanner, text="URL ou IP", font=fonte, bg=c, fg=co)
lb1.place(x=5, y=50)

inf = Entry(scanner, font=fonte, bg="gray10", fg="white")
inf.place(x=80, y=50)

ed12 = Text(scanner, font=("Arial","12", "bold"), bg="gray10", fg="white", width=43, height=18, selectbackground="green2", selectforeground="gray10")
ed12.place(x=5, y=140)

lb2 = Label(scanner, text="Início", font=fonte, bg=c, fg=co)
lb2.place(x=5, y=80)

ini = Entry(scanner, font=fonte, bg="gray10", fg="white")
ini.place(x=80, y=80)

lb3 = Label(scanner, text="Fim", font=fonte, bg=c, fg=co)
lb3.place(x=5, y=110)

fim = Entry(scanner, font=fonte, bg="gray10", fg="white")
fim.place(x=80, y=110)

def scan():
	ed12.delete(0.0)
	a = int(ini.get())
	b = int(fim.get())
	aa = a-1
	url = inf.get()
	lista = range(b, aa, -1)
	for i in lista:
		a = socket(AF_INET, SOCK_STREAM)
		a.settimeout(0.5)
		b = a.connect_ex((url, i))
		if b!= 0:
			ed12.insert(0.0, "A porta {} está fechada\n".format(i))
		else:
			ed12.insert(0.0, "\tA porta {} está ABERTA\n".format(i))
bt = Button(scanner, text="Iniciar", width=15, font=fonte, bg="gray10", fg=co, activebackground=c, activeforeground=co, command=scan)
bt.place(x=243, y=500)

scanner["bg"] = "gray15"
scanner.resizable(height=False, width=False)
scanner.title("Port Scanner")
scanner.geometry("400x540+450+20")
scanner.mainloop()