import json

from weapon import *
from armor import *

class Player:
  health = 100
  max_health = health

  inventory = []

  level = 1
  exp = 0

  # Contains dict of information about each level 
  levels = {}

  # Hold armor object
  armor = None

  def __init__(self, stats, weapon):
    self.strength = stats['str']
    self.dexterity = stats['dex']
    self.defense = stats['def']

    self.weapon = weapon

    self.add_inventory(weapon)


  def print_stats(self):
    print("Health: " + str(self.health))
    print()
    print("Level: " + str(self.level))
    print()
    print("Str: " + str(self.strength))
    print("Dex: " + str(self.dexterity))
    print("Def: " + str(self.defense))
    print()


  def add_exp(self, exp):
    self.exp += exp
    
    if self.exp > self.levels[self.level + 1]:
      self.level += 1
      self.exp = 0

      # Boost stats
      self.strength += 1
      self.dexterity += 1
      self.defense += 1

      print("You leveled up! You are now level " + str(self.level) + "!")

  # Load level dict from file
  def load_levels(self, filepath):
    f = open(filepath, 'r')

    raw = json.load(f)

    for level in raw['levels']:
      self.levels[int(level['level'])] = int(level['exp_needed'])

  
  def add_inventory(self, item):
    self.inventory.append(item);

  def print_inventory(self):
    print("You are currently carrying: ")
    
    for item in self.inventory:
      if item == self.armor or item == self.weapon:
        print(item.name + " (equipped)")
      else:
        print(item.name)

    print()

  def print_equipment(self):
    if self.weapon == None:
      print("You are without a weapon!")
    else:
      print("You are wielding the " + self.weapon.name)

    if self.armor == None:
      print("You are without armor!")
    else:
      print("You are wearing the " + self.armor.name)

    print()

  def equip_item(self, item):
    # if item equipped, check it's type and set appropriately
    for i in self.inventory:
      if i.name.lower().startswith(item):
        print("You equipped the " + i.name)

        if isinstance(i, Armor):
          self.armor = i
          return
        elif isinstance(i, Weapon):
          self.weapon = i
          return

    # if we get here, no armor was found
    print("No item found called " + item)

  def add_item(self, item):
    self.inventory.append(item);

    print("You picked up the " + item.name.lower())


