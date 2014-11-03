
import os
import sys
import random
import time

# Fight scene between player and enemy!
#
# If player wins, delete the enemy from the room.


# Calculate damage from given attacker and defender
def calculate_damage(attacker, defender):
  armor = 0

  # Does defender have armor?
  if hasattr(defender, 'armor') and defender.armor != None:
    armor = defender.armor.defense

  damage = attacker.strength/2 + attacker.weapon.damage - armor
  return random.randrange(int(damage), 2 * int(damage)) - defender.defense



# Calculate the damage if critical hit
def calculate_critical_damage(attacker, defender):
  damage = attacker.strength/2 + attacker.weapon.damage
  return (random.randrange(damage, 2 * damage) +
          random.randrange(damage, 2 * damage) -
          defender.defense)

def fight(player, enemy, room):
  # Clear the screen
  if os.name == 'posix':
    os.system('clear')
  else:
    os.system('cls')

  # Enemy intro message
  print(enemy.generateintro() + "\n")

  # Battle loop
  while True:
    if player.health <= 0:
      print("You have died!")
      sys.exit()

    if enemy.health <= 0:
      print("You have won this battle!!!")
      print()
      print("You gained " + str(enemy.exp) + " xp!")

      player.add_exp(enemy.exp)

      room.enemies.remove(enemy)
      break

    print("You have " + str(player.health) + " health")
    print()
    print("1. Attack")
    print("2. Recover")
    print("3. Flee")

    command = input(">")
    option = 0

    # Check that we actually entered a number
    try:
      option = int(command)
    except ValueError:
      print("Please enter a number\n")
      continue

    # Check that we selected a menu option
    if option > 3 or option < 1:
      print("Please select a menu option\n")
      continue

    # Formulae from here:
    # http://www.gamefaqs.com/boards/522595-final-fantasy/41701255

    if option == 1:
      # Damage enemy
      damage = 0

      # Calculate whether critical hit
      if (random.randrange(0, 150) < player.dexterity):
        damage = calculate_critical_damage(player, enemy)
        print("\nCritical hit!\n")
      else:
        damage = calculate_damage(player, enemy)

      enemy.health -= damage;

      print("You hit the enemy for " + str(damage) + " with your " + player.weapon.name)

    if option == 2:
      # Calculate healing
      healing = random.randrange(round(player.max_health/6), round(player.max_health/4))

      player.health += healing

      print("You healed for " + str(healing) + " health")

    if option == 3:
      if random.random() > 0.4:
        # Flee
        print("You ran away!")
        return 0
      else:
        print("You failed to escape!")

    time.sleep(0.5)

    # Damage player
    damage = calculate_damage(enemy, player)
    player.health -= damage

    print("The enemy hit you for " + str(damage) + " with its " + enemy.weapon.name + "\n")


    time.sleep(0.5)

  player.health = player.max_health

