# Funções com saídas
def formatar_nome(p_nome, u_nome):
    if p_nome == "" or u_nome == "":
        return "Você não adicionou valores válidos."
    p_nome_formatado = p_nome.title()
    u_nome_formatado = u_nome.title()
    f"Result: {p_nome_formatado} {u_nome_formatado}"


# Salvando a saída em uma vareável
nome_formatado = formatar_nome(
    input("O seu primeiro: "), input("O seu último nome?: "))
print(nome_formatado)
# ou salvanddo a saída diretamente
print(formatar_nome(input("Qual é o seu primeiro nome? "),
                    input("Qual é o seu último nome? ")))

# Funções com saída já usadas
tamanho = len(nome_formatado)

# Retorna como um valor de saída


def formatar_nome(p_nome, u_nome):
    """Pegar o primeiro e o último nome e o formata
    para retornar cada palavra com letras maiúsculas."""
    if p_nome == "" or u_nome == "":
        return "Você não adicionou valores válidos."
    p_nome_formatado = p_nome.title()
    u_nome_formatado = u_nome.title()
    return f"Result: {p_nome_formatado} {u_nome_formatado}"
