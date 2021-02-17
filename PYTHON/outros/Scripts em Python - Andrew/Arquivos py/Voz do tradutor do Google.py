#Instale com o CMD digitando pip install gtts
from gtts import gTTS   #Importa o módulo Google Text-to-Speech (Síntese de voz Google)
import os   #Apenas para executar o áudio após ele ser salvo

#Abre um arquivo de texto no modo leitura e lê o conteúdo
arquivoTexto = open('arquivo.txt')
conteudoArquivo = arquivoTexto.read()

#Escolhe o idioma, pt-br é o português brasileiro, para inglês escreva idioma = "en"
idioma = "pt-br"

#Pega a voz do tradutor do Google no idioma selecionado com o conteúdo passado,
#   é necessário estar conectado a internet para funcionar
audio = gTTS(text=conteudoArquivo, lang=idioma, slow=False)

#Salva e executa o áudio
audio.save("áudio.mp3")
os.system("áudio.mp3")

arquivoTexto.close()    #Fecha o arquivo