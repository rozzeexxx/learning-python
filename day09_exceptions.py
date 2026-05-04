  # --- PART 1: Basic exception handling ---

  # 1. Write a function called safe_divide that takes two numbers
  #    and returns the result of dividing them.
  #    Handle ZeroDivisionError — return None and print a message.
def safe_divide(number1,number2):
    try:
        division = number1/number2
    except ZeroDivisionError:
        print("Not a valid division")
        return None
    else:
        return division

  # 2. Write a function called safe_int that takes a string
  #    and tries to convert it to an integer.
  #    Handle ValueError — return None and print "Invalid number".
  #    Test it with "42", "hello", and "7"
def safe_int(string):
    try:
        integer = int(string)
    except ValueError:
        print("Invalid number")
        return None
    else:
        return integer

print(safe_int("42"))
print(safe_int("hello"))
print(safe_int("7"))


  # --- PART 2: Multiple exceptions and else/finally ---

  # 3. Write a function called get_character_stat that takes
  #    a character dictionary and a stat name.
  #    Try to return the stat — handle KeyError if it doesn't exist.
  #    Use else to print "Found it!" if successful.
  #    Use finally to always print "Search complete."
def get_character_stat(dictionary, stat_name):
    try:
        stat = dictionary[stat_name]
    except KeyError:
        return None
    else:
        print("Found it!")
        return stat
    finally:
        print("Search complete.")

  # 4. Write a function called safe_index that takes a list and an index
  #    and handles both IndexError and TypeError
  #    (TypeError happens if you pass a string as the index e.g. "two")
def safe_index(list, index):
    try:
        item = list[index]
    except IndexError:
        print("That's out of range.")
    except TypeError:
        print("Something's not the right type.")
    else:
        return item

  # --- PART 3: Raising exceptions ---

  # 5. Write a function called set_health that takes a health value.
  #    Raise a ValueError if health is below 0 or above 100.
  #    Otherwise return the value.
def set_health(health):
    if not 0 <= health <= 100:
        raise ValueError(f"Health outside range.")
    return health

  # 6. Create a custom exception called InvalidGoldError.
  #    Write a function called add_gold that takes a current amount
  #    and an amount to add. Raise InvalidGoldError if the amount
  #    to add is negative. Otherwise return the new total.
class InvalidGoldError(Exception):
    pass
def add_gold(current_amount, add_amount):
    if add_amount < 0:
        raise InvalidGoldError("Amount can't be negative")
    return current_amount + add_amount


  # --- PART 4: Stretch ---

  # 7. Write a function called load_character that takes a dictionary
  #    and a character name. It should:
  #    - Raise a KeyError if "characters" key doesn't exist in the dict
  #    - Raise a ValueError if the character name isn't in the list
  #    - Return the character if found
  #    Wrap a call to it in try/except that handles both errors
  #    with different messages
def load_character(dictionary, character_name):
    if "characters" not in dictionary["characters"]:
        raise KeyError("Characters doesnt exist")
    if character_name not in dictionary:
        raise ValueError("Name not found")
    return(f"Character found - {character_name}")
    
try:
    print(load_character({"characters": ["Elowen", "Bramble"]}, "Pip"))
except KeyError as e:
    print(f"Key error: {e}")
except ValueError as e:
    print(f"Value error: {e}")