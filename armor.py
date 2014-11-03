import json

class Armor:

  def __init__(self, name, desc, defense):
    self.name = name
    self.desc = desc
    self.defense = defense



# Return a list of armor
def parse_armor(filepath):
  f = open(filepath, 'r')

  raw = json.load(f)

  armors = []

  for armor in raw["armor"]:
    _name = ""
    _desc = ""
    _defense = 0

    if 'name' in armor:
      _name = armor['name']
    if 'desc' in armor:
      _desc = armor['desc']
    if 'defense' in armor:
      _defense = int(armor['defense'])

    armors.append(Armor(_name, _desc, _defense))

  return armors
