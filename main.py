#!/usr/local/bin/python3

#                        ^    ^
#                       / \  //\
#         |\___/|      /   \//  .\
#         /O  O  \__  /    //  | \ \
#        /     /  \/_/    //   |  \  \
#        @___@'    \/_   //    |   \   \ 
#           |       \/_ //     |    \    \ 
#           |        \///      |     \     \ 
#          _|_ /   )  //       |      \     _\
#         '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.
#         ,-{        _      `-.|.-~-.           .~         `.
#          '/\      /                 ~-. _ .-~      .-~^-.  \
#             `.   {            }                   /      \  \
#           .----~-.\        \-'                 .~         \  `. \^-.
#          ///.----..>    c   \             _ -~             `.  ^-`   ^-_
#            ///-._ _ _ _ _ _ _}^ - - - - ~                     ~--,   .-~



# Standard modules
import sys
import random

# Our modules
from player import *
import room
import enemy
import battle
import weapon
import armor
import action



# This is where the player chooses their class (and thus, their starting stats).
def get_stats():
  class_input = input("Do you want to be a warrior, or thief? ")

  if (class_input.lower() == "warrior"):
    return {'str': 14, 'dex': 6, 'def': 16}
  elif (class_input.lower() == "thief"):
    return {'str': 10, 'dex': 18, 'def': 6}



def main():
  # Responses for bad input, these are picked randomly.
  bad_responses = ["I don't understand what you're saying",
                   "Does not compute. Does not compute.",
                   "Huh?",
                   "wut?",
                   "Say again?"]


  # Populate weapons list by parsing the weapon data file.
  weapons = weapon.parse_weapons('data/weapons.json')
  
  # Populate armor
  armors = armor.parse_armor('data/armor.json')
  
  # Populate enemies, passing in weapons (that they can wield)
  enemies = enemy.parse_enemies('data/enemies.json', weapons)

  # ID of current room (index for the rooms list)
  room_id = 3 # Changed from 0 for debugging purposes

  # Populate rooms in game
  rooms = room.parse_rooms('data/rooms.json', enemies, weapons, armors)

  # Print the description for the starting room!
  rooms[room_id].print_desc()

  # Set up player
  # Instantiate the player class, weapons[0] is the default weapon
  #p = Player(get_stats())
  player = Player({'str': 14, 'dex': 10, 'def': 16}, weapons[0]) 

  player.load_levels('data/levels.json') # Load the players leveling
  #player.armor = armors[0] # Give the player the basic armor
  player.add_inventory(armors[0])
  
  # Main game loop
  while True:
    # Here we parse the command by first splitting it by each space so
    # as to parse each word separately. The parsing is not case
    # sensitive so we lowercase the string before splitting.

    command = input("> ").lower().split()

    # Handle prop actions
    triggered = action.handle_actions(player, command, rooms[room_id])

    # Handle looking/examining objects, rooms or enemies.
    if (command[0] == 'look' or command[0] == 'examine'):

      # Subject string
      subject = ""

      # We can validly enter no subject to return the room description
      # so we check if command[1] exists before assigning it to subject
      if len(command) > 1:
        subject = command[1]
      else:
        subject = ""

      # No subject or room so print room description
      if subject == "" or subject == "room":
        rooms[room_id].print_desc()
        continue


      item_found = False # Used for item not found error

      # Print each enemy description if observed
      for e in rooms[room_id].enemies:

        # Check that enemy name starts with subject so we do
        # not have to type entire enemy name to look at them.
        if e.name.lower().startswith(subject):
          e.print_desc()
          item_found = True

      # Print each prop description if observed
      for prop in rooms[room_id].props:
        if prop.name.lower().startswith(subject):
          prop.print_desc()
          item_found = True

      # Print a nice error if no item is found
      if item_found == False:
        print("No item or enemy was found called " + "\"" + subject + "\"")


    elif (command[0] == 'fight' or command[0] == 'attack'):

      # If we do not enter a command, assume we want to fight the
      # first enemy in the room.
      if len(command) > 1:
        subject = command[1]
      else:
        battle.fight(player, rooms[room_id].enemies[0], rooms[room_id])
        continue


      enemy_found = False # For enemy not found error

      # Attack enemy if observed
      for e in rooms[room_id].enemies:
        # Check that enemy name starts with subject, and subject not empty.
        if e.name.lower().startswith(subject) and subject.isspace() == False:
          battle.fight(player, e, rooms[room_id])
          enemy_found = True

      # Print error if no enemy is found
      if enemy_found == False:
        print("No enemy was found called " + "\"" + subject + "\"")

    
    elif command[0].lower() == 'stats':
      player.print_stats()

    elif (command[0].lower() == 'n' or command[0].lower() == 's' or
        command[0].lower() == 'w' or command[0].lower() == 'e'):

      # Store the old room ID to check whether we ended up moving to a new room.
      old_room_id = room_id

      for exit in rooms[room_id].exits:
        # Change room if exit exits in direction chosen
          if exit['dir'] == command[0].lower():
            room_id = int(exit['id'])
            rooms[room_id].print_desc()

            break # No need to continue now we've found the exit.

      # If room didn't change, the choice didn't exist.
      if (old_room_id == room_id):
        print('Sorry, that room does not exist!')

    elif command[0].lower() == 'inventory':
      player.print_inventory()

    elif command[0].lower() == 'equip':
      player.equip_item(" ".join(command[1:]))

    elif command[0].lower() == 'take':
      subject = " ".join(command[1:])

      item_found = False  
      _item = None # Temp item for removing from list
      for item in rooms[room_id].items:
        if item.name.startswith(subject) and subject.isspace() == False:
          player.add_item(item)
          item_found = True
          _item = item

          break

      # Remove item from room so it can't be picked up again
      if not _item == None:
        rooms[room_id].items.remove(_item)

      if item_found == False:
        print("No item found named " + subject)


    elif command[0].lower() == 'equipment':
      player.print_equipment()

    # Quit the game
    elif (command[0].lower() == "exit" or command[0].lower() == "quit"):
      sys.exit()

    # No prop event triggered AND no command triggered, so print
    # an error telling us we put in an unrecognized command
    elif not triggered:
      print(bad_responses[random.randint(0, len(bad_responses) - 1)])


if __name__ == "__main__":
  main()
