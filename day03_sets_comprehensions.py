  # --- PART 1: Sets ---

loot_drops = ["moonstone", "candle", "moonstone", "scroll",
            "candle", "fox fur", "scroll", "moonstone"]

  # 1. Remove all duplicates and store as a set called "unique_loot"
unique_loot = set(loot_drops)

  # 2. Print how many unique items there are
print(len(unique_loot))

  # 3. Check if "potion" is in unique_loot and print a message either way
if "potion" in unique_loot:
    print("yes")
else:
    print("no")

rival_loot = {"scroll", "potion", "silver ring", "candle"}

  # 4. Print items that appear in BOTH collections
print(rival_loot & unique_loot)

  # 5. Print items Elowen has that the rival does NOT have
print(unique_loot - rival_loot)


  # --- PART 2: Tuple unpacking ---

party = [("Elowen", "Witch", 5), ("Bramble", "Ranger", 3), ("Sable", "Rogue", 4)]


  # 6. Loop through party using tuple unpacking and print:
  #    "Elowen is a level 5 Witch"  (one line per character)
for name, job, level in party:
    print(name, "is a level", level, job)


  # --- PART 3: List comprehensions ---

characters = [
    {"name": "Elowen", "level": 5, "class": "Witch"},
    {"name": "Bramble", "level": 3, "class": "Ranger"},
    {"name": "Sable", "level": 4, "class": "Rogue"},
    {"name": "Pip", "level": 2, "class": "Bard"},
]

  # 7. Use a comprehension to make a list of all character names
names = [character["name"] for character in characters]

  # 8. Use a comprehension to make a list of names where level > 3
namesHighLevel = [character["name"] for character in characters if character["level"] > 3]

  # 9. Use a comprehension to make a list of strings formatted as:
  #    "Elowen (Witch)" for each character
nameAndClass = [f'{character["name"]} ({character["class"]})' for character in characters]

  # 10. STRETCH: Use a comprehension to build a dictionary where
  #     the key is the character's name and the value is their level
  #     e.g. {"Elowen": 5, "Bramble": 3, ...}
  #     Hint: use {key: value for item in collection}
nameAndLevel = {character["name"]: character["level"] for character in characters}