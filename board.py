import pandas as pd
from tile import Start, Property

class Board:
    
    def __init__(self, config_name):
        self.config = self.get_config(config_name)
        self.tiles = self.construct_tiles()
        self.tile_groups = self.construct_tile_groups()
    
    def get_config(self, config_name):
        config_grid = pd.read_csv("config_board.csv")
        config_file = config_grid[config_grid.config_name == config_name]
        return config_file
    
    def construct_tiles(self):
        tiles = []
        for tile_idx in range(len(self.config)):
            tile_type, tile_name, tile_group = self.config.loc[tile_idx][2:5]
            if tile_type == "start":
                tile = Start(tile_idx, tile_name, tile_group)
            elif tile_type == "property":
                tile_price, tile_rent = self.config.loc[tile_idx][5:7]
                tile = Property(tile_idx, tile_name, tile_group, tile_price, tile_rent)
            tiles.append(tile)
        return tiles

    def construct_tile_groups(self):
        tile_groups = {}
        for tile in self.tiles:
            tile_groups.setdefault(tile.group, []).append(tile)
        return tile_groups
    
    def display(self):
        for tile in self.tiles:
            tile.display()