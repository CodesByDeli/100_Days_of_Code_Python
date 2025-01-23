### Definition function
# klicove def nazev():
# do this
# and this .. .


#############source https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Alone&url=worlds%2Ftutorial_en%2Falone.json


def my_function():
    print("Hello")
    print("Bye")

 # staci pouze zavolat funkci
my_function()

######################### Hurdle 1
def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def zakladni_cyklus():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for opakovani in range(7):
    zakladni_cyklus()

#reseni s while

number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1
    print(numner_of_hurdles) # vytiskne zbyly pocet cyklu

############# HURDLE 2

number_of_hurdles = 6
while number_of_hurdles > 0:
    zakladni_cyklus()
    if at_goal() == False:
        number_of_hurdles -= 1
    else:
        number_of_hurdles = 0
        print(number_of_hurdles)

## jednodusi cesta
while not at_goal():
    zakladni_cyklus()

################################### HURDLE 3

def turn_around():
    turn_left()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def zakladni_cyklus():
    #    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while not at_goal():
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        zakladni_cyklus()

        ############# reseni 2

        def turn_right():
            turn_left()
            turn_left()
            turn_left()


        def hop():
            turn_left()
            while wall_on_right():
                move()
            turn_right()
            move()
            turn_right()
            while front_is_clear():
                move()
            turn_left()


        while not at_goal():
            if wall_in_front():
                hop()
            else:
                move()

###################################### HURDLE 4


##### moje reseni
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()


        ####### reseni 2 without infinite loop

        def turn_right():
            turn_left()
            turn_left()
            turn_left()


        while front_is_clear():
            move()
            turn_left()

        while not at_goal():
            if right_is_clear():
                turn_right()
                move()
            elif front_is_clear():
                move()
            else:
                turn_left()
S