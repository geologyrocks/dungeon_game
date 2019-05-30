import random
import time

win_loss_counter = [0,0] 

def clear_screen():
    print ('\n' * 100)

def dungeon_builder():
    clear_screen()
    global rows
    global cols
    global name
    global game_difficulty
    permitted_game_difficulties = ['Easy', 'Medium', 'Hard']
    print('Welcome to the dungeon!')
    time.sleep(1)
    while True:
        print('Would you like to know how to play the game? Enter Y/N.')
        entry = str(input('> ')).title()
        if entry == 'No' or entry == 'N':
            print('Let\'s jump straight to it then.\n')
            time.sleep(0.7)
            break
        elif entry == 'Yes' or entry == 'Y':
            print('The aim of the game is to get your character \o@ to the secret door, which is hidden somewhere in the dungeon.')
            time.sleep(2)
            print('Although armed with your trusty sword \ and shield @ , you know they\'ll be no match against the fearsome monster which is hiding somewhere in the dungeon.')
            time.sleep(2)
            print('If you are 1 room away from the monster, you\'ll be able to hear it, so be careful! \nIf you are 1 room away from the door, you\'ll be able to make out a faint glow.')
            time.sleep(2)
            print('The coordinate system comes from the top-left (0,0), right and down.')
            time.sleep(2)
            break
        else:
            print('I didn\'t understand that. Please only enter Yes/Y, or No/N.')
            time.sleep(0.7)
            continue    
    while True:
        print('Firstly, what is your name?  It must be between 1 and 20 characters.')
        name = input ('> ')
        if len(name) > 0 and len(name) < 20:
            name = name
            break
        else:
            print('Sorry, your name must be between 1 and 20 characters, try again.')
            time.sleep(0.7)
            continue
        
    while True:
        print('How tall would you like the dungeon to be, {}? \nEnter a number between 2 and 9.'.format(name))
        try:
            rows = int(input('> '))
        except ValueError:
            print('That\'s not an integer!')
            time.sleep(0.7)
            continue
        if rows > 1 and rows < 10:
            rows = int(rows)
            break
        else:
            print('Sorry, input must be an integer between 2 and 9, try again.')
            time.sleep(0.7)
            continue

    while True:
        print('And how wide? Enter a number between 2 and 9.')
        try:
            cols = int(input('> '))
        except ValueError:
            print('That\'s not an integer!')
            time.sleep(0.7)
            continue
        if cols > 1 and cols < 10:
            cols = int(cols)
            break
        else:
            print('Sorry, input must be an integer between 2 and 9, please try again.')
            time.sleep(0.7)
            continue
    
    while True:
        print('What difficulty level would you like? Enter Easy, Medium or Hard.\nEasy level means you\'ll be able to detect both the door and the monster;\nMedium level means you\'ll only be able to detect the door;\nHard level means you can\'t detect either of them!')
        entry = input('> ').title()
        if entry not in permitted_game_difficulties:
           print('I didn\'t understand that. Please only enter Easy, Medium or Hard.\n')
           continue
        else:
          game_difficulty = entry
          break
    print('One moment please!')
    time.sleep(0.5)
    return [(x, y) for x in range(cols) for y in range(rows)]

def grid_drawer():
####  One or the other of these - depends on the upformat you want (blank rooms vs clear coordinates).
    x, y = player

    dungeon = [['¦{},{}'.format(x,y) for x in range(cols)] for y in range(rows)]
    character_sprite = '¦\o@'
    dungeon[y][x] = character_sprite
    print('+' + '---+' * (cols))
    for row in dungeon:
        print(''.join(row), end = '¦\n')
        print('+' + '---+' * (cols))   

#    dungeon = [['¦ ' for y in range(cols)] for x in range(rows)]
#    character_sprite = '¦#'
#    dungeon[y][x] = character_sprite
#    print('+' + '-+' * (cols))
#    for row in dungeon:
#        print(''.join(row), end = '¦\n')
#        print('+' + '-+' * (cols)) 

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
        print('\nYou can hear the monster close by!')
        time.sleep(0.7)
        
def door_location():
    x_player, y_player = player
    x_door, y_door = door
    if abs(x_door - x_player) <= 1 and abs(y_door - y_player) <= 1:
        print('\nYou can make out a faint ethereal glow!')
        time.sleep(0.7)
        
def get_moves(player):
    global moves
    moves = ['Left', 'Right', 'Up', 'Down']
    moves_permitted = moves[:]
    x, y = player
    if x == 0:
        moves_permitted.remove('Left')
    if x == cols-1:
        moves_permitted.remove('Right')
    if y == 0:
        moves_permitted.remove('Up')
    if y == rows-1:
        moves_permitted.remove('Down')
    return moves_permitted

def game_restart():
    while True:
        time.sleep(1)
        print('You have won {} games and lost {} games.'.format(win_loss_counter[0],win_loss_counter[1]))
        print('Would you like to play again? Enter Y/N.')
        answer = input('> ').title()
        if answer == 'Yes' or answer == 'Y':
            clear_screen()
            game_loop()
            break
        if answer == 'No' or answer == 'N':
            print('Goodbye {}!'.format(name))
            raise SystemExit(0)
        else:
            print('I didn\'t understand that. Please only enter Yes/Y, or No/N.')
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
##        print('The secret door is in room {}'.format(door))
##        print('The monster is in room {}'.format(monster))
        if game_difficulty == 'Easy':
          monster_location()
          door_location()
        elif game_difficulty == 'Medium':
          door_location()
        else:
          pass
        print('\nYou can move {}.'.format(', '.join(get_moves(player))))
        print('Or enter Quit to quit.')

        move = input('> ').title()
        if move == 'Quit':
            print('Goodbye {}!'.format(name))
            raise SystemExit(0)
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
            win_loss_counter[0] += 1
            game_restart()
        if player == monster:
            print('{} has been eaten by the monster!'.format(name))
            win_loss_counter[1] += 1
            game_restart()
        else:
            continue

game_loop()
####    Monster moves too?
####    Cursor keys to move?
