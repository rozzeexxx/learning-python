import random
 # --- PART 1: range and enumerate ---

inventory = ["moonstone", "candle", "enchanted quill", "fox fur", "scroll"]

  # 1. Print each item numbered from 1 using enumerate
  #    Output should look like:
  #    1. moonstone
  #    2. candle  etc.
for i, item in enumerate(inventory, start=1):
    print(f'{i}. {item}')

  # 2. Using range, print every item at an even index (0, 2, 4...)
for item in range(0,len(inventory),2):
    print(inventory[item])



  # --- PART 2: zip ---

characters = ["Elowen", "Bramble", "Sable"]
health = [80, 60, 70]
mana = [100, 40, 55]

  # 3. Using zip, print each character's name, health, and mana on one line
  #    Hint: you can zip more than two lists
for name, health_level, mana_level in zip(characters, health, mana):
    print(f'Name: {name}, Health: {health_level}, Mana: {mana_level}')


  # --- PART 3: while ---

  # 4. A character has 100 health. A monster deals 17 damage per turn.
  #    Use a while loop to simulate combat — print the health after each turn.
  #    When health hits 0 or below, print "Defeated!" instead.
health = 100
monster_damage = 17
while health > 0:
    print("Monster hits and deals 17 points")
    health -= monster_damage
    print("New health: ", health)
print("Defeated!")

  # 5. A character is searching a dungeon. Use a while loop that keeps
  #    "searching" (just print "Searching...") until they find a key.
  #    Randomly decide each turn if the key is found.
  #    Hint: use the random module — import random, then random.random()
  #    returns a float between 0 and 1. If it's above 0.8, the key is found.
  #    Use break to exit when found.
key = False
while key is False:
    print("Searching...")
    if random.random() > 0.8:
        print("Key is found")
        key = True



  # --- PART 4: nested loops ---

floors = ["ground floor", "upper floor", "basement"]
rooms = ["library", "kitchen", "study"]

  # 6. Print every combination of floor and room
for floor in floors:
    for room in rooms:
        print(f"{floor} - {room}")

  # 7. STRETCH: Same as above but skip any combination that includes
  #    "basement" and "kitchen" together — use continue
for floor in floors:
    for room in rooms:
        if room == "kitchen" and floor == "basement":
            continue
        print(f"{floor} - {room}")