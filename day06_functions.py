 # --- PART 1: Basic functions ---

  # 1. Write a function called greet_character that takes a name
  #    and returns "Welcome to Fae's Hollow, {name}!"
def greet_character(name):
    return f"Welcome to Fae's Hollow, {name}!"
  # 2. Write a function called is_high_level that takes a level
  #    and returns True if level > 4, False otherwise
def is_high_level(level):
    return level > 4

  # 3. Write a function called summarise_character that takes
  #    name, class_type, and level (default level=1, default class_type="Wanderer")
  #    and returns a formatted string describing them
def summarise_character(name, class_type="Wanderer", level=1):
    return f"Your character's a level {level} {class_type} called {name}"


  # --- PART 2: Working with data ---

characters = [
    {"name": "Elowen", "level": 5, "class": "Witch", "gold": 1340.5},
    {"name": "Bramble", "level": 3, "class": "Ranger", "gold": 872.25},
    {"name": "Sable", "level": 4, "class": "Rogue", "gold": 210.0},
    {"name": "Pip", "level": 2, "class": "Bard", "gold": 95.0},
]

  # 4. Write a function called get_high_level_characters that takes
  #    a list of characters and returns only those with level > 3
def get_high_level_characters(all_characters):
    high_levelled = [c for c in all_characters if c["level"] > 3]
    return high_levelled
  # 5. Write a function called total_gold that takes a list of characters
  #    and returns the sum of all their gold
def total_gold(all_characters):
    return sum(c["gold"] for c in all_characters)

  # 6. Write a function called find_character that takes a list and a name,
  #    and returns the matching character dictionary, or None if not found
def find_character(all_characters, name):
    for c in all_characters:
        if c["name"] == name:
            return c
    return None

  # --- PART 3: Multiple return values ---

  # 7. Write a function called min_max_level that takes a list of characters
  #    and returns the lowest and highest level as two separate values
  #    Use it like: low, high = min_max_level(characters)
def min_max_level(all_characters):
    levels = [c["level"] for c in all_characters]
    levels.sort()
    return levels[0], levels[-1]

  # --- PART 4: Stretch ---

  # 8. Write a function called apply_to_all that takes a list of characters
  #    and a function, and returns a new list with that function applied
  #    to every character name.
  #    Example:
  #    apply_to_all(characters, str.upper) should return
  #    ["ELOWEN", "BRAMBLE", "SABLE", "PIP"]
def apply_to_all(all_characters, function):
    return [function(c["name"]) for c in all_characters]