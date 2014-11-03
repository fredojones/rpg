import json
import copy

from prop import *
from action import *

class Room:

  def __init__(self, desc, exits, enemies, props, items):
    self.desc = desc
    self.exits = exits
    self.enemies = enemies
    self.props = props
    self.items = items

  def print_desc(self):
    print(self.desc + "\n")

    if len(self.exits) > 0:
      exit_string = 'There are exits: '
      
      for exit in self.exits:
        exit_string += exit['dir'] + " "

      print(exit_string + "\n")
   

    if len(self.enemies) > 0:
      print ("There are enemies here:")
    
      for enemy in self.enemies:
        print(enemy.name)



# Return a list of rooms parsed from JSON
# also fills room with enemies in game.
def parse_rooms(filepath, enemies, weapons, armor):
  f = open(filepath, 'r')

  raw = json.load(f)

  rooms = []

  # Populate list
  for room in raw['rooms']:
    _desc = ''
    _exits = []
    _enemies = []
    _props = []
    _items = []

    # Check if attribute exists in dictionary
    if 'desc' in room:
      _desc = room['desc']
    if 'exits' in room:
      _exits = room['exits']
    if 'enemies' in room:
      _enemies = room['enemies']
    if 'props' in room:
      # Create prop objects
      for prop in room['props']:
        _actions = []
        
        if 'actions' in prop:
          for action in prop['actions']:
            _actions.append(Action(action['stimuli'], action['action']))

        _props.append(Prop(prop['name'], prop['desc'], _actions))
    
    if 'items' in room:
      # Create item objects
      for item in room['items']:
        if item['type'] == 'weapon':
          _items.append(weapons[item['id']])
        if item['type'] == 'armor':
          _items.append(weapons[item['id']])


    # Populate enemies
    _enemyobjects = []

    for enemy_id in _enemies:
      _enemyobjects.append(copy.deepcopy(enemies[int(enemy_id)]))

    rooms.append(Room(_desc, _exits, _enemyobjects, _props, _items))


  return rooms

