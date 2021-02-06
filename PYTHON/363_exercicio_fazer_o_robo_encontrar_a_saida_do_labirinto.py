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
            move()
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


# 63. Final Project: Scaping the Maze
# In my case, It took three freaking hours for me to finally find the code solution for the "Maze World".
# But, the code that I wrote works all good in all of the Meze World layouts.Including "problem_world1", "problem_world2" and "problem_world3":
# Here is my code:
