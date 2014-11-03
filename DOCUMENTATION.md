Format
======


Armor
-----

Top level Array:

    { "armor" : [ ... ] }

*"Armor" object fields:*

    "name" : "..."

Name of piece of armor

    "desc" : "..."

Armor description

    "defense" : ...

Integer defense rating of armor


Weapons
-------

Top level Array:

    { "weapons" : [ ... ] }

*"Weapons" object fields:*

    "id" : ...

ID of weapon (unused in code)

    "name" : "..."

Name of weapon

    "desc" : "..."

Weapon description

    "damage" : ...

Base (integer) weapon damage


Rooms
-----

Top level Array:

    { "rooms" : [ ... ] }

*"Rooms" object fields:*

    "id" : ...

ID of room (unused in code)

    "desc" : "..."

Description of room (used when looked at)

    "exits" : [ ... ]

List of exit objects

    "props" : [ ... ]

List of prop objects

    "items" : [ ... ]

List of items in the room

*"Exit" object fields:*

    "id" : ...

Room that this exit leads to

    "dir" : "..."

Direction of exit


*"Prop" object fields:*

    "name" : "..."

Name of prop

    "desc" : "..."

Description when looked at

    "actions" : [ ... ]

List of action objects

*"Action" object fields*

The action object holds information about how an prop should react to certain stimuli commands like "look" or "touch"

    "stimuli" : "..."

Trigger command

    "action" : { }

This is dependent on action type, see ACTIONS.md


*"Item" object fields*

The item field is to allow the player to be able to pick up items from the floor

"type" : "..."

This is the type of item to be picked up (e.g. "armor", or "weapon")

"id" : ...

The integer ID of the item to equip. For example, if this were a weapon, it would get the weapon with the index "ID".


Enemies
-------

Top level list

    "enemies" : [ ... ]

*"enemies" object fields*

    "id" : ...

ID of enemy (unused in code)

    "name" : "..."

Name of enemy

    "desc" : "..."

Description of enemy when looked at

    "health" : ...

Health of enemy on spawn

    "str" : ...

Base strength attribute of enemy

    "def" : ...

Base defense of enemy

    "weapon_id" : ...

ID of weapon held by enemy (from weapons.json) for now it doesn't refer to the ID but to the order of the weapons

    "exp" : ...

Exp rewarded to player upon defeating enemy

    "intro" : "..."

Intro message on battle entrance


Levels
------

Top level list

    { "levels" : [ ... ] }

*"level" object fields*

    "level" : ...

Level to be advanced to

    "exp_needed" : ...

Exp needed to get to that level
