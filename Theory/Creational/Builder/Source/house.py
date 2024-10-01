class House:
    def __init__(self, walls, doors, has_pool, has_roof, color) -> None:
        self.walls = walls
        self.doors = doors
        self.has_pool = has_pool
        self.has_roof = has_roof
        self.color = color

    def __str__(self) -> str:
        return f"House(walls={self.walls}, doors={self.doors}, has_pool={self.has_pool}, has_roof={self.has_roof}, color='{self.color}')"
    
    """ def get_walls(self):
        return self.walls

    def get_doors(self):
        return self.doors

    def has_pool(self):
        return self.has_pool

    def has_roof(self):
        return self.has_roof

    def get_color(self):
        return self.color """