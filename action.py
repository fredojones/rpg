

class Action:

  def __init__(self, stimuli, action):
    self.stimuli = stimuli
    self.action = action



# Handle and trigger prop actions and
# return true if action triggered, else false.
def handle_actions(player, command, room):

  triggered = False

  for prop in room.props: 
    for action in prop.actions:
      # Action triggered
      if action.stimuli == command[0].lower():
        
        # Hurt something
        if action.action['type'] == 'damage':
          
          if action.action['subject'] == 'player':
            damage = action.action['amount']
            player.health -= damage
            
            print("Ow! You were hurt for " + str(damage) +  " health!")

        
        # Say something
        if action.action['type'] == 'say':
          print(action.action['message'])

        # An action was triggered
        triggered = True

  return triggered




