 # --- PART 1: Scope ---

level = 10   # global

  # 1. Write a function called display_level that reads the global
  #    level variable and prints it — don't pass it as a parameter.
  #    Then write a second function called update_level that takes
  #    a current_level and amount, and returns current_level + amount.
  #    Call it like: level = update_level(level, 5)
  #    Print level before and after to show it worked.
def display_level():
    print(level)
display_level()
def update_level(current_level,amount):
    return current_level + amount
level = update_level(level,5)
display_level()



  # --- PART 2: *args ---

  # 2. Write a function called total_damage that accepts any number
  #    of hit values and returns their sum
def total_damage(*hits):
    return sum(hits)

  # 3. Write a function called describe_party that accepts any number
  #    of character names and prints:
  #    "The party contains: Elowen, Bramble, Sable"
def describe_party(*party_names):
    all_names = ", ".join(party_names)
    print(f"The party contains: {all_names}")


  # --- PART 3: **kwargs ---

  # 4. Write a function called create_character that accepts **kwargs
  #    and returns a dictionary of whatever was passed in
  #    e.g. create_character(name="Elowen", level=5) returns
  #    {"name": "Elowen", "level": 5}
def create_character(**character_information):
    return character_information

  # 5. Write a function called character_summary that accepts **kwargs
  #    and prints each key and value on its own line
  #    Call it with at least name, level, and class_type
def character_summary(**character_information):
    for key, value in character_information.items():
        print(f"{key}: {value}")

character_summary(name= "Elowen", level= 5, class_type= "Wanderer")

  # --- PART 4: Nested functions ---

  # 6. Write a function called combat_round that takes
  #    attacker_name, base_damage, and bonus_damage.
  #    Inside it, write a nested function called calculate_damage
  #    that adds base and bonus together.
  #    Return a string like: "Elowen strikes for 15 damage!"
def combat_round(attacker_name, base_damage, bonus_damage):
    def calculate_damage(base_damage, bonus_damage):
        return base_damage + bonus_damage
    return f"{attacker_name} strikes for {calculate_damage(base_damage, bonus_damage)} damage!"



  # --- PART 5: Stretch ---

  # 7. Write a function called flexible_summary that accepts:
  #    - one required argument: name
  #    - *args for any number of traits (e.g. "brave", "cunning")
  #    - **kwargs for any number of stats (e.g. level=5, gold=100)
  #    Print a summary using all of them:
  #    "Elowen | Traits: brave, cunning | level: 5, gold: 100"
def flexible_summary(name,*traits,**stats):
    all_traits = ", ".join(traits)
    all_stats = ", ".join(f"{key}: {value}" for key, value in stats.items())
    print(f"{name} | Traits: {all_traits} | {all_stats}")