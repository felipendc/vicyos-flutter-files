#Write your code below this line 👇
# video 11

username = input("What's your name? ")

username_length = len(username) - username.count(' ')

print(username_length)


# Outro modo de imprimir o input na tela:
# print( len( input("What's your name? ") ) )

# username.count(' ') = Serve para contar os espaços entre as palavras!
# len(objeto) = Serve para contar os caracteres da str.
# input(obj) = Serve para pegar e armazenar oque o usuário digitou!
