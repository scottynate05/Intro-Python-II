# -*- coding: utf-8 -*-
from room import Room
from player import Player
from item import Item

# Declare all the rooms

sword = Item('Swamp-Sword', 'Ain\'t the sharpest tool in the shed ¯\_(ツ)_/¯ ')
rose = Item('Golden-Rose', 'Gives ultimate power, you have won!')
rock = Item('Muddy-Boulder', 'Seems useless, very heavy.')

room = {
    'hole': Room('\n⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀\n⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀\n⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆\n⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆\n⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆\n⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿\n⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉\n⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇\n⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇\n⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇\n⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃\n⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉', "Hole right behind you...", "You stumble backwards falling into it. You hear the faint sound of someone breathing, and a stench like no other. You look over your shoulder, and you see it... What is it? Who is it? Wait... it's... it's him! \n'Donkey?!?!' \nHe says. \n'It's me, Shrek!' \nIn the distance you hear the anthem roaring... 'SOMEBODY ONCE TOLD ME THE WORLD IS GONNA ROLL ME...' \nThis is your life now.", [sword]),

    'outside':  Room('          /\ \n         /**\ \n        /****\   /\ \n       /      \ /**\ \n      /  /\    /    \        /\    /\  /\      /\            /\/\/\  /\ \n     /  /  \  /      \      /  \/\/  \/  \  /\/  \/\  /\  /\/ / /  \/  \ \n    /  /    \/ /\     \    /    \ \  /    \/ /   /  \/  \/  \  /    \   \ \n   /  /      \/  \/\   \  /      \  /     /    \ \n__/__/_______/___/__\___\__________________________________________________', "Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room(' \n                     / ^ \              /\'\       _ \n|\_..           /\'.,/     \_         .,\'   \     / \_ \n|    \         /            \      _/       \_  /    \     _\n|     \__,.   /              \    /           \/.,   _|  _/ \ \n|          \_/                \  /\',.,\'\'\      \_ \_/  \/    \ \n|                           _  \/   /    \',../\',.\    _/      \ \n|             /           _/m\  \  /    |         \  /.,/\'\   _\ \n|           _/           /MMmm\  \_     |          \/      \_/  \ \n|          /      \     |MMMMmm|   \__   \          \_       \   \_ \n|                  \   /MMMMMMm|      \   \           \       \    \ \n|                   \  |MMMMMMmm\      \___            \_      \_   \ \n|                    \|MMMMMMMMmm|____.\'  /\_            \       \   \_ \n|                    /\'.,___________...,,\'   \            \   \        \ \n|                   /       \          |      \    |__     \   \_       \ \n|                 _/        |           \      \_     \     \    \       \_ \n|                /                               \     \     \_   \        \ \n|                                                 \     \      \   \__      \ \n|                                                  \     \_     \     \      \ \n|                                                   |      \     \     \      \ \n|                                                    \            |            \ ', "Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [rock]),

    'overlook': Room('            ^^                   @@@@@@@@@\n       ^^       ^^            @@@@@@@@@@@@@@@\n                            @@@@@@@@@@@@@@@@@@              ^^\n                           @@@@@@@@@@@@@@@@@@@@\n ~~~~ ~~ ~~~~~ ~~~~~~~~ ~~ &&&&&&&&&&&&&&&&&&&& ~~~~~~~ ~~~~~~~~~~~ ~~~\n ~         ~~   ~  ~       ~~~~~~~~~~~~~~~~~~~~ ~       ~~     ~~ ~\n   ~      ~~      ~~ ~~ ~~  ~~~~~~~~~~~~~ ~~~~  ~     ~~~    ~ ~~~  ~ ~~\n   ~  ~~     ~         ~      ~~~~~~  ~~ ~~~       ~~ ~ ~~  ~~ ~\n ~  ~       ~ ~      ~           ~~ ~~~~~~  ~      ~~  ~             ~~\n       ~             ~        ~      ~      ~~   ~             ~\n', "Grand Overlook", """A steep cliff appears before you, falling
into the dark water below. Ahead to the north, the sun sets on the watery horizon. A light flickers on
the distance beach beneath you, but there is no way down the chasm.""", []),

    'narrow':   Room(' \n|        \    /\  /****\     / \n|         |  / *\/  **  \   | \n|         \ /   / ...... \ / \n|          \ ............ / \n|           | .......... | \n|            \  ......  / \n|             \  ....  / \n|              |  ..  / \n|               \ , ,| \n|                /  / \n|               /  / \n|              |  | \n|              \  \ \n|               \  \ \n|               |   |', "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room('                ..ooo.\n             .888888888.\n             88"P""T"T888 8o\n         o8o 8.8"8 88o."8o 8o\n        88 . o88o8 8 88."8 88P"o\n       88 o8 88 oo.8 888 8 888 88\n       88 88 88o888" 88"  o888 88\n       88."8o."JEJ88P.88". 88888 88\n       888."888."88P".o8 8888 888\n       "888o"8888oo8888 o888 o8P"\n        "8888.""888P"P.888".88P\n         "88888ooo  888P".o888\n           ""8P"".oooooo8888P\n  .oo888ooo.    8888NATE8P8\no88888"888"88o.  "8888"".88   .oo888oo..\n 8888" "88 88888.       88".o88888888"888.\n "8888o.""o 88"88o.    o8".888"888"88 "88P\n  T888C.oo. "8."8"8   o8"o888 o88" ".=888"\n   88888888o "8 8 8  .8 .8"88 8"".o888o8P\n    "8888C.o8o  8 8  8" 8 o" ...o"""8888\n      "88888888 " 8 .8  8   88888888888"\n        "8888888o  .8o=" o8o..o(8oo88"\n            "888" 88"    888888888""\n                o8P       "888"""\n          ...oo88\n "8oo...oo888""', "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [rose]),
}


# Link rooms together

room['hole'].n_to = room['outside']
room['outside'].s_to = room['hole']
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# def addItem(roomName, itemName):
#     for i, item in enumerate(room[roomName].items):
#         if item.name == itemName:
#             player1.items.append(room[roomName].items[i])
#             room[roomName].items[i].on_take()
#             del room[roomName].items[i]
#             break

# def dropItem(roomName, itemName):
#     for i, item in enumerate(player1.items):
#         if item.name == itemName:
#             room[roomName].items.append(player1.items[i])
#             player1.items[i].on_drop()
#             del player1.items[i]
#             break

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player('Nate', current_room = room['outside'], bag = [])
print(f"\n{player1.current_room.art}")
print(f"\n{player1.name}'s starting room: {player1.current_room.name}")
print(f"{player1.current_room.description}")
print(f"Items In Room: {player1.current_room.items}")

while True:
    user_input = input('\nWhere would you like to go? ')
    if user_input == 'i':
        if len(player1.bag) > 0:
            for i, item in enumerate(player1.bag):
                print(f'\nInventory : \n{i + 1}) {item}')
        else:
            print("You haven't picked up any items")
        user_input = input('\nWhere would you like to go? ')
    if user_input == 't':
        for item in player1.current_room.items:
            player1.bag.append(item)
            player1.current_room.items.remove(item)
    elif user_input == 'd':
        for item in player1.bag:
                player1.current_room.items.append(item)
                player1.bag.remove(item)
    movement = {
        'n': lambda x: x.n_to,
        's': lambda x: x.s_to,
        'e': lambda x: x.e_to,
        'w': lambda x: x.w_to,
    }
    # user_input = input('\nWhere would you like to go? ')
    if user_input == 'q':
        print('\nThank you for playing!')
        exit()
    try:
        if not user_input:
            continue
        else:
            user_input = user_input[0].lower()
        if user_input in movement.keys():
            target = movement[user_input](player1.current_room)
            if target:
                player1.current_room = target
                print(f"\n{player1.current_room.art}")
                print(f'\n{player1.name} enters the {player1.current_room.name}')
                print(f'{player1.current_room.description}')
                for i, item in enumerate(player1.current_room.items):
                    print(f"\nItems In Room: \n{item}")
            else:
                exit()
        else:
            print(f'\nYou cannot go that way, "{user_input}" is not a valid '
                f'direction.\n[n] Move North   [w] Move West   [s] Move South   [e] Move East   [q] Quit')
            print(f"\n{player1.current_room.art}")
            print(f'\n{player1.name} is currently at the {player1.current_room.name}')
            print(f'{player1.current_room.description}')
            for i, item in enumerate(player1.current_room.items):
                print(f"\nItems In Room: \n{item}")
    except:
        print("\nMovement not allowed")
        print(f"\n{player1.current_room.art}")
        print(f'\n{player1.name} is currently at the {player1.current_room.name}')
        print(f'{player1.current_room.description}')
        for i, item in enumerate(player1.current_room.items):
            print(f"\nItems In Room: \n{item}")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
