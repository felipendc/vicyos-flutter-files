###################################
########### Vareáveis:  ###########
at_goal()
soma_a_altura_da_parede = 0
###################################


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_up():
    turn_left()


def jump():
    turn_right()
    move()
    turn_right()
#    move()


def going_down():
    while soma_a_altura_da_parede == 0:
        jump()
        soma_a_altura_da_parede -= 1


def start_position():
    turn_left()

##################################
# Lógica do código:
##################################


while at_goal() == False:
    if wall_in_front():
        turn_up()
        while wall_on_right():
            move()
            soma_a_altura_da_parede += 1
            print(soma_a_altura_da_parede)

        jump()
        while not soma_a_altura_da_parede == 0:
            print(soma_a_altura_da_parede)
            move()
            soma_a_altura_da_parede -= 1
            print(soma_a_altura_da_parede)

        start_position()

    else:
        if front_is_clear():
            move()

    print(at_goal())
    print(front_is_clear())
    print(wall_on_right)


#########################
# Link:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# Hurdle: 4 Nível difícil.

# Código:
# Só é preciso upá-lo:
#########################
