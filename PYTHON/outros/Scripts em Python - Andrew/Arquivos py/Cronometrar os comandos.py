import time		#Para funções time

start = time.time()		#Começa a contagem do tempo
time.sleep(1.5)		#Aguarda um segundo e meio (para simular os comandos)
tempoDecorrido = time.time() - start	#Recebe o tempo decorrido (tempo atual - o tempo inicial)
print(f"\nO tempo decorrido foi de {tempoDecorrido} segundos")

input("\nAperte ENTER para sair...")