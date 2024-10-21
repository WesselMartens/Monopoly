class Tile:    
    def __init__(self, board, index, name, group):
        self.board = board
        self.name = name
        self.index = index
        self.group = group
    
    def __str__(self):
        return self.name
    
    def display(self):
        print(f"Tile: {self.index} \t Name: {self.name} \t Group: {self.group}")

class Start(Tile):
    def __init__(self, board, index, name, group):
        super().__init__(board, index, name, group)

    def interact(self, player):
        print(f"Player {player} lands on start and receives an extra $200!")
        player.money += 200

class Prison(Tile):
    def __init__(self, board, index, name, group):
        super().__init__(board, index, name, group)
    
    def interact(self, player):
        print(f"Player {player} goes to jail!")
        player.jail_turns = 3
        
class Parking(Tile):
    def __init__(self, board, index, name, group):
        super().__init__(board, index, name, group)

    def interact(self, player):
        print(f"Player {player} lands on parking and receives $100!")
        player.money += 100

class GoToPrison(Tile):
    def __init__(self, board, index, name, group):
        super().__init__(board, index, name, group)

    def interact(self, player):
        print(f"Player {player} goes to jail!")
        player.change_position(self.board.prison_index, mode='absolute')
        player.jail_turns = 3

class Property(Tile):
    def __init__(self, board, index, name, group, price, rent):
        super().__init__(board, index, name, group)
        self.price = price
        self.rent = rent
        self.owner = None    
    
    def interact(self, player):
        if self.owner == player:
            print(f"Player {player} owns this property and does not pay rent.")
        elif self.owner == None:
            print(f"Property {self} has no owner, so player {player} tries to buy it.")
            player.buy_property(self)
        else:
            print(f"Property {self} has owner {self.owner} and charges rent {self.rent}.")
            self.charge_rent(player)
    
    def charge_rent(self, player):
        if player.money >= self.rent:
            self.owner.money += self.rent
            player.money -= self.rent
        else:
            self.owner.money += self.rent
            player.bankrupt = True
    
class Station(Tile):
    def __init__(self, board, index, name, group, price, rent):
        super().__init__(board, index, name, group)
        self.price = price
        self.rent = rent
        self.owner = None
    
    def interact(self, player):
        if self.owner == player:
            print(f"Player {player} owns this station and does not pay rent.")
        elif self.owner == None:
            print(f"Station {self} has no owner, so player {player} buys it.")
            player.buy_property(self)
        else:
            print(f"Station {self} has owner {self.owner} and charges rent {self.rent}.")
            self.charge_rent(player)
        
    def charge_rent(self, player):
        if player.money >= self.rent:
            self.owner.money += self.rent
            player.money -= self.rent
        else:
            self.owner.money += self.rent
            player.bankrupt = True
