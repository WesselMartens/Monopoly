class Tile:    
    def __init__(self, index, name):
        self.name = name
        self.index = index

class Start(Tile):
    def __init__(self, index, name):
        super().__init__(index, name)
        
    def display(self):
        print(f"Tile: {self.index} \t Name: {self.name}")

class Property(Tile):
    def __init__(self, index, name, price, rent):
        super().__init__(index, name)
        self.price = price
        self.rent = rent
        self.owner = None
    
    def display(self):
        print(f"Tile: {self.index} \t Name: {self.name} \t Owner: {self.owner} \t Price: {self.price}")
        