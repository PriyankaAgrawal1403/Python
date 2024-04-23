 class Inventory:
  def __init__(self):
      self.items = {}

  def add_item(self, item, quantity):
      if item in self.items:
          self.items[item] += quantity
      else:
          self.items[item] = quantity
      print(f"{quantity} {item}(s) added to inventory.")

  def remove_item(self, item, quantity):
      if item in self.items:
          if self.items[item] >= quantity:
              self.items[item] -= quantity
              print(f"{quantity} {item}(s) removed from inventory.")
          else:
              print(f"Not enough {item} in inventory.")
      else:
          print(f"{item} not found in inventory.")

  def display_inventory(self):
      print("Current Inventory:")
      for item, quantity in self.items.items():
          print(f"{item}: {quantity}")

def main():
  inventory = Inventory()

  while True:
      print("\n1. Add Item")
      print("2. Remove Item")
      print("3. Display Inventory")
      print("4. Exit")
      choice = input("Enter your choice (1-4): ")

      if choice == '1':
          item = input("Enter item name: ")
          quantity = int(input("Enter quantity: "))
          inventory.add_item(item, quantity)
      elif choice == '2':
          item = input("Enter item name: ")
          quantity = int(input("Enter quantity: "))
          inventory.remove_item(item, quantity)
      elif choice == '3':
          inventory.display_inventory()
      elif choice == '4':
          print("Exiting...")
          break
      else:
          print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
  main()