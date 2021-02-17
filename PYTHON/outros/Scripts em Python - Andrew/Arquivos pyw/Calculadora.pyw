"""
	Programa Calculador com Tkinter
	Código comentado por Rodrigo Nery

"""


# importo o RE do módulo Regex
import re
# importo o Tkinter a lib das dialogs :)
import tkinter as tk
# importo o Math a lib dos cálculos :)
from math import sqrt
 
# Crio a classe Aplication e passo o frame do TK
 
# O widget Frame é muito importante para o processo de agrupamento e organização de outros widgets de uma forma amigável. Ele funciona como um contêiner, que é responsável por organizar a posição de outros widgets.
# Ele usa áreas retangulares na tela para organizar o layout e fornecer preenchimento desses widgets. Um frame também pode ser usado como uma classe básica para implementar widgets complexos. 
class Application(tk.Frame):
    # master - representa a janela principal.
    # o _init_ É chamado de construtor na terminologia orientada a objetos. Este método é chamado quando um objeto é criado a partir de uma classe e permite que a classe inicialize os atributos da classe 
    def __init__(self, master=None):
        # O super serve para - em uma relação de herança entre uma classe Base e outra Derivada - permitir que a classe Derivada se refira explicitamente à classe Base.
        super().__init__(master=master)
        self.master = master
 
        # Este gerenciador de geometria organiza widgets em blocos antes de colocá-los no widget pai.
 
        #Sintaxe
        #widget.pack (pack_options)
        #Aqui está a lista de opções possíveis -
 
        #expand - Quando definido como verdadeiro, o widget se expande para preencher qualquer espaço não usado de outra forma no pai do widget.
 
        #fill - Determina se o widget preenche qualquer espaço extra alocado a ele pelo empacotador ou mantém suas próprias dimensões mínimas: NENHUMA (padrão), X (preencher apenas horizontalmente), Y (preencher apenas verticalmente) ou AMBOS (preencher horizontal e verticalmente )
 
        #side - Determina qual lado do widget pai é compactado: TOPO (padrão), INFERIOR, ESQUERDO ou DIREITO. 
        self.pack()
        # o self coloca etiquetas nos objetos, atribui coisas/valores ou objetos. 
        self.input = '0' # digo que o input da classe terá o valor 0
        self.draw_frame() # invoco o método draw_frame() da classe
    
    # Classe de criação do butão passando os parâmetros texto, cor, command, r = row = linha e column = coluna 
    # Em suma: coloco atributos no botão da classe principal.
    def create_button(self, text, color, command, r, c, cspan=1, w=8):
        # botão da classe principal chama o módulo tk, crio um botão e digo que ele terá uma variável cor e fg - foreground = branco
        # Em suma o botão terá fundo a ser determinado e letra branca.
        self.button = tk.Button(self, bg=color, fg='white')
        # Passo o texto que será exibido no botão
        self.button['text'] = text
        # Passo o command que é geralmente a ação do botão da classe
        self.button['command'] = command
        # Coloco a altura e largura
        self.button.config(height=2, width=w)
        # o grid trabalha com coluna e linha do botão
        self.button.grid(row=r, column=c, columnspan=cspan, pady=4)
 
        # retorna o botão da classe
        return self.button
    
    # desenha o frame e passa o objeto da classe
    def draw_frame(self):
        # crio o label com o tk.label() um dos métodos do módulo TK
        # atribuo fonte, cor, etc.
        self.label = tk.Label(self, font=("Helvetica", 16), bg='gray30', fg='white', anchor='se')
        # texto a ser exibido na label
        self.label['text'] = '0'
        # configuração de altura e largura
        self.label.configure(width=23, height=5)
        # trabalho com o grid
        self.label.grid(row=0, column=0, columnspan=4, pady=10)
 
        # botão CE da calculadora
        self.ce = self.create_button('CE', 'red2', self.clear, 1, 0)
        # botão BackSpace
        self.back = self.create_button(u'\u232b', 'gray20', self.back, 1, 1)
        # botão mod
        self.mod = self.create_button('%', 'gray20', lambda : self.get('%'), 1, 2)
        # divisão
        self.div = self.create_button('/', 'gray20', lambda : self.get('/'), 1, 3)
        # botão 7
        self.seven = self.create_button('7', 'gray20', lambda : self.get('7'), 2, 0)
        # botão 8 .. segue...
        self.eight = self.create_button('8', 'gray20', lambda : self.get('8'), 2, 1)
        self.nine = self.create_button('9', 'gray20', lambda : self.get('9'), 2, 2)
        self.mul = self.create_button('X', 'gray20', lambda : self.get('*'), 2, 3)
 
        self.four = self.create_button('4', 'gray20', lambda : self.get('4'), 3, 0)
        self.five = self.create_button('5', 'gray20', lambda : self.get('5'), 3, 1)
        self.six = self.create_button('6', 'gray20', lambda : self.get('6'), 3, 2)
        self.minus = self.create_button('-', 'gray20', lambda : self.get('-'), 3, 3)
 
        self.one = self.create_button('1', 'gray20', lambda : self.get('1'), 4, 0)
        self.two = self.create_button('2', 'gray20', lambda : self.get('2'), 4, 1)
        self.three = self.create_button('3', 'gray20', lambda : self.get('3'), 4, 2)
        self.plus = self.create_button('+', 'gray20', lambda : self.get('+'), 4, 3)
 
        self.root = self.create_button('v', 'gray20', lambda : self.get('v'), 5, 0)
        self.zero = self.create_button('0', 'gray20', lambda : self.get('0'), 5, 1)
        self.dot = self.create_button('.', 'gray20', lambda : self.get('.'), 5, 2)
        self.equal = self.create_button('=', 'gray20', self.output, 5, 3)
 
    # passo valores e o objeto da classe pra continuar trabalhando dentro da classe pai
    def get(self, value):
        self.input += str(value)
        # + - divisão, etc.
        self.ops = ['+','-','*','/','%', 'v']
        
        # o input trabalha com as entradas, os campos da calculadora
        if self.input[-1] in self.ops and self.input[-2] in self.ops:
            self.input = str(self.input[:-2] + self.input[-1])
        if self.input[0] == '0':
            self.input = self.input[1:]
        if self.input[0] in self.ops:
            self.input = self.input[1:]
            self.input = '0' + self.input
        # digo que um dos labels que exibem texto receberão o que for do input
        self.label['text'] = self.input
    
    # apagar
    def clear(self):
        self.input = '0'
        self.label['text'] = self.input
    # backspace
    def back(self):
        self.text = self.input
        if len(self.input) == 1:
            self.clear()
        else:
            self.input = self.text[:-1]
            self.label['text'] = self.input
    
    # saída
    def output(self):
        # regex pra validar a saída dos inputs
        root_ = re.compile(r'v\d+')
        # valida tudo
        all_roots = re.findall(root_, self.input)
        if all_roots:
            for num in all_roots:
                # calcula com o math
                calc = sqrt(int(num.lstrip('v')))
                self.input = re.sub(num, '*'+str(round(calc,3)), self.input)
 
                if self.input[0] == '*' :
                    self.input = self.input[1:]
 
        self.out = str(round(eval(self.input), 5))
        self.label['text'] = self.out
        self.input = self.out
 
# Janela principal do TK vai receber o módulo tk e a classe que foi criada ai em cima
root = tk.Tk()
# a janela principal possui alguns métodos agora como o geometry
root.geometry('300x400+433+234')
# Possui a capacidade de atribuir um título às janelas
root.wm_title('Calculadora')
# Pode também definir que o usuário não poderá redimensinonar a janela da dialog
root.resizable(False, False)
 
# altero o nome da classe e digo que o root é a janela principal
app = Application(master=root)
# app agora tem todas as propriedades e métodos do root anterior incluindo o método .mainloop
app.mainloop() # invoco o loop das dialogs e finalizo o processo inteiro de construição