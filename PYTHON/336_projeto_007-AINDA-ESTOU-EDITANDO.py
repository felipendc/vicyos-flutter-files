print('''
     0000             0000        7777777777777777/========___________
   00000000         00000000      7777^^^^^^^7777/ || ||   ___________
  000    000       000    000     777       7777/=========//
 000      000     000      000             7777// ((     //
0000      0000   0000      0000           7777//   \\   //
0000      0000   0000      0000          7777//========//
0000      0000   0000      0000         7777
0000      0000   0000      0000        7777
 000      000     000      000        7777
  000    000       000    000       77777
   00000000         00000000       7777777
     0000             0000        777777777
''')

print("Bem-vindo de volta, soldado 007.")
print("A sua missão é encontrar a sua parceira que foi capturada.")

saltar = input("Digite a letra 'S' para saltar do avião: ")

if saltar == "S" or saltar == "s":
    print("")
    print("Agora são 2 horas da manhã...")
    print("")
    print("Você acabou de saltar do avião e caiu em um matagal,\nlogo a frente, você se deparou com dois caminhos com direções diferentes.")
    print("")
    print("Um está a sua direita e o outro a sua esquerda.")
    print("")
    escolher_lado = input(
        "Pra qual lado você deseja ir? D = Diteira, E = Esquerda: ")
    print("")
    if escolher_lado == "D" or escolher_lado == "d":
        print("\n Fim de jogo!\n Missão fracassada!\n Você caiu em uma armadilha e foi capturado pelos inimigos!\n\n\n")

    elif escolher_lado == "E" or escolher_lado == "e":
        print("Em breve!")
        # Código ainda em desenvolvimento!
