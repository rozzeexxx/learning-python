  # --- PART 1: Cleaning and transforming ---

raw_entries = [
    "  elowen ",
    "BRAMBLE",
    "  sable the rogue  ",
    "pip  ",
]

  # 1. Print each name cleaned (stripped and title cased)
for item in raw_entries:
  print(item.strip().title())

  # 2. Using a comprehension, build a list of cleaned names
clean_entries = [name.strip().title() for name in raw_entries]


  # --- PART 2: Splitting and joining ---

character_data = "Elowen,Witch,5,80,100"

  # 3. Split this string into a list
character_data_listed = character_data.split(",")

  # 4. Print the character's name, class and level from the split list
print(f"Name: {character_data_listed[0]}, Class: {character_data_listed[1]}, Level: {character_data_listed[2]}")

  # 5. Build a new string from the list joined with " | " as separator
character_data_reconstructed = " | ".join(character_data_listed)


  # --- PART 3: Checking contents ---

descriptions = [
    "A ancient grimoire bound in shadow",
    "A vial of moonpetal extract",
    "An enchanted silver compass",
    "A shadow cloak woven from nightfall",
    "A candle that never burns out",
]

  # 6. Print only descriptions that contain the word "shadow"
for sentence in descriptions:
    if "shadow" in sentence:
       print(sentence)

  # 7. Print only descriptions that start with "An"
for sentence in descriptions:
    if sentence.startswith("An"):
       print(sentence)


  # --- PART 4: f-string formatting ---

characters = [
    {"name": "Elowen", "level": 5, "gold": 1340.5},
    {"name": "Bramble", "level": 3, "gold": 872.25},
    {"name": "Sable", "level": 4, "gold": 210.0},
]

  # 8. Print a formatted table that looks like this:
  #            Name   Level    Gold
  #    Elowen         5        1340.50
  #    Bramble        3        872.25
  #    Sable          4        210.00
  #    Hint: use f"{value:<15}" for left-aligned columns
print(f"{"Name":<15} {"Level":<9} Gold")
for c in characters:
    print(f"{c["name"]:<15} {c["level"]:<9} {c["gold"]:.2f}")

  # --- PART 5: Stretch ---

  # 9. Take this messy string and extract just the item names as a clean list:
messy = "moonstone | candle  |  enchanted quill |fox fur|  scroll  "
  # Expected: ["moonstone", "candle", "enchanted quill", "fox fur", "scroll"]
  # Hint: split on "|" then strip each piece
clean_list = [item.strip() for item in messy.split("|")]
print(clean_list)
