from turtle import *
from random import choice
from playsound import playsound
from freegames import floor, vector

def intro_play_sound():
    playsound('pacman_beginning.wav')


def making_square(x, y):
    "Draw square using path at (x, y)."
    pth_turtle.up()
    pth_turtle.goto(x, y)
    pth_turtle.down()
    pth_turtle.begin_fill()

    for count in range(4):
        pth_turtle.forward(20)
        pth_turtle.left(90)

    pth_turtle.end_fill()

def finding_offset(game_point):
    "Return offset of point in tiles."
    x_point = (floor(game_point.x, 20) + 200) / 20
    y_point = (180 - floor(game_point.y, 20)) / 20
    game_index = int(x_point + y_point * 20)
    return game_index

def check_valid(game_point):
    "Return True if point is valid in tiles."
    game_index = finding_offset(game_point)
    if game_tiles[game_index] == 0:
        return False
    game_index = finding_offset(game_point + 19)
    if game_tiles[game_index] == 0:
        return False
    return game_point.x % 20 == 0 or game_point.y % 20 == 0

def game_world():
    "Draw world using path."
    bgcolor('black')
    pth_turtle.color('blue')

    for game_index in range(len(game_tiles)):
        game_tile = game_tiles[game_index]
        if game_tile > 0:
            x = (game_index % 20) * 20 - 200
            y = 180 - (game_index // 20) * 20
            making_square(x, y)
            if game_tile == 1:
                pth_turtle.up()
                pth_turtle.goto(x + 10, y + 10)
                pth_turtle.dot(2, 'white')

def elements_movement():
    "Move pacman and all ghosts."
    writer_turtle.undo()
    writer_turtle.write(all_states['score'])

    clear()

    if check_valid(pacman_character + aim_machine):
        pacman_character.move(aim_machine)

    game_index = finding_offset(pacman_character)

    if game_tiles[game_index] == 1:
        game_tiles[game_index] = 2
        all_states['score'] += 1
        x = (game_index % 20) * 20 - 200
        y = 180 - (game_index // 20) * 20
        making_square(x, y)

    up()
    goto(pacman_character.x + 10, pacman_character.y + 10)
    dot(20, 'yellow')

    for pnt, crse in ghosts_riders:
        if check_valid(pnt + crse):
            pnt.move(crse)
        else:
            options = [
                vector(-5, 0),
                vector(0, -5),
                vector(5, 0),
                vector(0, 5),
            ]
            pln = choice(options)
            crse.x = pln.x
            crse.y = pln.y

        up()
        goto(pnt.x + 10, pnt.y + 10)
        dot(20, 'red')

    update()

    for pnt, crse in ghosts_riders:
        if abs(pacman_character - pnt) < 20:
            return

    ontimer(elements_movement, 100)

def do_change(x, y):
    "Change pacman aim if valid."
    if check_valid(pacman_character+ vector(x, y)):
        aim_machine.x = x
        aim_machine.y = y


if __name__ == '__main__':

    # Starting State of score which is equal to 0
    all_states = {'score': 0}
    # Making path not Visibility
    pth_turtle = Turtle(visible=False)
    # Making turtle Writer not visible 
    writer_turtle = Turtle(visible=False)
    # Describe the Aim
    aim_machine = vector(5, 0)
    # Making Pacman Character
    pacman_character = vector(-40, -80)
    # Making 4 Ghosts
    ghosts_riders = [
        [vector(-180, -160), vector(0, 5)],
        [vector(100, -160), vector(-5, 0)],
        [vector(-180, 160), vector(5, 0)], 
        [vector(100, 160), vector(0, -5)],
    ]   

    # These are the tiles which will make the game
    game_tiles = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]

    # Setting the frame Size
    setup(420, 420, 370, 0)

    # Hiding Turtle
    hideturtle()
    # Making Turtle Tracer = False
    tracer(False)

    # Telling turtle to go to this position
    writer_turtle.goto(160, 160)

    # Setting up the turtle color = White
    writer_turtle.color('white')

    # This will update all the score on the window
    writer_turtle.write(all_states['score'])

    #play intro sound
    intro_play_sound()

    # This will listen all the key
    listen()

    # All keys funtions 
    onkey(lambda: do_change(-5, 0), 'Left')
    onkey(lambda: do_change(0, -5), 'Down')
    onkey(lambda: do_change(5, 0), 'Right')
    onkey(lambda: do_change(0, 5), 'Up')

    # Making Game World
    game_world()

    # Move Elements
    elements_movement()

    # Finish the Game 
    done()
