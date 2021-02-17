#Importa as funções do módulo necessário
from pytube import Playlist, YouTube

#Pega o endereço da playlist
playlist_url = input("Cole aqui o endereço da playlist: ")

#Cria um objeto do tipo <class 'pytube.contrib.playlist.Playlist'>
playlist = Playlist(playlist_url)

#Percorre os endereços da lista e baixa todos os vídeos
for url in playlist:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download()

#Endereço teste:
# https://www.youtube.com/watch?v=OZSZHmWSOeM&list=PLshJcDKb9hL-GATrGJuAjOW8o7xDWrbUe

#Salva os vídeos da playlist no diretório do projeto Python