# FUNÇÃO COM ARGUMENTO POSICIONAL:

# O argumento é o que passa pelo parâmetro.
# Essa é uma função com argumentos posicionais.
def cumprimentar_com_nome(nome, nome2):
    print('')
    print(f'Eai, {nome}, você viu o {nome2}?')
    print(f'Eai, {nome}, beleza? Como está o {nome2}?')
    print(
        f'Você pode falar pro {nome2} que eu estou chamando ele? Muito obrigado.')
    print('')


# Pois, eu tenho que posicionar os nomes nas ordens posicionais.
cumprimentar_com_nome('Felipe', 'Emerson')

# Se eu inverter os argumentos, no print, eles terão outro resultados.
cumprimentar_com_nome('Emerson', 'Felipe')  # Argumentos invertidos!


#
# FUNÇÃO COM # FUNÇÃO COM ARGUMENTO NOMEADO:

def cumprimentar_com_nome(nome, nome2):
    print('')
    print(f'Eai, {nome}, você viu o {nome2}?')
    print(f'Eai, {nome}, beleza? Como está o {nome2}?')
    print(
        f'Você pode falar pro {nome2} que eu estou chamando ele? Muito obrigado.')
    print('')


# Agora mesmo que eu inverta as posições dos argumentos o resultado sempre será o mesmo.
# Pois, eu já atribuí o valor de cada parâmetro.
cumprimentar_com_nome(nome='Felipe', nome2='Emerson')
# Argumentos invertidos, com o mesmo resultado!
cumprimentar_com_nome(nome2='Emerson', nome='Felipe')
