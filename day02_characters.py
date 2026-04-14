 # --- PART 1: Basic dictionary operations ---

character = {
    "name": "Elowen",
    "class": "Witch",
    "level": 5,
    "health": 80
}

  # 1. Print the character's name and class using dictionary access
print(character["name"],character["class"])

  # 2. Add a "mana" key with value 60
character["mana"] = 60

  # 3. The character levels up — increase "level" by 1
character["level"] += 1

  # 4. Use .get() to safely print the value of "stamina"
  #    (it doesn't exist — make sure it doesn't crash, show 0 as default)
print(character.get("stamina",0))

  # 5. Print all keys and values using .items()
for key,value in character.items():
    print(key, ":", value)


  # --- PART 2: Working with multiple characters ---

party = [
    {"name": "Elowen", "class": "Witch", "level": 5},
    {"name": "Bramble", "class": "Ranger", "level": 3},
    {"name": "Sable", "class": "Rogue", "level": 4},
]

  # 6. Print the name and class of every character in the party
for item in party:
    print(item["name"],item["class"])

  # 7. Print only the characters whose level is above 3
for item in party:
    if item["level"] > 3:
        for key, value in item.items():
            print(key, ":", value)

  # --- PART 3: Nested dictionaries ---

character = {
    "name": "Elowen",
    "stats": {
        "strength": 4,
        "magic": 9,
        "agility": 6
    },
    "inventory": ["moonstone", "candle", "enchanted quill"]
}

  # 8. Print Elowen's magic stat
print(character["stats"]["magic"])

  # 9. Add "luck": 7 to her stats
character["stats"]["luck"] = 7

  # 10. Add "shadow cloak" to her inventory
  #     (her inventory is a list — what method do you use?)
character["inventory"].append("shadow cloak")