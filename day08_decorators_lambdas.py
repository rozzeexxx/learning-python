 # --- PART 1: Lambdas ---

characters = [
    {"name": "Elowen", "level": 5, "gold": 1340.5},
    {"name": "Bramble", "level": 3, "gold": 872.25},
    {"name": "Sable", "level": 4, "gold": 210.0},
    {"name": "Pip", "level": 2, "gold": 95.0},
]

  # 1. Sort characters by level (ascending) using a lambda
sorted(characters, key=lambda c: c["level"])

  # 2. Sort characters by name length using a lambda
sorted(characters, key=lambda c: len(c["name"]))

  # 3. Sort characters by gold (descending) using a lambda
  #    Hint: use the reverse=True argument in sorted()
sorted(characters, key=lambda c: c["gold"], reverse=True)

  # 4. Using filter() and a lambda, get only characters with gold > 500
  #    filter(lambda, iterable) returns an iterator — wrap it in list()
list(filter(lambda c: c["gold"] > 500, characters))


  # --- PART 2: Decorators ---

  # 5. Write a decorator called log_call that prints
  #    "Calling: {function name}" before the function runs
  #    and "Done: {function name}" after it returns
  #    Apply it to a simple function of your choice and call it
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        result= func(*args, **kwargs)
        print(f"Done: {func.__name__}")
        return result
    return wrapper

@log_call
def greet(name):
    return f"welcome, {name}"

print(greet("Elowen"))

  # 6. Write a decorator called validate_level that checks if
  #    the first argument passed to a function is between 1 and 10.
  #    If not, print "Invalid level" and return None instead of running.
  #    Apply it to a function called describe_character(level, name)
def validate_level(func):
    def wrapper(*args, **kwargs):
        level = 1 <= args[0] <= 10
        if level == False:
            print(f"Invalid level")
            return None
        return func(*args, **kwargs)
    return wrapper

@validate_level
def describe_character(level, name):
    return f"Your character's called {name}, and it's level {level}"

print(describe_character(11,"El"))


  # --- PART 3: Stretch ---

  # 7. Write a decorator called repeat that runs the decorated
  #    function 3 times.
  #    Hint: call func(*args, **kwargs) three times inside wrapper
def repeat(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = func(*args, **kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper