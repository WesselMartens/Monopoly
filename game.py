from board import Board
from player import Player

class Game:
    def __init__(self, config, players, money):
        self.board = Board(config)
        self.players = [Player(name, money, self.board) for name in players]
        self.game_over = False
        self.welcome()

    def play(self):
        while self.game_over != True:
            for player in self.players:
                if player.bankrupt:
                    pass
                else:
                    input(f"Player {player} - press a key to start turn.")
                    player.summary()
                    player.run_turn()
                    print()

    def welcome(self):
        print()
        print("Welcome to Monopoly!")
        print(f"Players: {', '.join(f'{player.name}' for player in self.players)}")
        print()
        self.board.display()
        print()

t = Game(config="Standard", players=["Wessel"], money=1500)
t.play()