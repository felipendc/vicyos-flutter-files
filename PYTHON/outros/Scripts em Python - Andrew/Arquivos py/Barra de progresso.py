# O script abaixo serve para mostrar um tipo de barra de progresso para sabermos o quanto
#	de um determinado comando já foi executado

from time import sleep
from tqdm import tqdm
for i in tqdm(range(25)):	#Executar 25 vezes a açõa do laço
    sleep(0.5)		#Esperar 0.5 segundos (meio segundo)

input("Aperte ENTER para sair...")

#Ou melhor ainda:

"""
from tqdm import tqdm

for i in tqdm(range(100000000), desc="Executando os comandos"):
    continue
"""

# O range pode ser substituído por qualquer objeto iterável.
# O continue deve ser substituído por um ou mais comandos.
# A barra criada com tqdm é boa para blocos de comandos demorados, por isso o range de 10 milhões.
# No programa original que estou criando o range é substituído por uma wordlist, um arquivo *.txt
#   que será lido linha por linha, e a cada leitura tentará quebrar a senha de um arquivo *.pdf
# O nome dessa técnica de quebra de senha é "Ataque de dicionário"