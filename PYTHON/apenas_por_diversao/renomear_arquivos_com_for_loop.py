from os import path, listdir

dir_atual = str(path.dirname(path.abspath(__file__)) + "\\")
listar_arquivos = listdir(dir_atual)

for arquivo in listar_arquivos:
    # Se o nome do arquivo que está dentro do
    # diretório desse script tem ".mp3" renomeie para .mp4
    # Caso contrário descarte-o
    if '.mp3' in arquivo:
        renomear = arquivo.split('.mp3', 1)[0] + f".mp4"
        print(renomear)
