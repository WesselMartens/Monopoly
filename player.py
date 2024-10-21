import numpy as np

class Player:
    def __init__(self, name, money, board):
        self.name = name
        self.money = money
        self.board = board
        
        self.position = 0
        self.tile = board.tiles[0]
        self.properties = []
    
        self.jail_turns = 0
        self.bankrupt = False
    
    def __str__(self):
        return self.name

    def run_turn(self):
        if self.jail_turns > 0:
            print(f"Player {self} is in jail for another {self.jail_turns} turn(s).")
            self.jail_turns -= 1
        else:
            self.move()
            self.tile.interact(self)

    def move(self):
        input(f"Player {self} - press a key to throw dice.")
        dice = np.sum(np.random.choice([1,2,3,4,5,6], size=2))
        self.change_position(dice)
        print(f"Player {self} throws {dice} and moves to tile {self.position}: {self.tile}")

    def change_position(self, number, mode='relative'):
        if mode == 'relative':
            if (self.position + number) > self.board.length:
                self.money += 200 # pass start
            self.position = (self.position + number) % self.board.length
        elif mode == 'absolute':
            self.position = number
        self.tile = self.board.tiles[self.position]
    
    def buy_property(self, property_):
        if self.money >= property_.price:
            self.money -= property_.price
            self.properties.append(property_)
            property_.owner = self
        else:
            print(f"Player {self} does not have sufficient funds to buy {property_}.")
    
    def summary(self):
        print()
        print(f"Player: {self}")
        print(f"Position: {self.position} ({self.tile})")
        print(f"Money: {self.money}")
        print(f"Properties: {', '.join(f'{property.name}' for property in self.properties)}")
        print()