from builder import Builder
from house import House

class HouseBuilder(Builder):
    def __init__(self) -> None:
        self.walls = 0
        self.doors = 0
        self.has_pool = False
        self.has_roof = False
        self.color = "undefined"

    def build_roof(self, has_roof):
        print(f"Building roof: {'Yes' if has_roof else 'No'}")
        self.has_roof = has_roof
        return self

    def build_walls(self, walls):
        print(f"Building {walls} walls")
        self.walls = walls
        return self

    def build_pool(self, has_pool):
        print(f"Adding pool: {'Yes' if has_pool else 'No'}")
        self.has_pool = has_pool
        return self

    def build_doors(self, doors):
        print(f"Adding {doors} doors")
        self.doors = doors
        return self

    def with_color(self, color):
        print(f"Painting house with color: {color}")
        self.color = color
        return self

    def build(self):
        # Trả về đối tượng House sau khi đã thiết lập xong
        print("House construction completed.")
        return House(self.walls, self.doors, self.has_pool, self.has_roof, self.color)