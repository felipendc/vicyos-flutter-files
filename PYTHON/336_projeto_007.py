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

print("Bem-vindo de volta, agente 007.")
print("A sua missão é encontrar a sua parceira que foi capturada.")

saltar = input("Digite a letra 'S' para saltar do avião: ")

if saltar == "S" or saltar == "s":
    print("")
    print("Agora, são 2 horas da manhã...")
    print("")
    print("Você acabou de saltar do avião e caiu em um matagal,\nlogo a frente, você se deparou com dois caminhos com direções diferentes.")
    print("")
    print("Um está á sua direita e o outro á sua esquerda.")
    print("")
    escolher_lado = input(
        "Pra qual lado você deseja ir? E = Esquerda ou D = Diteira: ")
    print("")
    if escolher_lado == "D" or escolher_lado == "d":
        print("\n Fim de jogo!\n Missão fracassada!\n Você caiu em uma armadilha e foi capturado pelos inimigos!\n\n\n")

    elif escolher_lado == "E" or escolher_lado == "e":
        print("Após uma longa caminhada no escuro, você se chegou até um lago...")
        print("E pra seguir em frente, você terá que nadar para você continuar o seu percurso...\n")
        nadar_ou_esperar = input(
            "Você gostaria de nadar ou esperar e descansar um pouco? Digite 'E' para esperar e descansar ou 'N' para nadar e seguir em frente.")
        if nadar_ou_esperar == "N" or nadar_ou_esperar == "n":
            print("\n Fim de jogo!\n Missão fracassada!\n Você caiu em uma armadilha que estava dentro do lago e foi capturado pelos inimigos!\n\n\n")

        elif nadar_ou_esperar == "E" or nadar_ou_esperar == "e":
            print(
                "\nAo parar, para descansar, você deitou-se na grama e começou olhar para as árvores,")
            print(
                "e você acabou notando uma casa de árvore que continha 3 portas.")
            print(
                "Você escalou a árvore e você decidiu ver o que tinha atrás das portas...")
            print(
                "Você se aproximou das portas e notou que tinha uma porta vermelha, uma azul e uma amarela")
            print("Então, você pensou... qual delas abrir primeiro.")
            print("")
            qual_porta_abrir = input(
                "Qual das portas você deseja abrir primeiro? Digite: 'V' para abrir a porta vermelha, 'A' para abrir a "
                "porta azul ou M para abrir a porta amarela: ")

            if qual_porta_abrir == "V" or qual_porta_abrir == "v":
                print(
                    "\n Fim de jogo!\n Missão fracassada!\n Ao abrir a porta vermelha, você foi incinerado pelo inimigo!")

            elif qual_porta_abrir == "A" or qual_porta_abrir == "a":
                print("")
                print(
                    "\n Fim de jogo!\n Missão fracassada!\n Ao abrir a porta azul, você foi comido por uma besta!")

            elif qual_porta_abrir == "M" or qual_porta_abrir == "m":
                print("")
                print(
                    "\n Parabéns! Missão concluída!\n Você encontrou a sua parceira e conseguiu resgatá-la!!!")
                print("")
                print("")

            else:
                print("")
                print("Fim de jogo!")
