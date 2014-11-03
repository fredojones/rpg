import json
from weapon import *

class Enemy:

  def __init__(self, name, desc):
    self.name = name
    self.desc = desc
    self.strength = 0
    self.health = 0
    self.defense = 0
    self.weapon = None
    self.exp = 0
    self.intro = ""

  def print_desc(self):
    print(self.name)
    print()
    print(self.desc)
    print()

  # generate battle introduction
  def generateintro(self):
    intro = ""

    if not self.intro == "":
      intro = self.intro
    else:
      intro = "stands before you!"

    return "The " + self.name.lower() + " " + intro


# return a list of enemies parsed from json, getting
# weapons from global list of all weapons
def parse_enemies(filepath, weapons):
  f = open(filepath, 'r')

  raw = json.load(f)

  enemies = []

  # populate list
  for enemy in raw['enemies']:
    _name = ""
    _desc = ""

    # check if attribute exists in dictionary
    if 'name' in enemy:
      _name = enemy['name']
    if 'desc' in enemy:
      _desc = enemy['desc']

    # generate enemy
    e = Enemy(_name, _desc)

    # fill optional stuff
    if 'health' in enemy:
      e.health = int(enemy['health'])
    if 'str' in enemy:
      e.strength = int(enemy['str'])
    if 'def' in enemy:
      e.defense = int(enemy['def'])
    if 'weapon_id' in enemy:
      e.weapon = weapons[int(enemy['weapon_id'])] # get weapon from id
    if 'exp' in enemy:
      e.exp = int(enemy['exp'])
    if 'intro' in enemy:
      e.intro = enemy['intro']

    enemies.append(e)

  return enemies

