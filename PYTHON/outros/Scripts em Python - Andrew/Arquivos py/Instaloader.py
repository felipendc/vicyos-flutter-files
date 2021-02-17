#Instale com o CMD digitando pip install instaloader
import instaloader

insta = instaloader.Instaloader()   #Instancia o objeto para trabalhar com Instagram
usuario = "felipendc2012"    #Substitua pelo nome de usuário no Instagram que você deseja
insta.download_profile(usuario, profile_pic_only=False)     #Baixa todos os arquivos do perfil

# IMPORTANTE: Só funciona em perfis públicos