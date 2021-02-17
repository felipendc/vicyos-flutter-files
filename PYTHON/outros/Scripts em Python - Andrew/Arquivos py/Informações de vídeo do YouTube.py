import pytube

youtube = pytube.YouTube(input("Cole aqui o link do vídeo: "))

# URL para você testar: https://www.youtube.com/watch?v=RRkIQ1Djlbs

print("\nÉ um vídeo restrito:", youtube.age_restricted)  #Se existe restrição de idade
print("Data:", youtube.publish_date)    #Exibe a data de publicação do vídeo
print("Duração: {} minutos e {} segundos".format(youtube.length//60, youtube.length%60))  #Exibe a extensão do vídeo em segundos
print("Palavras chaves:", youtube.keywords) #Exibe as palavras chaves associadas ao vídeo
print("Descrição:", youtube.description) #Exibe a descrição do vídeo (feita pelo autor)
print("Autor:", youtube.author)  #Exibe o autor (nome do canal)
print("Título:", youtube.title)   #Exibe o título do vídeo
print("Visualizações:", youtube.views)  #Exibe o número de views do vídeo

input("\nAperte ENTER para sair...")