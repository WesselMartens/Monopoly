import pandas as pd
from tile import Start, Prison, Parking, GoToPrison, Station, Property

class Board:
    
    def __init__(self, config_name):
        self.config = self.load_config(config_name)
        self.tiles = self.construct_tiles()
        self.tile_groups = self.construct_tile_groups()
        self.tile_group_names = self.get_tile_group_names()
        self.length= len(self.tiles)
    
    def load_config(self, config_name):
        config_grid = pd.read_csv("config_board.csv")
        config_file = config_grid[config_grid.config_name == config_name]
        return config_file
    
    def construct_tiles(self):
        tiles = []
        for tile_idx in range(len(self.config)):
            tile_type, tile_name, tile_group, tile_price, tile_rent = self.config.loc[tile_idx][2:7]
            if tile_type == "Start":
                tile = Start(self, tile_idx, tile_name, tile_group)
            elif tile_type == "Prison":
                self.prison_index = tile_idx
                tile = Prison(self, tile_idx, tile_name, tile_group)
            elif tile_type == "Parking":
                tile = Parking(self, tile_idx, tile_name, tile_group)
            elif tile_type == "GoToPrison":
                tile = GoToPrison(self, tile_idx, tile_name, tile_group)
            elif tile_type == "Station":
                tile = Station(self, tile_idx, tile_name, tile_group, tile_price, tile_rent)
            elif tile_type == "Property":
                tile = Property(self, tile_idx, tile_name, tile_group, tile_price, tile_rent)
            tiles.append(tile)
        return tiles

    def construct_tile_groups(self):
        tile_groups = {}
        for tile in self.tiles:
            tile_groups.setdefault(tile.group, []).append(tile)
        return tile_groups
    
    def get_tile_group_names(self):
        return sorted(self.tile_groups.keys())
    
    def display(self):
        for tile in self.tiles:
            tile.display()