def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_right()
    move()
    turn_right()


#############################
while not at_goal():
    if front_is_clear():
        move()
        if not is_facing_north() and front_is_clear() and right_is_clear():
            turn_right()
    else:
        if is_facing_north() and wall_in_front() and right_is_clear():
            turn_right()
        elif wall_in_front() and right_is_clear():
            turn_right()
        elif wall_in_front():
            turn_left()

#########################
# Link:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# Hurdle: MAZE

# Código:
# Só é preciso upá-lo:
#########################
