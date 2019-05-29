import random
import time

def dungeon_builder():
    global rows
    global cols
    global name
    print('Welcome to the dungeon!')
    time.sleep(1)
    while True:
        print('Have you played this game before? Enter Yes/No')
        entry = str(input('> ')).title()
        if entry == 'Yes' or entry == 'Y':
            print('Aha, let\'s jump straight to it then.')
            break
        elif entry == 'No' or entry == 'N':
            print('The aim of the game is to move your character \o@ onto the secret door.')
            time.sleep(2)
            print('Although armed with your trusty sword \ and shield @ , they\'ll be no match against the monster which is hiding in one of the rooms.')
            time.sleep(2)
            print('If you are 1 room away from the monster, you\'ll be able to hear it, so take care! \nIf you are 1 room away from the door, you\'ll be able to make out a faint glow.')
            time.sleep(2)
            print('The coordinate system comes from the top-left (0,0) right and down.')
            time.sleep(2)
            break
        else:
            print('Please enter only Yes or No.')
            time.sleep(0.7)
            continue
            
    while True:
        while True:
            print('Firstly, what is your name?')
            name = input ('> ')
            if len(name) > 1 and len(name) < 20:
                name = name
                break
            else:
                print('Sorry, your name must be between 1 and 20 characters, try again.')
                time.sleep(0.7)
                continue
            
        while True:
            print('How many rows would you like on your map, {}?'.format(name))
            try:
                rows = int(input('> '))
            except TypeError:
                print('That\'s not an integer!')
                time.sleep(0.7)
                continue
            if rows > 1 and rows < 10:
                rows = int(rows)
                break
            else:
                print('Sorry, input must be an integer between 1 and 9, try again.')
                time.sleep(0.7)
                continue

        while True:
            print('And how many columns?')
            try:
                cols = int(input('> '))
            except TypeError:
                print('That\'s not an integer!')
                time.sleep(0.7)
                continue
            if cols > 1 and cols < 10:
                cols = int(cols)
                break
            else:
                print('Sorry, input must be an integer between 1 9, please try again.')
                time.sleep(0.7)
                continue
        print('One moment please!')
        time.sleep(0.5)
        break
    return [(x, y) for x in range(rows) for y in range(cols)]

def grid_drawer():
    character_sprite = "|\o@"
####  One or the other of these - depends on the format you want (blank rooms vs clear coordinates).
##    dungeon = [['|_' for x in range(rows)] for y in range(cols)]
    dungeon = [['|{},{}'.format(x,y) for x in range(rows)] for y in range(cols)]
    x, y = player
    dungeon[y][x] = character_sprite
####  Use the second print line if you've got the numbered cells
##    print(' _' * (rows))
    print(' ___' * (rows))
    for row in dungeon:
        print(''.join(row), end = '|\n')
    print(' ̅̅̅' * (rows))

def get_locations():
    return random.sample(dungeon_builder(), 3)

def move_player(player, move):
    x, y = player
    if move == 'Left':
        player = (x -1, y)
    elif move == 'Right':
        player = (x +1, y)
    elif move == 'Up':
        player = (x, y -1)
    else:
        player = (x, y +1)
    return player

def player_location():
    print('You\'re currently in room {}.'.format(player))

def monster_location():
    x_player, y_player = player
    x_monster, y_monster = monster
    if abs(x_monster - x_player) <= 1 and abs(y_monster - y_player) <= 1:
        print('You can hear the monster close by!')
        
def door_location():
    x_player, y_player = player
    x_door, y_door = door
    if abs(x_door - x_player) <= 1 and abs(y_door - y_player) <= 1:
        print('You can make out a faint ethereal glow!')
        
def get_moves(player):
    global moves
    moves = ['Left', 'Right', 'Up', 'Down']
    moves_permitted = moves[:]
    x, y = player
    if x == 0:
        moves_permitted.remove('Left')
    if x == rows-1:
        moves_permitted.remove('Right')
    if y == 0:
        moves_permitted.remove('Up')
    if y == cols-1:
        moves_permitted.remove('Down')
    return moves_permitted

def clear_screen():
    print ("\n" * 100)

def game_restart():
    while True:
        time.sleep(1)
        print('Would you like to play again? Enter Yes/No.')
        answer = input('> ')
        answer = answer.title()
        if answer == 'Yes' or answer == 'Y':
            clear_screen()
            get_locations()
            break
        if answer == 'No' or answer == 'N':
            print('Goodbye {}!'.format(name))
            raise SystemExit(0)
        else:
            print('I didn\'t understand that.')
            continue
    
def game_loop():
    global monster
    global door
    global player
    
    monster, door, player = get_locations()
    
    while True:
        clear_screen()
        grid_drawer()
        player_location()
    ##    print('The secret door is in room {}'.format(door))
    ##    print('The monster is in room {}'.format(monster))
        monster_location()
        door_location()
        print('\nYou can move {}.'.format(', '.join(get_moves(player))))
        print('Or enter Quit to quit.')

        move = input('> ')
        move = move.title()

        if move == 'Quit':
            print('Goodbye {}!'.format(name))
            break
        elif move not in moves:
            print('{} is not a valid direction!\n'.format(move))
            time.sleep(1)
            continue
        elif move not in get_moves(player):
            print('\nWalls are hard! Don\'t run into them!\n')
            time.sleep(1)
            continue
        else:
            player = move_player(player, move)
        if player == door:
            print('{} has found the secret door!'.format(name))
            game_restart()
        if player == monster:
            print('{} has been eaten by the monster!'.format(name))
            game_restart()
        else:
            continue

game_loop()
####    Monster moves too?
####    You can hear the monster/door faintly if <2 cell away
####    You can't hear {object} if {object} >2 cells away?
