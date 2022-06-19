import sys

class stock:
    def __init__(self):
        self.amount = 0
    
    def add_stock(self):
        self.amount += 1

class appliances(stock):
    def __init__(self, name: str):
        super(appliances, self).__init__()
        self.type = name

class electronics(stock):
    def __init__(self):
        super(electronics, self).__init__()

class textiles(stock):
    def __init__(self):
        super(textiles, self).__init__()

class warehouse:
    def __init__(self):
        print('init function')
        self.inventory = None

    def create_inventory(self, items): #list of items to create an inventory from
        self.inventory = {i: items.count(i) for i in items}

    def add_items(self, items):
        "By taking the dictionary of original inventory and the list of items we want to add, return the inventory update"
        if self.inventory == None:
            self.inventory = self.create_inventory(items)
        keys = set(list(self.inventory.keys()) + list(items.keys()))
        return {key: self.inventory.get(key, 0) + items.get(key, 0) for key in keys}

    def decrement_items(self, inventory, items):
        """param inventory: dict - inventory dictionary. :param items: list - list of items to decrement from the inventory.
        :return: dict - updated inventory dictionary with items decremented."""
        items = create_inventory(items)
        return {key: inventory[key] - items.get(key, 0) if inventory[key] > items.get(key, 0) else 0 for key in inventory}

    def remove_item(self, inventory, item):
        """param inventory: dict - inventory dictionary. :param item: str - item to remove from the inventory.
        :return: dict - updated dictionary with item removed."""
        inventory.pop(item, None)
        return inventory

    def list_inventory(self, inventory):
        """:param inventory: dict - an inventory dictionary.:return: list of tuples - list of key, value pairs from the inventory dictionary."""
        return [i for i in list(inventory.items()) if i[1] != 0]

if __name__ == "__main__":
    w1 = warehouse()
    w1.create_inventory(['toaster','microwave','blender'])
    w1.add_items(appliances('toaster')) 