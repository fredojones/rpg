
class Prop:

  def __init__(self, name, desc, actions):
    self.name = name
    self.desc = desc
    self.actions = actions

  def print_desc(self):
    print(self.name)
    print()
    print(self.desc)
    print()
