class Warehouse:
    inventory =[]
    num_food = 0
    num_book = 0
    num_drink = 0

    def add_items(self, num_items):
        self.quantity = self.quantity + num_items

    def get_num_items(self):
        return self.quantity

    def remove_items(self, num_items):
        self.quantity = self.quantity - num_items

    def make_inventory(self):
        print('Name -- Quantity -- Type')
        for items in self.inventory:
            print(f'{items.name} ---- {items.quantity} ---- {items.type}')
        print('---------------------------')

    def total_items(self):
        tot = 0
        for items in self.inventory:
            tot += items.quantity
        return tot

class Stock(Warehouse):
    def __init__(self, name: str, quantity: int, type: str) -> None:
        self.name = name
        self.quantity = quantity
        self.type = type


class Food(Stock):
    def __init__(self, name, quantity):
        Stock.__init__(self, name, quantity, type)
        self.inventory.append(self)
        self.type = 'Food'
        ware.num_food += quantity


class Drink(Stock):
    def __init__(self, name, quantity):
        Stock.__init__(self, name, quantity, type)
        self.inventory.append(self)
        self.type = 'Drink'
        ware.num_drink += quantity


class Book(Stock):
    def __init__(self, name, quantity):
        Stock.__init__(self, name, quantity, type)
        self.type = 'Book'
        self.inventory.append(self)
        ware.num_book += quantity

if __name__ == "__main__":
    ware = Warehouse()
    print(f'Warehouse has {ware.total_items()} total items')
    print('Adding test items...')
    book1 = Book('school manual', 4)
    book2 = Book('math book', 8)
    food1 = Food('Rice', 20)
    food2 = Food('Beans', 15)
    drink1 = Drink('Gin', 9)
    print(f'Warehouse has {ware.total_items()} total items')
    inp = int(input('Make inventory? 1-yes 2-no '))
    print()
    if inp == 1:
        ware.make_inventory()
    print()
    inp1 = int(input('Want to add another item? 1-yes 2-no '))
    if inp1 == 1:
        inp2 = int(input('1-Food 2-Drink 3-Book '))
        name = input('Name of item: ')
        quant = int(input('Quantity of item: '))
        if inp2 == 1:
            new_item = Food(name,quant)
        elif inp2 == 2:
            new_item =Drink(name,quant)
        else:
            new_item = Book(name,quant)
    print()
    inp = int(input('Make inventory? 1-yes 2-no '))
    print()
    if inp == 1:
        ware.make_inventory()
    print()
    inp1 = int(input('Want to add/remove item? 1-add 2-remove 0-pass '))
    if inp1 == 1:
        list_items = [x.name for x in ware.inventory]
        name = input('Name of item: ')
        quant = int(input('Quantity of item: '))
        item = ware.inventory[list_items.index(name)]
        item.add_items(quant)
    elif inp1 == 2:
        list_items = [x.name for x in ware.inventory]
        name = input('Name of item: ')
        quant = int(input('Quantity of item: '))
        item = ware.inventory[list_items.index(name)]
        item.remove(quant)
    else:
        pass
    print()
    inp = int(input('Make inventory? 1-yes 2-no '))
    print()
    if inp == 1:
        ware.make_inventory()
    print()
    print(f'Warehouse has {ware.total_items()} total items')
    print()
    inp = int(input('Number of items for certain Stock: 1- Food 2- Drink 3- Book 0-pass '))
    if inp == 1:
        print(f'There are {ware.num_food} items of type Food')
    elif inp == 2:
        print(f'There are {ware.num_drink} items of type Drink')
    elif inp == 3:
        print(f'There are {ware.num_book} items of type Book')
    print()
    inp = int(input('Want to search if item is available? 1-yes 2-no '))
    if inp == 1:
        name = input('Name of item: ')
        list_items = [x.name for x in ware.inventory]
        if name in list_items:
            item = ware.inventory[list_items.index(name)]
            print(f'{name} is available and current stock is: {item.get_num_items()}')
        else:
            print(f'{name} is not available')








