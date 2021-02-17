import pytube   #Módulo para trabalhar com o Youtube

#Recebe o endereço do vídeo
url = input("Cole aqui o endereço do vídeo: ")

#Cria um objeto do tipo <class 'pytube.__main__.YouTube'>
youtube = pytube.YouTube(url)

#Imprime o título do vídeo
print(youtube.title)

#Cria um objeto para o vídeo e outro para o áudio
video = youtube.streams.get_highest_resolution()
audio = youtube.streams.get_audio_only()

#Baixa o vídeo e o áudio, se não houver passagem de parâmetros
# ele baixa os arquivos no local do projeto Python e mantém o nome do título
video.download("", "video")		#O primeiro argumento é o diretório, o segundo é o nome
audio.download("", "audio")
