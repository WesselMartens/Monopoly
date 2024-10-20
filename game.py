class Player:
    
    def __init__(self, name, money):
        self.name = name
        self.money = money
        
        self.properties = []
    
class Property:
    
    def __init__(self, name, country, price, rent):
        self.name = name
        self.country = country
        self.price = price
        self.rent = rent
    
class Board:
    
    def __init__(self, length, width, properties):
        self.length = length
        self.width = width
        self.properties = []