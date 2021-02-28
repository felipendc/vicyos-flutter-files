from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

root = Tk()
root.geometry("550x180+450+250")
root.resizable(False, False)
root.title("AES128")
root.configure(bg="#561623")
root.iconbitmap("Cadeado.ico")

img = ImageTk.PhotoImage(Image.open("Cadeado.ico"))

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()

def escolherArquivo():
    caminho = filedialog.askopenfilename ()
    var1.set(caminho)

def ondeSalvar():
    caminho = filedialog.askdirectory()
    var2.set(caminho)

def encriptarArquivo():
    arquivoOriginal = var1.get()
    extensao = str(var1.get()).split(".")
    arquivoEncriptado = str(var2.get()) + '\\Encriptado.{}'.format(extensao[len(extensao)-1])

    senhaBytes = var3.get().encode()

    salt = b"\xf1\t\x84\xc2\xa7y'\xf0\xb2\x8d\xec\x91]'\xc3\xea"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(senhaBytes))

    arq1 = open(arquivoOriginal, "rb")
    conteudoOriginal = arq1.read()

    fernet = Fernet(key)
    conteudoEncriptado = fernet.encrypt(conteudoOriginal)

    arq2 = open(arquivoEncriptado, "wb+")
    arq2.write(conteudoEncriptado)

    arq1.close()
    arq2.close()

def decriptarArquivo():
    arquivoEncriptado = var1.get()
    extensao = str(var1.get()).split(".")
    arquivoDecriptado = str(var2.get()) + '\\Decriptado.{}'.format(extensao[len(extensao)-1])

    senhaBytes = var3.get().encode()

    salt = b"\xf1\t\x84\xc2\xa7y'\xf0\xb2\x8d\xec\x91]'\xc3\xea"
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(senhaBytes))

    arq1 = open(arquivoEncriptado, "rb")
    conteudoEncriptado = arq1.read()

    fernet = Fernet(key)
    conteudoDecriptado = fernet.decrypt(conteudoEncriptado)

    arq2 = open(arquivoDecriptado, "wb")
    arq2.write(conteudoDecriptado)

    arq1.close()
    arq2.close()

lb1 = Label(root, image=img, bg="#561623").pack(anchor=NW)
lb2 = Label(root, text="  Digite a senha  ").place(x=130, y=95)
et1 = Entry(root, width=50, textvariable=var1).place(x=230, y=15)
et2 = Entry(root, width=50, textvariable=var2).place(x=230, y=55)
et3 = Entry(root, width=50, textvariable=var3).place(x=230, y=95)
bt1 = Button(root, text="Escolher arquivo", width=12, command=escolherArquivo).place(x=130, y=15)
bt2 = Button(root, text="Onde salvar", width=12, command=ondeSalvar).place(x=130, y=55)
bt3 = Button(root, text="Encriptar", command=encriptarArquivo).place(x=280, y=130)
bt4 = Button(root, text="Decriptar", command=decriptarArquivo).place(x=360, y=130)

root.mainloop()