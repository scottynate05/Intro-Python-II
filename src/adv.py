from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player('Nate', current_room = room['outside'])
print(f"\n{player1.name}'s starting room: {player1.current_room.name}")
print(f"{player1.current_room.description}")

while True:
    movement = {
        'n': lambda x: x.n_to,
        's': lambda x: x.s_to,
        'e': lambda x: x.e_to,
        'w': lambda x: x.w_to,
    }
    user_input = input('\nWhere would you like to go? ')
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
                print(f'\n{player1.name} enters the {player1.current_room.name}')
                print(f'{player1.current_room.description}')
            else:
                exit()
        else:
            print(f'\nYou cannot go that way, "{user_input}" is not a valid '
                f'direction.\n[n] Move North   [w] Move West   [s] Move South   [e] Move East   [q] Quit')
            print(f'\n{player1.name} is currently at the {player1.current_room.name}')
            print(f'{player1.current_room.description}')
    except:
        print("\nMovement not allowed")
        print(f'\n{player1.name} is currently at the {player1.current_room.name}')
        print(f'{player1.current_room.description}')

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
