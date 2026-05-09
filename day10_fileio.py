 # day10_fileio.py

import json
import os
import random

characters = [
    {"name": "Elowen", "level": 5, "class": "Witch", "gold": 1340.5},
    {"name": "Bramble", "level": 3, "class": "Ranger", "gold": 872.25},
    {"name": "Sable", "level": 4, "class": "Rogue", "gold": 210.0},
    {"name": "Pip", "level": 2, "class": "Bard", "gold": 95.0},
]

  # 1. Save the characters list to a file called "characters.json"
  #    Use indent=4 for readability
with open("characters.json", "w") as f:
    json.dump(characters, f, indent = 4)
  # 2. Load the characters back from "characters.json"
  #    and print each character's name and level
with open("characters.json", "r") as f:
    characters = json.load(f)
    for c in characters:
        print(f"{c['name']} is level {c['level']}")

  # 3. Check if "characters.json" exists using os.path.exists
  #    and print an appropriate message either way
if os.path.exists("characters.json"):
    print("It exists")
else:
    print("It doesn't exist")
  # 4. Add a new character to the loaded list and save it
  #    back to the file — the file should now have 5 characters
characters.append({"name": "Warner", "level": 21, "class": "Mage", "gold": 459.66})
with open("characters.json", "w") as f:
    json.dump(characters, f, indent=4)

  # 5. Write a function called save_character(character, filename)
  #    that appends a single character to an existing JSON file
  #    (load the list, append, save back)
def save_character(character, filename):
    with open(f"{filename}.json", "r") as f:
        characters = json.load(f)
    characters.append(character)
    with open(f"{filename}.json", "w") as f:
        json.dump(characters, f, indent=4)


  # 6. Write a function called load_character(name, filename)
  #    that loads the JSON file and returns the matching character
  #    or None if not found
def load_character(name, filename):
    with open(f"{filename}.json", "r") as f:
        character = json.load(f)
    for c in character:
        if c["name"] == name:
            return c
    return None

  # 7. Using random.choice, pick a random character from the loaded
  #    list and print their full details using an f-string
random_character = random.choice(characters)
print(f"You got {random_character["name"]}. Their level is {random_character["level"]}, and is a {random_character["class"]}. They have {random_character["gold"]} gold.")

  # --- STRETCH ---

  # 8. Write a function called backup_characters(filename)
  #    that reads the JSON file and writes a copy called
  #    "{filename}_backup.json"
  #    Use os.path.exists to check the original exists first
def backup_characters(filename):
    if os.path.exists(f"{filename}.json"):
        with open(f"{filename}.json", "r") as f:
            data = json.load(f)
        with open(f"{filename}_backup.json", "w") as f:
            json.dump(data, f, indent=4)
