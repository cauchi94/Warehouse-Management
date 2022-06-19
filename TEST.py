#define a class for Warehouse where we store the total inventory and the the number of items per stock type
class Warehouse:
    #initiate the inventory list
    inventory = []
    #initiate the number of speakers, headphones and stereos
    n_speakers = 0
    n_headphones = 0
    n_stereos = 0
    #----DEL num_food = 0
    #----DEL num_book = 0
    #----DEL num_drink = 0

    #define a function that add items to specific stock type
    def add_items(self, n_items):
        #whatever we initiated the 'Stock' class with and the number of items we will add to the stock
        self.quantity = self.quantity + n_items 

    #define a function that returns the number of items present in the warehouse for specific stock type 
    def get_n_items(self):
        #quantity will be defined in the 'Stock' class which inherits from 'Warehouse' class
        return self.quantity 

    #define a function that removes items from specific stock type
    def remove_items(self, n_items):
        #whatever we initiated the 'Stock' class with and the number of items we will remove from the stock
        self.quantity = self.quantity - n_items 

    #define a funcion that allows to add inventory from scratch
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
    #define function that does not return anything and if it does we return None
    def __init__(self, name: str, quantity: int, type: str) -> None: 
        #specify name of the stock
        self.name = name
        #specify the number of items we currently have in the Warehouse
        self.quantity = quantity
        #specify the type of the stock chosen
        self.type = type

class Speakers(Stock):
    def __init__(self, name, quantity):
        #access the class we inherited from Stock using super() and add a 'type' argument (either Speakers, Headphones or Stereos)
        super().__init__(self, name, quantity, type)
        #add inventory list inherited from 'Warehouse' class with the initiation of the class that we shall define after (e.g. s1 = Speakers('In-Wall', 2, Speakers) )
        self.inventory.append(self)
        #specify the type of the stock
        self.type = 'Speakers'
        #increment number of speakers by the quantity added above
        warehouse.n_speakers += quantity

s1 = Speakers('InWall',4)