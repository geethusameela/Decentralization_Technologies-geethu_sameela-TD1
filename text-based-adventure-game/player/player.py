class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} added to your inventory.")

    def display_inventory(self):
        print("Inventory:")
        for item in self.inventory:
            print(f"- {item}")
