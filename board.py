import pandas as pd
from tile import Start, Property

class Board:
    
    def __init__(self, config_name):
        self.config = self.get_config(config_name)
        self.tiles = self.construct_tiles(self.config)
    
    def get_config(self, config_name):
        config_grid = pd.read_csv("config_board.csv")
        config_file = config_grid[config_grid.config_name == config_name]
        return config_file
    
    def construct_tiles(self, config_grid):
        tiles = []
        for tile_idx in range(len(config_grid)):
            tile_type, tile_name, tile_group = config_grid.loc[tile_idx][2:5]
            if tile_type == "start":
                tile = Start(tile_idx, tile_name, tile_group)
            elif tile_type == "property":
                tile_price, tile_rent = config_grid.loc[tile_idx][5:7]
                tile = Property(tile_idx, tile_name, tile_group, tile_price, tile_rent)
            tiles.append(tile)
        return tiles
    
    def display(self):
        for tile in self.tiles:
            tile.display()