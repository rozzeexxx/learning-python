  # --- PART 1: Basic operations ---

inventory = ["acorn cap", "dried lavender", "moonstone", "fox fur"]

  # 1. Print the first item and the last item (use indexing, not the name)
print(inventory[0])
print(inventory[-1])

  # 2. Add "enchanted quill" to the end of the inventory
inventory.append("enchanted quill")

  # 3. Insert "shadow cloak" at position 2
inventory.insert(2, "shadow cloak")

  # 4. Remove "dried lavender"
inventory.remove("dried lavender")

  # 5. Print how many items are in the inventory
print(len(inventory))

  # 6. Print the inventory sorted alphabetically (don't change the original)
print(sorted(inventory))

  # --- PART 2: The copy gotcha ---

  # 7. Make a real independent copy of inventory called "backup"
backup = inventory.copy()

  # 8. Clear the original inventory using .clear()
inventory.clear()

  # 9. Print both inventory and backup
  #    inventory should be empty, backup should still have all items
print(inventory)
print(backup)

  # --- PART 3: Stretch goal ---

  # A list of (item, quantity) pairs
supplies = [("moonstone", 3), ("candle", 10), ("potion", 2), ("scroll", 7)]

  # 10. Print only the items where quantity is greater than 2
for i in supplies:
    if i[1] > 2:
       print(i)

  # 11. Print the item names only, sorted by quantity from smallest to largest

for item in sorted(supplies, key=lambda item: item[1]):
    print(item[0])
