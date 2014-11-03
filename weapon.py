import json

class Weapon:

  def __init__(self, name, desc, damage):
    self.name = name
    self.desc = desc
    self.damage = damage



# Return a list of weapons
def parse_weapons(filepath):
  f = open(filepath, 'r')

  raw = json.load(f)

  weapons = []

  for weapon in raw["weapons"]:
    _name = ""
    _desc = ""
    _damage = 0

    if 'name' in weapon:
      _name = weapon['name']
    if 'desc' in weapon:
      _desc = weapon['desc']
    if 'damage' in weapon:
      _damage = int(weapon['damage'])

    weapons.append(Weapon(_name, _desc, _damage))


  return weapons

