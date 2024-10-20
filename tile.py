class Tile:    
    def __init__(self, index, name, group):
        self.name = name
        self.index = index
        self.group = group

class Start(Tile):
    def __init__(self, index, name, group):
        super().__init__(index, name, group)
        
    def display(self):
        print(f"Tile: {self.index} \t Name: {self.name}")

class Property(Tile):
    def __init__(self, index, name, group, price, rent):
        super().__init__(index, name, group)
        self.price = price
        self.rent = rent
        self.owner = None
    
    def display(self):
        print(f"Tile: {self.index} \t Name: {self.name} \t Owner: {self.owner} \t Price: {self.price}")
        