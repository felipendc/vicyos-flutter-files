def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_up():
    turn_left()
    move()


def move_four():
    move()
    move()
    move()
    move()


def fazer_um_quadrado():
    move_up()
    turn_right()
    move()
    turn_right()
    move()
    turn_right()
    move()


def jump():
    # move() Pois eu estou usando-o na declaração "if"
    move_up()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


#########################

# for passo in range(6):
#    jump()

at_goal()
# while not at_goal():
while at_goal() == False:
    if front_is_clear():
        move()
    else:
        jump()

    print(at_goal())
    print(front_is_clear())


# Código finalizado com sucesso!
#########################
# Link:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

# Código:
# Só é preciso upá-lo:
#########################
