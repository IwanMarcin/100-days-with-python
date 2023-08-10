#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
#My solution

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    else:    
        while wall_in_front() and not at_goal():
            turn_left()
            while wall_on_right() and not at_goal():
                if front_is_clear():
                    move()
                    if right_is_clear():
                        turn_right()
                        move()
                        turn_right()
                else:
                    turn_left()